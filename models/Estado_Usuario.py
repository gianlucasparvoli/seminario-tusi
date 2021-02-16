from app import db,app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class Estado_Usuario(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre

db.create_all()


class StateUserSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre')

estado_usuario_schema = StateUserSchema()  #Uno solo (POST,GET)
estados_usuarios_schema = StateUserSchema(many=True) #Varios (GET)