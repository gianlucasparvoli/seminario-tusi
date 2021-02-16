from flask import Flask, request, jsonify,render_template, flash
from flask.views import MethodView
from database import *
from sqlalchemy.sql import select
import smtplib
from email.mime.text import MIMEText
import random
import string

class UsersSigInEndPoint(MethodView):
    def get(self):
        # all_users = select([usuario])
        # result = users_schema.dump(all_users)
        # return jsonify(result)
        return render_template('registrer.html')
        
    # def post(self):
    #     usuario = request.json['usuario']
    #     apellido = request.json['apellido']
    #     nombre = request.json['nombre']
    #     mail = request.json['mail']
    #     new_user= User(nom, direc)
    #     db.session.add(new_user)
    #     db.session.commit()
    #     return user_schema.jsonify(new_user)

class UsersLogInEndPoint(MethodView):
    def get(self):
        # all_users = select([usuario])
        # result = users_schema.dump(all_users)
        # return jsonify(result)
        return render_template('login.html')
    def post(self):
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        user = Usuario.query.filter_by(usuario=usuario).all()     
        usuarioIngresado = usuarios_schema.dump(user)

        for x in usuarioIngresado:
            claveusuario=(x["clave"])
            idusuario=x["id"]
        
        if user and check_password_hash(claveusuario, contrasena):
            return render_template('login.html',value=idusuario)
            
        flash("Usuario y/o Contraseña Incorrectas")
        return render_template('login.html')

class UsersGestionEndPoint(MethodView):
    def get(self,id):
        # all_users = select([usuario])
        # result = users_schema.dump(all_users)
        # return jsonify(result)
        return render_template('gestion.html',value=id)
    

class UserEndPoint(MethodView):   
    def get(self, id):
        user = Usuario.query.get(id)
        return usuario_schema.jsonify(user)

    def delete(self, id):
        user = Usuario.query.get(id)
        db.session.delete(user)
        db.session.commit()
        #ELIMINACION DE VALORES DE Grupos_Usuario
        gruposUser = Grupos_Usuario.query.filter_by(usuarioid=id).all()     
        gruposUserDump = grupos_usuarios_schema.dump(gruposUser)
        for x in gruposUserDump:
            gu = Grupos_Usuario.query.get(x["id"])
            db.session.delete(gu)
            db.session.commit()

        return jsonify("OK")


class UsersEndPoint(MethodView):   
    def get(self):
        user = Usuario.query.all()
        return usuarios_schema.jsonify(user)

    def post(self):
        usuario = request.form['Usuario']
        apellido = request.form['Apellido']
        nombre = request.form['Nombre']
        mail = request.form['Email']
        estado = request.form.get('Estado')
        if estado is None:
            estado = 2 # estado = Descativado
        else:
            estado = 1 # estado = Acctivado

        def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

        clave = id_generator()

        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login("seminario.tusi@gmail.com","pabloaudoglio")
        msg = MIMEText(u'<h3> Alta de Usuario - Seminario</h3><br></br><a> Usuario: '+usuario+'</a><br></br><a> Clave: '+clave+'</a>','html')
        server.sendmail("seminario.tusi@gmail.com",mail,msg.as_string())
        server.quit()
        
        claveHash = generate_password_hash(clave,method='sha256')
        new_user= Usuario(nombre,apellido,mail,usuario,claveHash,estado)
        db.session.add(new_user)
        db.session.commit()
        
        user = Usuario.query.filter_by(usuario=usuario).all()     
        usuarioIngresado = usuarios_schema.dump(user)
        for x in usuarioIngresado:
            idusuario=x["id"]
            
        all_group = Grupo.query.all()
        
        allgrupos = grupos_schema.dump(all_group)
        for x in allgrupos:
            estado = request.form.get('grupo'+str(x["id"]))
            if estado is None:
                print(estado)
            else:
                new_gruposusuario= Grupos_Usuario(idusuario,estado)
                db.session.add(new_gruposusuario)
                db.session.commit()
                
        db.session.close()
        
        flash("Alta de usuario '" + usuario + "' correcta")
        return render_template('registrer.html')


