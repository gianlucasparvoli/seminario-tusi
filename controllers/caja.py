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