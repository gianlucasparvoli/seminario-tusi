from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='SecretKey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/db.db'

db=SQLAlchemy(app)


from routes.index import *
from routes.usuario import *
from routes.grupo import *
from routes.grupos_usuario import *
from routes.acciones_grupo import *
from routes.accion import *
from routes.formulario import *
from routes.modulo import *
from routes.producto import *
from routes.cliente import *
from routes.ventas import *
from routes.premio import *

#from routes.routes import *

if __name__=='__main__':
    app.run(debug=True)

