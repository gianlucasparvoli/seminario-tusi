from flask import Flask, request, jsonify,render_template, flash
from flask.views import MethodView
from database import *
from sqlalchemy.sql import select
import smtplib
from email.mime.text import MIMEText
import random
import string
import datetime

class sellEndPoint(MethodView):
    def get(self):
        return render_template("alta-ventas.html")

class sellAddEndPoint(MethodView):
    def post(self):
        clienteid = request.form['Cliente']
        productoid = request.form['Producto']
        cantidad = request.form['Cantidad']
        fecha = datetime.datetime.now()
        
        new_sell= Venta(clienteid,productoid,cantidad,fecha)
        db.session.add(new_sell)
        db.session.commit()
                
        db.session.close()
        
        flash("Ventas Registrada")
        return render_template('alta-ventas.html')

class sellAllEndPoint(MethodView):
    def get(self):
        venta = Venta.query.all()
        s = ventas_schema.dump(venta)
        return jsonify(s)
    

class sellIDEndPoint(MethodView):
    def get(self, id):
        venta = Venta.query.filter_by(id=id).all()
        s = ventas_schema.dump(venta)
        return jsonify(s)
    def delete(self, id):
        sell = Venta.query.get(id)
        db.session.delete(sell)
        db.session.commit()
        return jsonify("OK")

#class modifySellEndPoint(MethodView): 
    # def post(self):
    #     id = request.form['id']
    #     cli = Venta.query.get(id)

    #     direccion = request.form['direccion']
    #     telefono = request.form['telefono']
    #     nombre = request.form['nombre']

    #     cli.direccion=direccion
    #     cli.telefono=telefono
    #     cli.nombre=nombre

    #     db.session.commit()
    #     flash("Modificacion de cliente '" + nombre + "' correcta")
    #     return render_template('gestion-clientes.html')

class sellViewEndPoint(MethodView):
    def get(self):
        return render_template("gestion-ventas.html")