from app import db,app
from flask_marshmallow import Marshmallow
from sqlalchemy import Table, Column, Integer, ForeignKey,UniqueConstraint
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


ma = Marshmallow(app)

class Modulo(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)
    
    def __init__(self, nombre):
        self.nombre = nombre
    
class ModuloSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre')
modulo_schema = ModuloSchema()  #Uno solo (POST,GET)
modulos_schema = ModuloSchema(many=True) #Varios (GET)


class Formulario(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)
    modulo=db.Column(db.String(50), ForeignKey('modulo.id'))

    moduloFK = relationship(Modulo)

    def __init__(self, nombre,modulo):
        self.nombre = nombre
        self.modulo = modulo

class FormularioSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','modulo')
formulario_schema = FormularioSchema()  #Uno solo (POST,GET)
formularios_schema = FormularioSchema(many=True) #Varios (GET)


class Accion(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)
    formulario=db.Column(db.String(50), ForeignKey('formulario.id'))

    formularioFK = relationship(Formulario)

    def __init__(self, nombre,formulario):
        self.nombre = nombre
        self.formulario = formulario

class AccionSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','formulario')
accion_schema = AccionSchema()  #Uno solo (POST,GET)
acciones_schema = AccionSchema(many=True) #Varios (GET)


class Estado_Grupo(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre

class Estado_GrupoSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre')
estado_grupo_schema = Estado_GrupoSchema()  #Uno solo (POST,GET)
estados_grupos_schema = Estado_GrupoSchema(many=True) #Varios (GET)


class Grupo(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)
    # acciones=(db.Integer,autoincrement=True)
    # acciones=db.Column(db.ARRAY(Integer), ForeignKey('accion.id'))
    estado_grupo=db.Column(db.String(50), ForeignKey('estado__grupo.id'))

    # accionFK = relationship(acciones)
    estadoGrupoFK = relationship(Estado_Grupo)

    def __init__(self,nombre,estado_grupo):
        self.nombre = nombre
        self.estado_grupo = estado_grupo

class GroupSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','estado_grupo')
grupo_schema = GroupSchema()  #Uno solo (POST,GET)
grupos_schema = GroupSchema(many=True) #Varios (GET)


class Acciones_Grupo(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    grupoid=db.Column(db.Integer, ForeignKey('grupo.id'))
    accionid=db.Column(db.Integer,ForeignKey('accion.id'))
    __table_args__ = (db.UniqueConstraint('grupoid', 'accionid', name='_uidx_Acciones_Grupo'), )

    grupoidFK = relationship(Grupo)
    accionFK = relationship(Accion)

    def __init__(self, grupoid, accionid):
        self.grupoid = grupoid
        self.accionid = accionid

class AccionGroupSchema(ma.Schema):
    class Meta:
        fields = ('id','grupoid','accionid')
accion_grupo_schema = AccionGroupSchema()  #Uno solo (POST,GET)
acciones_grupos_schema = AccionGroupSchema(many=True) #Varios (GET)


class Estado_Usuario(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre

class StateUserSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre')
estado_usuario_schema = StateUserSchema()  #Uno solo (POST,GET)
estados_usuarios_schema = StateUserSchema(many=True) #Varios (GET)


class Usuario(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)
    apellido=db.Column(db.String(50),nullable=False)
    mail=db.Column(db.String(50),nullable=False)
    usuario=db.Column(db.String(50))
    clave=db.Column(db.String(50))
    #grupos=db.Column(db.ARRAY(String(50)), ForeignKey('Grupo.id'))
    estado=db.Column(db.String(50), ForeignKey('estado__usuario.id'))

    # grupoFK = relationship(Grupo)
    estadoUsuarioFK = relationship(Estado_Usuario)

    # def set_password(self, password):
    #     self.clave = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.clave, password)

    def __init__(self, nombre, apellido,mail,usuario,clave,estado):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.usuario = usuario
        self.clave = clave
        self.estado = estado

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','apellido','mail','usuario','clave','estado')
usuario_schema = UserSchema()  #Uno solo (POST,GET)
usuarios_schema = UserSchema(many=True) #Varios (GET)


class Grupos_Usuario(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    usuarioid=db.Column(db.Integer,ForeignKey('usuario.id'))
    grupoid=db.Column(db.Integer, ForeignKey('grupo.id'))
    __table_args__ = (db.UniqueConstraint('usuarioid', 'grupoid', name='_uidx_grupos_usuario'), )

    grupoidFK = relationship(Grupo)
    usuarioFK = relationship(Usuario)

    def __init__(self, usuarioid, grupoid):
        self.usuarioid = usuarioid
        self.grupoid = grupoid

class GroupUserSchema(ma.Schema):
    class Meta:
        fields = ('id','usuarioid','grupoid')
grupo_usuario_schema = GroupUserSchema()  #Uno solo (POST,GET)
grupos_usuarios_schema = GroupUserSchema(many=True) #Varios (GET)

# HASTA ACA MODULO DE SEGURIDAD

class Producto(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)
    precio=db.Column(db.Integer,nullable=False)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','precio')
producto_schema = ProductoSchema()  #Uno solo (POST,GET)
productos_schema = ProductoSchema(many=True) #Varios (GET)


class Cliente(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    nombre=db.Column(db.String(50),nullable=False)
    direccion=db.Column(db.String(50),nullable=False)
    telefono=db.Column(db.String(50),nullable=False)

    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','direccion', 'telefono')
cliente_schema = ClienteSchema()  #Uno solo (POST,GET)
clientes_schema = ClienteSchema(many=True) #Varios (GET)


class Venta(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    clienteid=db.Column(db.Integer, ForeignKey('cliente.id'))
    productoid=db.Column(db.Integer, ForeignKey('producto.id'))
    cantidad=db.Column(db.Integer,nullable=False)
    fecha=db.Column(db.String(50),nullable=False)

    clienteidFK = relationship(Cliente)
    productoidFK = relationship(Producto)

    def __init__(self, clienteid, productoid, cantidad,fecha):
        self.clienteid = clienteid
        self.productoid = productoid
        self.cantidad = cantidad
        self.fecha = fecha

class VentaSchema(ma.Schema):
    class Meta:
        fields = ('id','clienteid','productoid', 'cantidad', 'fecha')
venta_schema = VentaSchema()  #Uno solo (POST,GET)
ventas_schema = VentaSchema(many=True) #Varios (GET)


class Premio(db.Model):
    id=db.Column(db.Integer, primary_key=True,nullable=False)
    usuarioid=db.Column(db.Integer, ForeignKey('usuario.id'))
    productoid=db.Column(db.Integer, ForeignKey('producto.id'))
    cantidad=db.Column(db.Integer,nullable=False)
    fecha=db.Column(db.String(50),nullable=False)
    premio=db.Column(db.String(50),nullable=False)

    usuarioidFK = relationship(Usuario)
    productoidFK = relationship(Producto)

    def __init__(self, usuarioid, productoid, cantidad,fecha,premio):
        self.usuarioid = usuarioid
        self.productoid = productoid
        self.cantidad = cantidad
        self.fecha = fecha
        self.premio = premio

class PremioSchema(ma.Schema):
    class Meta:
        fields = ('id','usuarioid','productoid', 'cantidad', 'fecha', 'premio')
premio_schema = PremioSchema()  #Uno solo (POST,GET)
premios_schema = PremioSchema(many=True) #Varios (GET)

db.create_all()