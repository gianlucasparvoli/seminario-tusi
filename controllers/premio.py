from flask import Flask, request, jsonify,render_template, flash
from flask.views import MethodView
from database import *
from sqlalchemy.sql import select
import smtplib
from email.mime.text import MIMEText
import random
import string
import datetime

class prizeEndPoint(MethodView):
    def get(self):
        return render_template("gestion-premios.html")

class prizeNewEndPoint(MethodView):
    def get(self):
        return render_template("alta-premios.html")

class prizeAddEndPoint(MethodView):
    def post(self):
        usuario = request.form['Usuario']
        producto = request.form['Producto']
        cantidad = request.form['Cantidad']
        fecha = datetime.datetime.now()
        premio = request.form['Premio']
        
        new_prize= Premio(usuario,producto,cantidad,fecha,premio)
        db.session.add(new_prize)
        db.session.commit()
                
        db.session.close()
        
        flash("Premio Registrado")
        return render_template('alta-premios.html')

class prizeAllEndPoint(MethodView):
    def get(self):
        premio = Premio.query.all()
        s = premios_schema.dump(premio)
        return jsonify(s)

class prizeReportEndPoint(MethodView):
    def get(self):
        return render_template("reportes-premios.html")