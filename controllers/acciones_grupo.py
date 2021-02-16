from flask import Flask, request, jsonify,render_template
from flask.views import MethodView
from database import *
from sqlalchemy.sql import select

class AccionesGruposEndPoint(MethodView):
    def get(self):
        all_group = Acciones_Grupo.query.all()
        result = acciones_grupos_schema.dump(all_group)
        return jsonify(result)

class AccionesGrupoEndPoint(MethodView):
    def get(self, id):
        user = Acciones_Grupo.query.filter_by(grupoid=id).all()
        s = acciones_grupos_schema.dump(user)
        return jsonify(s)