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


# @app.route("/api/connection", methods=["POST"])
# def connection():
#    data = json.loads(request.get_data())
#    print(data)
#    return data
#

@app.route("/api/forum/<categorie_>", methods=["GET", "POST"])
def publications(categorie_):
    if request.method == "POST":
        data = json.loads(request.get_data())
        res = i.ajout_publication(
            data['auteur'], data['categorie'], data['contenu'])
        return json.dumps({"id": res.id,"auteur": res.auteur,
                           "sous_categorie": res.sous_categorie, "date": str(res.date),
                           "contenu": res.contenu}), 201

    elif request.method == "GET":
        list = i.list_publication(categorie_)
        return json.dumps(list, default=str), 200

    else:
        return "", 404


@app.route("/api/etudiants", methods=["GET"])
def etudiants():
    list = i.list_etudiants()
    return json.dumps(list, default=str)

# @app.route("/api/listEtudiant/<sigle_>", methods=["GET"])
# def etudiants(sigle_):
#    list = i.list_etudiants( sigle_ )
#    return json.dumps(list)


# LOL python is weird..
import Interation as i
