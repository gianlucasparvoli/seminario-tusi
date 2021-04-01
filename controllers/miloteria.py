from flask import Flask, request, jsonify,render_template
from flask.views import MethodView
from database import *
from sqlalchemy.sql import select

class MyLotteryEndPoint(MethodView):
    def get(self):
        return render_template("mi-loteria.html")
    
    def post(self):
        nombre = request.form['NombreLoteriaNuevo']
        cbu = request.form['CBUNuevo']
        alias = request.form['AliasCBUNuevo']
        tipoCuenta = request.form['TipoCuentaNuevo']
        banco = request.form['BancoNuevo']
        saldo = request.form['SaldoNuevo']

        lot = MiLoteria.query.get(1)
        lot.nombre= nombre
        lot.cbu= cbu
        lot.aliasCbu= alias
        lot.tipoCuenta= tipoCuenta
        lot.banco= banco
        lot.saldoActual= saldo

        db.session.commit()
        db.session.close()
        
        # flash("Alta de cliente '" + nombre + "' correcta")
        return render_template('mi-loteria.html')


class MyLotteryFindOneEndPoint(MethodView):
    def get(self, id):
        lot = MiLoteria.query.filter_by(id=id).all()
        s = MisLoterias_schema.dump(lot)
        return jsonify(s)

class MyLotteryMovementEndPoint(MethodView):
    def post(self):
        valor = request.form['valor']
        fecha = request.form['fecha']
        comentario = request.form['comentario']

        newMovementLottery= MiLoteriaMovimientos(valor,fecha,comentario)
        db.session.add(newMovementLottery)
        db.session.commit()

        lot = MiLoteria.query.get(1)
        lot.saldoActual= int(lot.saldoActual) + int(valor)

        db.session.commit()
                
        db.session.close()
        
        # flash("Alta de cliente '" + nombre + "' correcta")
        return render_template('mi-loteria.html')