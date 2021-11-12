# TODO    Install sqlalchemy for DB with flask with command 'pip install flask-sqlalchemy' or 'pip3 install flask-sqlalchemy'
from flask_sqlalchemy import SQLAlchemy 
from flask import Flask
# juste pour tester , app devrait être isinstancier ailleurs par la suite.
# 
app = Flask(__name__)
db = SQLAlchemy( app )

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://etudiant.sqlite3'

class etudiant(db.Model):
   _email = db.Column("email", db.str)



