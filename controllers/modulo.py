from flask import Flask, request, jsonify,render_template
from flask.views import MethodView
from database import *
from sqlalchemy.sql import select

class ModuloEndPoint(MethodView):
    def get(self, id):
        modulo = Modulo.query.filter_by(id=id).all()
        s = modulos_schema.dump(modulo)
        return jsonify(s)

class ModulosEndPoint(MethodView):
    def get(self):
        modulo = Modulo.query.all()
        s = modulos_schema.dump(modulo)
        return jsonify(s)


