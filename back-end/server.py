import Interation as i
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


#@app.route("/api/connection", methods=["POST"])
#def connection():
#    data = json.loads(request.get_data())
#    print(data)
#    return data
#
# comment j'imagine qu'il faudrait appeler la méthode pour envoyer les posts
@app.route("/api/forum", methods=["POST"])
def publications():
    categorie_ = json.loads(request.get_data())
    return i.list_publication( categorie_ ) 
