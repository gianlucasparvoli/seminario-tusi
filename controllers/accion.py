from flask import Flask, request, jsonify,render_template
from flask.views import MethodView
from database import *
from sqlalchemy.sql import select

class AccionEndPoint(MethodView):
    def get(self, id):
        user = Accion.query.filter_by(id=id).all()
        s = acciones_schema.dump(user)
        return jsonify(s)

class AccionFormularioEndPoint(MethodView):
    def get(self, id):
        form = Accion.query.filter_by(formulario=id).all()
        s = acciones_schema.dump(form)
        return jsonify(s)