from flask import Flask, request, jsonify,render_template, flash
from flask.views import MethodView
from database import *
from sqlalchemy.sql import select
import smtplib
from email.mime.text import MIMEText
import random
import string
import datetime

class productAllEndPoint(MethodView):
    def get(self):
        preoduct = Producto.query.all()
        s = productos_schema.dump(preoduct)
        return jsonify(s)

class productEndPoint(MethodView):
    def get(self):
        return render_template("gestion-productos.html")

class productIDEndPoint(MethodView):
    def get(self, id):
        producto = Producto.query.filter_by(id=id).all()
        s = productos_schema.dump(producto)
        return jsonify(s)

    def delete(self, id):
        prod = Producto.query.get(id)
        db.session.delete(prod)
        db.session.commit()
        return jsonify("OK")

class modifyProductEndPoint(MethodView): 
    def post(self):
        id = request.form['id']
        prod = Producto.query.get(id)

        precio = request.form['precio']
        nombre = request.form['nombre']

        prod.precio=precio
        prod.nombre=nombre

        db.session.commit()
        
        new_prodHist= ProductoHistorial(id, datetime.datetime.now(), precio)
        db.session.add(new_prodHist)
        db.session.commit()

        db.session.close()

        return render_template('gestion-productos.html')

class productNewEndPoint(MethodView):
    def get(self):
        return render_template("alta-productos.html")

class productAddEndPoint(MethodView):
    def post(self):
        nombre = request.form['Nombre']
        precio = request.form['Precio']
        
        new_prod= Producto(nombre,precio)
        db.session.add(new_prod)
        db.session.commit()
                
        db.session.close()
        
        flash("Alta de producto '" + nombre + "' correcta")
        return render_template('alta-productos.html')

class reportProductEndPoint(MethodView):
    def get(self):
        return render_template("reporte-productos.html")

class historyProductEndPoint(MethodView):
    def get(self):
        return render_template("productos-historial.html")

class historyAllProductEndPoint(MethodView):
    def get(self):
        prodHist = ProductoHistorial.query.all()
        s = ProductosHistorial_schema.dump(prodHist)
        return jsonify(s)