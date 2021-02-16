from flask import Flask, request, jsonify,render_template
from flask.views import MethodView
from database import *
from sqlalchemy.sql import select

class FormularioEndPoint(MethodView):
    def get(self, id):
        form = Formulario.query.filter_by(id=id).all()
        s = formularios_schema.dump(form)
        return jsonify(s)

class FormularioModEndPoint(MethodView):
    def get(self, id):
        form = Formulario.query.filter_by(modulo=id).all()
        s = formularios_schema.dump(form)
        return jsonify(s)