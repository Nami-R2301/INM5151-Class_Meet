# TODO    Install sqlalchemy for DB with flask with command 'pip install flask-sqlalchemy' or 'pip3 install flask-sqlalchemy'
from flask_sqlalchemy import SQLAlchemy 
from flask import Flask
# juste pour tester , app devrait être isinstancier ailleurs par la suite.
# 
app = Flask(__name__)
db = SQLAlchemy( app )

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://etudiantUqam.sqlite3'

class etudiants(db.Model):
    id = db.Column(db.Integer , primary_key = true)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)

def _init_(self, username, email):
    self.username = username
    self.email = email
#Inserts records into a mapping table
#db.session.add (model object)
#delete records from a table
#db.session.delete (model object)
#retrieves all records (corresponding to SELECT queries) from the table.
#model.query.all ()



db.create_all()

@app.route('/')
def show_all():
   return render_template('show_all.html', etudiants = etudiants.query.all() )
