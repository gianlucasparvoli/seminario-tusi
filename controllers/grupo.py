from flask import Flask, request, jsonify,render_template
from flask.views import MethodView
from database import *
from sqlalchemy.sql import select
import json

class GruposEndPoint(MethodView):
    def get(self):
        # grupos = Grupo.query.all()
        all_group = Grupo.query.all()
        result = grupos_schema.dump(all_group)
        return jsonify(result)

class GruposGestionEndPoint(MethodView):
    def get(self,id):
        # all_users = select([usuario])
        # result = users_schema.dump(all_users)
        # return jsonify(result)
        return render_template('gestion-grupos.html',value=id)

class AddGrupoEndPoint(MethodView):
    def post(self):
        nombre = request.form.get('nombreGrupo')
        estado = request.form.get('estado')

        new_group= Grupo(nombre,estado)
        db.session.add(new_group)
        db.session.commit()
        
        user = Grupo.query.filter_by(nombre=nombre).all()     
        grupoIngresado = usuarios_schema.dump(user)
        for x in grupoIngresado:
            idgrupo=x["id"]

        return idgrupo