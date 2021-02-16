from app import db,app
from flask_marshmallow import Marshmallow
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

ma = Marshmallow(app)

class Formulario(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)
    modulo=db.Column(db.String(50), ForeignKey('modulo.id'))

    moduloFK = relationship(modulo)

    def __init__(self, nombre,modulo):
        self.nombre = nombre
        self.modulo = modulo

db.create_all()


class FormSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','modulo')

formulario_schema = FormSchema()  #Uno solo (POST,GET)
formularios_schema = FormSchema(many=True) #Varios (GET)