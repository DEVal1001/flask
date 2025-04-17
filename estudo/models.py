from estudo import db
from datetime import datetime

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.now)
    nome = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(120), nullable=True) #, unique=True
    assunto = db.Column(db.String(200), nullable=True)
    mensagem = db.Column(db.Text, nullable=True)
    respondido = db.Column(db.Integer, default=0)

    