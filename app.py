from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:password123@127.0.0.1:5432/trello'

db = SQLAlchemy(app)

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    status = db.Column(db.String)
    priority = db.Column(db.String)


@app.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@app.cli.command('drop')
def drop_db():
    db.drop_all()
    print('Tables dropped')

@app.cli.command('seed')
def seed_db():
    card = Card(
        title = 'start project',
        description = 'stage 1 create db',
        status = 'todo',
        priority = 'High',
        date = date.today()
    )

    db.session.add(card)
    db.session.commit()
    print("table seeded")

@app.route('/')
def index():
    return 'hello'