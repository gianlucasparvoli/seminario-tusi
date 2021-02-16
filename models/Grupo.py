from app import db,app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class Grupo(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)
    acciones=db.Column(db.ARRAY(String(50)), ForeignKey('Accion.id'))
    estado=db.Column(db.String(50), ForeignKey('Estado_Grupo.id'))

    accionFK = relationship(Accion)
    estadoGrupoFK = relationship(Estado_Grupo)

    def __init__(self, nombre, acciones,estado):
        self.nombre = nombre
        self.acciones = acciones
        self.estado = estado

db.create_all()


class GroupSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','acciones','estado')

grupo_schema = GroupSchema()  #Uno solo (POST,GET)
grupos_schema = GroupSchema(many=True) #Varios (GET)