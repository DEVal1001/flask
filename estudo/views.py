from estudo import app, db
from flask import render_template, url_for, request, redirect
from estudo.models import Contato

from flask_login import login_user, logout_user, current_user, login_required
from estudo.forms import ContatoForm, UserForm, LoginForm, PostForm, Post, PostComentarioForm


@app.route('/', methods=['GET', 'POST'])
def homepage():
    usuario = 'Lucas'
    idade = 22
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = form.login()
        login_user(user, remember=True) 
        
        
    context = {
        'usuario': usuario,
        'idade': idade,
    }
    return render_template('index.html', context=context, form=form)

@app.route('/cadastro/', methods=['GET', 'POST'])
def cadastro():
    form = UserForm()
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True) 
        return redirect(url_for('homepage'))   
    return render_template('cadastro.html', form=form)

@app.route('/sair/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/post/novo/', methods=['GET', 'POST'])
@login_required
def postNovo():
    form = PostForm()
    if form.validate_on_submit():
        form.save(current_user.id)
        return redirect(url_for('homepage'))
    return render_template('post_novo.html', form=form)

@app.route('/post/lista/', methods=['GET', 'POST'])
@login_required
def postLista():
    posts = Post.query.all()
    return render_template('post_lista.html', posts=posts)


@app.route('/post/<int:id>/', methods=['GET', 'POST'])
@login_required
def postDetail(id):
    post = Post.query.get(id)
    form = PostComentarioForm()
    if form.validate_on_submit():
        form.save(current_user.id, id)
        return redirect(url_for('postDetail', id=id))
    
    return render_template('post.html', post=post, form=form)


@app.route('/contato/', methods=['GET', 'POST'])
@login_required
def contato():
    form = ContatoForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
        
    return render_template('contato.html', context=context, form=form)

@app.route('/contato/lista/')
@login_required
def contatoLista():
    if current_user.id == 1: return redirect(url_for('homepage'))
        
    
    print(current_user.id)
    
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')
        
    dados = Contato.query.order_by('nome')
    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa)
    context = {'dados': dados.all()}
    
    return render_template('contato_lista.html', context=context)

@app.route('/contato/<int:id>/', methods=['GET'])
@login_required
def contatoDetail(id):
    obj = Contato.query.get(id)

    return render_template('contato_detail.html', obj=obj)
    
# Formato não recomendado, mas para fins de estudo
@app.route('/contato_old/', methods=['GET', 'POST'])
@login_required
def contato_old():
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
        
    return render_template('contato_old.html', context=context)
