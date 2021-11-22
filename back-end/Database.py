from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy( app )

class etudiant(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)


def __repr__(self):
    return '<etudiant %r %r>' % self.username % self.email

db.create_all()


### SQLAlchemy define a constructor already
#def __init__(self, username, email):
#    self.username = username
#    self.email = email


#@app.route('/')
