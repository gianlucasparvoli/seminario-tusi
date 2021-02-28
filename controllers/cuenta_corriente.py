from flask import Flask, request, jsonify,render_template, flash
from flask.views import MethodView
from database import *
from sqlalchemy.sql import select
import smtplib
from email.mime.text import MIMEText
import random
import string
import datetime
import json

# class prizeEndPoint(MethodView):
#     def get(self):
#         return render_template("gestion-premios.html")

class currentAccountNewEndPoint(MethodView):
    def get(self):
        return render_template("alta-cuenta-corriente.html")

class currentAccountAddEndPoint(MethodView):
    def post(self):
        
        cliente = request.form['cliente']
        #prodYJug = request.form['prodYJug[0][producto]']
        observaciones = request.form['observaciones']
        total = request.form['total']
        fechamov = datetime.datetime.now()
        cantProd = int(request.form['cantProd'])

        

        #print(cliente,observaciones,total)
        
        #FALTA SOLAMENTE GUARDAR prodCC

        new_CC= Cuenta_Corriente(cliente,observaciones,fechamov,total)
        db.session.add(new_CC)
        db.session.commit()

        cc = Cuenta_Corriente.query.filter_by(clienteid=cliente,observaciones=observaciones,monto=total).all() 
        ccIngresada = cuentas_corrientes_schema.dump(cc)
        for x in ccIngresada:
            idCC=x["id"]
            
        for x in range(cantProd):
            producto = request.form['prodYJug['+str(x)+'][producto]']
            jugada = request.form['prodYJug['+str(x)+'][num_jugada]']
            new_prod_CC= ProductosCC(producto,jugada,idCC)
            db.session.add(new_prod_CC)
                
        db.session.commit()
        db.session.close()
        
        flash("CC Registrado")
        return render_template('alta-cuenta-corriente.html')

class currentAccountAllEndPoint(MethodView):
    def get(self):
        cc = Cuenta_Corriente.query.all()
        s = cuentas_corrientes_schema.dump(cc)
        productoscc = ProductosCC.query.all()
        x = productosCC_schema.dump(productoscc)
        return jsonify(s,x)

# class prizeReportEndPoint(MethodView):
#     def get(self):
#         return render_template("reportes-premios.html")