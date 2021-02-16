from flask import Flask, request, jsonify,render_template
from flask.views import MethodView

class IndexEndPoint(MethodView):
    def get(self):
        return render_template('inicio.html')
        # jsonify({'message': 'Welcome to API - Seminario - UTN FRSN'})