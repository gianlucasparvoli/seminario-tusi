from flask import Flask, request, jsonify,render_template, flash
from flask.views import MethodView
from database import *
from sqlalchemy.sql import select
import smtplib
from email.mime.text import MIMEText
import random
import string

class clientEndPoint(MethodView):
    def get(self):
        return render_template("gestion-clientes.html")

class clientAllEndPoint(MethodView):
    def get(self):
        client = Cliente.query.all()
        s = clientes_schema.dump(client)
        return jsonify(s)
    

class clientIDEndPoint(MethodView):
    def get(self, id):
        cliente = Cliente.query.filter_by(id=id).all()
        s = clientes_schema.dump(cliente)
        return jsonify(s)
    def delete(self, id):
        client = Cliente.query.get(id)
        db.session.delete(client)
        db.session.commit()
        return jsonify("OK")

class modifyClientEndPoint(MethodView): 
    def post(self):
        id = request.form['id']
        cli = Cliente.query.get(id)
        print(id,cli)

        direccion = request.form['direccion']
        telefono = request.form['telefono']
        nombre = request.form['nombre']

        cli.direccion=direccion
        cli.telefono=telefono
        cli.nombre=nombre

        db.session.commit()
        flash("Modificacion de cliente '" + nombre + "' correcta")
        return render_template('gestion-clientes.html')

class clientNewEndPoint(MethodView):
    def get(self):
        return render_template("alta-clientes.html")


class clientAddEndPoint(MethodView):
    def post(self):
        nombre = request.form['Nombre']
        direccion = request.form['Direccion']
        telefono = request.form['Telefono']
        
        new_prod= Cliente(nombre,direccion,telefono)
        db.session.add(new_prod)
        db.session.commit()
                
        db.session.close()
        
        flash("Alta de cliente '" + nombre + "' correcta")
        return render_template('alta-clientes.html')