class UsersMenuEndPoint(MethodView):   
    def get(self,id):
        # user = Usuario.query.get(id)
        # usuariojson = usuario_schema.dump(user)
        # print(usuariojson['id'])
        return render_template('navbar-logueado.html',value=id)

class UsersModifEndPoint(MethodView): 
    def post(self,id):

        usuario = request.form['Usuario']
        user = Usuario.query.filter_by(usuario=usuario).all()     
        usuarioIngresado = usuarios_schema.dump(user)
        for x in usuarioIngresado:
            idusuario=x["id"]

        
        #MOFICIACION DE VALORES DE USUARIO
        user = Usuario.query.get(idusuario)

        apellido = request.form['Apellido']
        nombre = request.form['Nombre']
        mail = request.form['Email']
        estado = request.form.get('Estado')

        user.apellido=apellido
        user.nombre=nombre
        user.mail=mail
        user.estado=estado

        #ELIMINACION DE VALORES DE Grupos_Usuario
        gruposUser = Grupos_Usuario.query.filter_by(usuarioid=idusuario).all()     
        gruposUserDump = grupos_usuarios_schema.dump(gruposUser)
        for x in gruposUserDump:
            gu = Grupos_Usuario.query.get(x["id"])
            db.session.delete(gu)
            db.session.commit()

        #ALTA DE VALORES DE Grupos_Usuario

        all_group = Grupo.query.all()
        
        allgrupos = grupos_schema.dump(all_group)
        for x in allgrupos:
            estado = request.form.get('grup'+str(x["id"]))
            if estado is None:
                print(estado)
            else:
                new_gruposusuario= Grupos_Usuario(idusuario,estado)
                db.session.add(new_gruposusuario)
                db.session.commit()


        db.session.commit()
        flash("Modificacion de usuario '" + usuario + "' correcta")
        return render_template('gestion.html',value=id)



class UsersCambiarClaveEndPoint(MethodView): 
    def get(self, id):
        user = Usuario.query.get(id)
        return render_template('cambiar-clave.html',value=id)

    def post(self, id):
        print(id)
        user = Usuario.query.get(id)
        usuario = usuario_schema.dump(user)
        claveDB = usuario["clave"]
        contrasena = request.form['ClaveActual']
        if usuario and check_password_hash(claveDB, contrasena):
            nuevaclave = request.form['Clave']
            nuevaclaverepetida = request.form['ClaveRepetida']
            if nuevaclave == nuevaclaverepetida:
                claveHash = generate_password_hash(nuevaclave,method='sha256')
                user.clave=claveHash
                db.session.commit()
                flash("Cambio de Clave correcto")
                return render_template('cambiar-clave.html',value=id)
        flash("Error en alguno de los datos ingresados")
        return render_template('cambiar-clave.html',value=id)

class UsersResetearClaveEndPoint(MethodView): 
    def get(self, id, idAdmin):
        
        user = Usuario.query.get(id)
        usuario = usuario_schema.dump(user)
        mail = usuario["mail"]
        username=usuario["usuario"]

        def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

        clave = id_generator()

        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login("seminario.tusi@gmail.com","pabloaudoglio")
        msg = MIMEText(u'<h3> Reseteo de Clave - Seminario</h3><br></br><a> Usuario: '+username+'</a><br></br><a> Clave: '+clave+'</a>','html')
        server.sendmail("seminario.tusi@gmail.com",mail,msg.as_string())
        server.quit()

        claveHash = generate_password_hash(clave,method='sha256')
        user.clave=claveHash
        db.session.commit()
        flash("Reseteo de Clave de Usuario " + username + "exitoso")

        return render_template('gestion.html',value=idAdmin)