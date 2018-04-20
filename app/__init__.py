# -*- coding: utf-8 -*-

from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
#from flask_cors import cross_origin # Por el momento no usamos CORS
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import json
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.models import *

@app.route('/')
def start_here():
    return 'App iniciada'

@app.route('/canciones')
def listar_canciones():
    canciones = PostCancion.query.order_by(PostCancion.fecha_publicacion.desc()).all()
    return jsonify([cancion.serialize() for cancion in canciones])

# admin
class AuthView(ModelView):
    def _handle_view(self, name, **kwargs):
        auth = request.authorization
        if not auth or not \
                (auth.username == 'ricardo' and auth.password == 'ruedasdelpasado'):
            return Response('identifíquese',
                            401,
                            {'WWW-Authenticate': 'Basic fb=fbchallenge'})

admin = Admin(app, name="Friday Songbird", template_mode='bootstrap3')
admin.add_view(AuthView(PostCancion, db.session))
