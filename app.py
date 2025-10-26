from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, User
from forms import UserForm

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Cria tabelas automaticamente (para ambiente de teste)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        novo = User(nome=form.nome.data, email=form.email.data)
        db.session.add(novo)
        db.session.commit()
        flash("Usuário adicionado com sucesso!", "success")
        return redirect(url_for('index'))
    return render_template('add_user.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
