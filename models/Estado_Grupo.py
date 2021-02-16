from app import db,app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class Estado_Grupo(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre

db.create_all()


class StateGroupSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre')

estado_grupo_schema = StateGroupSchema()  #Uno solo (POST,GET)
estados_grupos_schema = StateGroupSchema(many=True) #Varios (GET)