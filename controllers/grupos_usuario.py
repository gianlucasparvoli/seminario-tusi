from flask import Flask, request, jsonify,render_template
from flask.views import MethodView
from database import *
from sqlalchemy.sql import select

class GruposUsuariosEndPoint(MethodView):
    def get(self):
        all_group = Grupos_Usuario.query.all()
        result = grupos_usuarios_schema.dump(all_group)
        return jsonify(result)

class GruposUsuarioEndPoint(MethodView):
    def get(self, id):
        user = Grupos_Usuario.query.filter_by(usuarioid=id).all()
        s = grupos_usuarios_schema.dump(user)
        return jsonify(s)