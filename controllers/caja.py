from flask import Flask, request, jsonify,render_template, flash
from flask.views import MethodView
from database import *
from sqlalchemy.sql import select
import smtplib
from email.mime.text import MIMEText
import random
import string
import datetime

class cajaEndPoint(MethodView):
    def get(self):
        return render_template("caja.html")

class cajaLastEndPoint(MethodView):
    def get(self):
        ultimaCaja = Caja.query.all()
        s = CajasSchema_schema.dump(ultimaCaja)
        return jsonify(s[len(s) - 1])

class cajaAddEndPoint(MethodView):
    def post(self):
        ventaMostrador = request.form['ventaMostrador']
        efectivoInicial = request.form['efectivoInicial']
        ventaSistema = request.form['ventaSistema']
        premiosEnLinea = request.form['premiosEnLinea']
        deposito = request.form['deposito']
        gastos = request.form['gastos']
        ventaCtaCte = request.form['ventaCtaCte']
        cobroCtaCte = request.form['cobroCtaCte']
        sube = request.form['sube']
        saldoFinal = request.form['saldoFinal']
        efectivoCierreCaja = request.form['efectivoCierreCaja']
        diferencia = request.form['diferencia']
        comision = request.form['comision']

        new_caja= Caja(ventaMostrador,efectivoInicial,ventaSistema,premiosEnLinea,deposito,gastos,ventaCtaCte,cobroCtaCte, sube,saldoFinal, efectivoCierreCaja,diferencia,comision)
        db.session.add(new_caja)
        db.session.commit()
                
        db.session.close()
        
        flash("Alta de caja correcta")
        return render_template('caja.html')