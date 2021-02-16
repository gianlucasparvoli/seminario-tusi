from app import db,app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class Accion(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)
    formulario=db.Column(db.String(50), ForeignKey('Formulario.id'))

    formularioFK = relationship(Formulario)

    def __init__(self, nombre,formulario):
        self.nombre = nombre
        self.formulario = formulario

db.create_all()


class AccionSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','formulario')

accion_schema = AccionSchema()  #Uno solo (POST,GET)
acciones_schema = AccionSchema(many=True) #Varios (GET)