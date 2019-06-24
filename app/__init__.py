# -*- coding: utf-8 -*-

from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
#from flask_cors import cross_origin # Por el momento no usamos CORS
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import json
from datetime import datetime
from sqlalchemy import or_

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.models import *

@app.route('/')
def start_here():
    return 'App iniciada'

@app.route('/canciones')
def listar_canciones():
    termino_busqueda = request.args.get('t')
    if termino_busqueda is not None:
        return jsonify({'canciones': buscar_canciones(termino_busqueda)})

    canciones = PostCancion.query.\
                filter(PostCancion.fecha_publicacion <= datetime.today()).\
                order_by(PostCancion.fecha_publicacion.desc()).all()
    return jsonify([cancion.serialize() for cancion in canciones])

def buscar_canciones(termino):
    canciones = PostCancion.query.\
                filter(or_(PostCancion.titulo.ilike('%'+termino+'%'), PostCancion.artista.ilike('%'+termino+'%'))).\
                order_by(PostCancion.fecha_publicacion.desc()).all()[:10]
    return [cancion.serialize_short() for cancion in canciones]

@app.route('/listado_canciones')
def listar_canciones_2():
    canciones = PostCancion.query.\
            order_by(PostCancion.fecha_publicacion.desc()).all()[:10]
    return jsonify({'canciones': [cancion.serialize_min() for cancion in canciones]})

@app.route('/canciones/<int:id_cancion>')
def obtener_cancion(id_cancion):
    cancion = PostCancion.query.get(id_cancion)
    return jsonify(cancion.serialize_short())

# admin
class AuthView(ModelView):
    def _handle_view(self, name, **kwargs):
        auth = request.authorization
        if not auth or not \
                (auth.username == 'ricardo' and auth.password == 'ruedasdelpasado'):
            return Response('identifíquese',
                            401,
                            {'WWW-Authenticate': 'Basic fb=fbchallenge'})

class PostCancionView(AuthView):
    column_exclude_list = ['texto']

admin = Admin(app, name="Friday Songbird", template_mode='bootstrap3')
admin.add_view(PostCancionView(PostCancion, db.session))
