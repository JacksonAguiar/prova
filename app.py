from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy import Select,insert
from flask import Flask, render_template, request,url_for, redirect



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy()
db.app = app
db.init_app(app)

app.app_context().push()

class Game(db.Model):
    __tablename__ = "game"
     
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    plataforma = db.Column(db.String(15))
    preco = db.Column(db.String(15))
    quantidade = db.Column(db.Integer)


@app.route("/")
def index():
    db.session.execute(
    insert(Game),
    [
        {"nome": "DEAD SPACE REMAKE", "plataforma": "PS5","preco":"R$350,00", "quantidade": 10},
        {"nome": "FORSPOKEN", "plataforma": "PS5","preco":"R$350,00", "quantidade": 8},
        {"nome": "DEAD ISLAND 2", "plataforma": "PS5","preco":"R$350,00", "quantidade": 10},
        {"nome": "HOGWARTS LEGACY", "plataforma": "PS5","preco":"R$350,00", "quantidade": 7},
        {"nome": "WILD HEARTS", "plataforma": "PS5","preco":"R$350,00", "quantidade": 7},
        {"nome": "RESIDENT EVIL 4", "plataforma": "PS5","preco":"R$350,00", "quantidade": 10},
        {"nome": "THE LEGEND OF ZELDA: TEARS OF THE KINGDOM", "plataforma": "PS5","preco":"R$350,00", "quantidade": 10},
      
    ],)
    games =  Game.query.all()
    return render_template("index.html", games = games)

@app.route("/save", methods=['POST'])
def save():
    _nome = request.form["nome"]
    _plataforma = request.form["plataforma"]
    _preco = "R$"+ request.form["preco"]
    _quantidade = request.form["quantidade"]

    game = Game(nome = _nome, plataforma = _plataforma, preco=_preco, quantidade=_quantidade)
    
    db.session.add(game)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)