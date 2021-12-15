from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/connection", methods=["POST"])
def connection():
    data = json.loads(request.get_data())
    etudiant = i.connection(data['email'], data['password'])
    if(etudiant['id'] < 1):
        return json.dumps(etudiant), 404
    return json.dumps(etudiant), 200


@app.route("/api/register", methods=["POST"])
def register():
    try:
        data = json.loads(request.get_data())
        student = i.register(data['email'], data['username'], data['password'])
        if("err" in student.keys()):
            return json.dumps(student), 404
        return json.dumps(student), 201
    except Exception as err:
        return {"err": err}


@app.route("/api/checkEmail", methods=["POST"])
def check_email():
    data = json.loads(request.get_data())
    student = i.check_email(data['email'])
    if student['id'] < 1:
        return json.dumps(student), 404
    return json.dumps(student), 200




@app.route("/api/forum/<categorie_>", methods=["GET", "POST"])
def publications(categorie_):
    if request.method == "POST":
        data = json.loads(request.get_data())
        res = i.ajout_publication(
            data['auteur'], data['categorie'], data['contenu'])
        return json.dumps({"id": res.id, "auteur": res.auteur,
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


@app.route("/api/etudiant/<email_etudiant>")
def etudiant(email_etudiant):
    student = i.retourner_cours_de(email_etudiant)
    return server_response(student)


@app.route("/api/cours/<sigle>")
def cours(sigle):
    cours = i.retourner_etudiants_de(sigle)
    return server_response(cours)


# @app.route("/api/listEtudiant/<sigle_>", methods=["GET"])
# def etudiants(sigle_):
#    list = i.list_etudiants( sigle_ )
#    return json.dumps(list)


def server_response(data, status=200, header={"Content-Type": "application/json"}):
    return Response(json.dumps(data), status, header)


# LOL python is weird..
import Interation as i
