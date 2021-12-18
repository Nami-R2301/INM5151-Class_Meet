import re
from datetime import datetime
import Database
import secrets
import hashlib


regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
#######################################################################
# Méthode que l'on doit utiliser/appeler pour le moment
class Objet_publication:
    def __init__(self, auteur_, contenu_, date_):
        self.date = date_
        self.auteur = auteur_
        self.contenu = contenu_


def retourne_Publication(Publication_):
    return Objet_publication(
        auteur_=Publication_.auteur,
        contenu_=Publication_.contenu,
        date_=Publication_.date,
    )


def list_publication(sous_categorie_):
    posts = Database.Publication.query.filter_by(sous_categorie=sous_categorie_).all()
    list = []
    if ( len(posts) == 0 or posts == None ):
        msgBienvenue = Database.Publication (
        contenu= ("Bienvenue sur la page de forum pour le cours " + sous_categorie_ + ", veuillez garder le respect dans vos propos, ClassMeet est une plateforme d'entraide avant tout, et sur ce, bon clavardage."),
        auteur= "Forum_Master",
        sous_categorie=sous_categorie_,
        date=datetime.now().replace(microsecond=0),
                )
        Database.db.session.add(msgBienvenue)
        Database.db.session.commit()
        posts = Database.Publication.query.filter_by(sous_categorie=sous_categorie_).all()
    
    for Publication in posts:
        list.append(
            {
                "auteur": retourne_Publication(Publication).auteur,
                "contenu": retourne_Publication(Publication).contenu,
                "dateTime": retourne_Publication(Publication).date,
            }
        )
    return list


def list_etudiants():
    etudiants = Database.Etudiant.query.all()
    list = []
    for Etudiant in etudiants:
        list.append({"etudiant": Etudiant.username})
    return list


def retourner_cours_de(email_):
    etudiant = Database.Etudiant.query.filter_by(email=email_).first()
    if etudiant is None:
        print("Étudiant avec " + email_ + " non inscris!")
        return
    print("Cours de l'étudiant " + etudiant.username)
    list = []
    for Database.Cours in etudiant.listeCours:
        list.append(Database.Cours.sigle)
    return list


def retourner_etudiants_de(sigle_):
    print("Etudiants inscris à " + sigle_)
    cours = Database.Cours.query.filter_by(sigle=sigle_).first()
    if cours is None:
        print("Cours " + sigle_ + " non éxistant!")
        return
    cours.listeEtudiants
    list = []
    for etudiant in cours.listeEtudiants:
        list.append(etudiant.username)
    return list


def afficher_cours_de(email_):
    etudiant = Database.Etudiant.query.filter_by(email=email_).first()
    if etudiant is None:
        print("Étudiant avec " + email_ + " non inscris!")
        return
    print("Cours de l'étudiant " + etudiant.username)
    for Database.Cours in etudiant.listeCours:
        print(Database.Cours.sigle)


def afficher_etudiants_de(sigle_):
    cours = Database.Cours.query.filter_by(sigle=sigle_).first()
    if cours is None:
        print("Cours " + sigle_ + " non éxistant!")
        return
    print("Etudiants inscris à " + sigle_)
    cours.listeEtudiants
    for etudiant in cours.listeEtudiants:
        print(__repr_etudiant__(etudiant))


def ajout_inscription(email_, sigle_):
    cours = Database.Cours.query.filter_by(sigle=sigle_).first()
    if cours is None:
        print("Cours " + sigle_ + " non disponible!")
        return
    etudiant = Database.Etudiant.query.filter_by(email=email_).first()
    nbr = 0
    for Database.Cours in etudiant.listeCours:
        nbr += 1
    if nbr < 5:
        cours.listeEtudiants.append(etudiant)
        Database.db.session.commit()
    else:
        print("Maximum de cours atteint!")


def ajout_cours(sigle_, session_):
    nouveau_cours = Database.Cours(sigle=sigle_, session=session_)
    Database.db.session.add(nouveau_cours)
    Database.db.session.commit()


def ajout_utilisateur(username_, email_, psw_, salt_):
    if email_valide(email_):
        n = Database.Etudiant(username=username_, email=email_, password=psw_, salt=salt_)
        Database.db.session.add(n)
        Database.db.session.commit()
    else:
        print("Email " + email_ + " invalide!")


def ajout_publication(username_, sigle_, contenu_):
        
    n = Database.Publication(
        contenu=contenu_,
        auteur=username_,
        sous_categorie=sigle_,
        date=datetime.now().replace(microsecond=0),
    )
    Database.db.session.add(n)
    Database.db.session.commit()
    return n


def supprimer_publications_de(sigle_):
    publications = Database.Publication.query.filter_by(sous_categorie=sigle_)
    publications.delete(synchronize_session=False)
    Database.db.session.commit()


def connection(email, password):
    try:
        etudiant = Database.Etudiant.query.filter_by(
            email=email, password=password
        ).first()
        return {
            "id": etudiant.etudiantId,
            "username": etudiant.username,
            "email": etudiant.email,
        }
    except AttributeError as err:
        return {"id": 0, "err": "Incorrect email or password"}
    except Exception as err:
        print(err)
        return {"id": 0, "err": err}


def email_valide(email_):
    if re.fullmatch(regex, email_):
        return True
    else:
        return False


def register(email, username, password):
    try:
        if not email_valide(email):
            raise Exception("email not valid")
        salt = secrets.token_hex(16)
        hash_password = hashlib.sha512((password + salt).encode("utf-8")).hexdigest()
        res = Database.Etudiant(email=email, username=username, password=hash_password, salt=salt)
        Database.db.session.add(res)
        Database.db.session.commit()
        return {"username": username, "email": email}
    except Exception as err:
        if "UNIQUE constraint failed" in err.args[0]:
            return {"err": "Email already exists"}
        else:
            return {"err": err}


def check_email(email):
    try:
        match = Database.Etudiant.query.filter_by(email=email).first()
        return {"email": match.email}
    except AttributeError as err:
        return {"err": "Incorrect email or password"}
    except Exception as err:
        return {"err": err}


        
#####################################################################################


def __repr_etudiant__(self):
    return "Username  %r" % self.username + "\n Email %r" % self.email


def __repr_post__(self):
    return "%r\n%r\n%r" % (self.date, self.contenu, self.auteur)


# Print passe la liste passé en paramêtre dans une boucle qui affiche le contenu avec repr
def print_etudiant(Etudiants):
    for Etudiant in Etudiants:
        print(__repr_etudiant__(Etudiant))


# pas fonctionnel encore


def afficher_publications(sous_categorie_):
    posts = Database.Publication.query.filter_by(sous_categorie=sous_categorie_).all()
    for Publication in posts:
        print(__repr_post__(Publication))
