from app import db,app
from flask_marshmallow import Marshmallow
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

ma = Marshmallow(app)

class Modulo(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)

    # moduloFK = relationship("Formulario")
    
    def __init__(self, nombre):
        self.nombre = nombre

db.create_all()


class ModuleSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre')

modulo_schema = ModuleSchema()  #Uno solo (POST,GET)
modulos_schema = ModuleSchema(many=True) #Varios (GET)