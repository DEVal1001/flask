from estudo import app, db
from flask import render_template, url_for, request
from estudo.models import Contato

@app.route('/')
def homepage():
    usuario = 'Lucas'
    idade = 22
    context = {
        'usuario': usuario,
        'idade': idade,
        
    }
    return render_template('index.html', context=context)

@app.route('/contato/', methods=['GET', 'POST'])
def novapagina():
    context = {}
        
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        print('GET:',pesquisa)
        context.update({'pesquisa': pesquisa})
        
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        assunto = request.form.get('assunto')
        mensagem = request.form.get('mensagem')
        
        contato = Contato(
            nome=nome, 
            email=email, 
            assunto=assunto, 
            mensagem=mensagem
            )
        db.session.add(contato)
        db.session.commit()
        
    return render_template('contato.html', context=context)
