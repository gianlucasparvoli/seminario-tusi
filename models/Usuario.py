from app import db,app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class Usuario(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)
    apellido=db.Column(db.String(50),nullable=False)
    mail=db.Column(db.String(50),nullable=False)
    usuario=db.Column(db.String(50),nullable=False)
    clave=db.Column(db.String(50),nullable=False)
    grupos=db.Column(db.ARRAY(String(50)), ForeignKey('Grupo.id'))
    estado=db.Column(db.String(50), ForeignKey('Estado_Usuario.id'))

    grupoFK = relationship(Grupo)
    estadoUsuarioFK = relationship(Estado_Usuario)

    def __init__(self, nombre, apellido,mail,usuario,clave,grupos,estado):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.usuario = usuario
        self.clave = clave
        self.grupos = grupos
        self.estado = estado

db.create_all()


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','apellido','mail','usuario','clave','grupos','estado')

usuario_schema = UserSchema()  #Uno solo (POST,GET)
usuarios_schema = UserSchema(many=True) #Varios (GET)