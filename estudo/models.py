from estudo import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=True)
    sobrenome = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    senha = db.Column(db.String(50), nullable=True)
    posts = db.relationship('Post', backref='user', lazy=True)
    post_comentarios = db.relationship('PostComentarios', backref='user', lazy=True)

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.now)
    nome = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(120), nullable=True) #, unique=True
    assunto = db.Column(db.String(200), nullable=True)
    mensagem = db.Column(db.Text, nullable=True)
    respondido = db.Column(db.Integer, default=0)
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.now)
    mensagem = db.Column(db.String, nullable=True)
    imagem = db.Column(db.String, nullable=True, default='img_default.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    comentarios = db.relationship('PostComentarios', backref='post', lazy=True)
    
    def msg_resumo(self):
        return f"{self.mensagem[:30]} ..."
    
class PostComentarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.now)
    comentario = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=True)