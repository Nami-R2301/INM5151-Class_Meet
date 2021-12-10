from datetime import datetime
from sqlalchemy.sql.functions import user
import Database
import sqlite3

#######################################################################
# Méthode que l'on doit utiliser/appeler pour le moment
class Objet_publication():
    def __init__ ( self , auteur_, contenu_, date_  ):
        self.date = date_
        self.auteur = auteur_
        self.contenu = contenu_

def retourne_Publication( Publication_ ):
    return  Objet_publication( auteur_=Publication_.auteur , contenu_=Publication_.contenu, date_= Publication_.date)

def list_publication( sous_categorie_ ):
     posts= Database.Publication.query.filter_by(sous_categorie=sous_categorie_).all()
     list = []
     for Publication in posts:
         list.append({"auteur":retourne_Publication( Publication ).auteur, "contenu":retourne_Publication(Publication).contenu, "dateTime":retourne_Publication(Publication).date})
     return list

def list_etudiants():
     etudiants= Database.Etudiant.query.all()
     list = []
     for Etudiant in etudiants:
         list.append( { "etudiant":Etudiant.username })
     return list

#def list_etudiants( sous_categorie_ ):
#     posts= Database.Etudiant.query.filter_by(sous_categorie=sous_categorie_).all()
#     list = []
#     for Publication in posts:
#         list.append({"auteur":retourne_Publication( Publication ).auteur, "contenu":retourne_Publication(Publication).contenu})
#     return list


def ajout_utilisateur( username_, psw_, email_ ):
   n = Database.Etudiant( username=username_, password=psw_, email=email_)
   Database.db.session.add(n)
   Database.db.session.commit()

def ajout_publication(username_, sigle_,  contenu_  ):
    n = Database.Publication( contenu=contenu_, auteur=username_ , sous_categorie=sigle_ )
    Database.db.session.add(n)
    Database.db.session.commit()
    return n

def connection(email, password):
    try:
        etudiant = Database.Etudiant.query.filter_by(email=email, password=password).first()
        return {"id": etudiant.id, "username": etudiant.username, "email": etudiant.email}
    except AttributeError as err:
        return {"id": 0, "err": "Incorrect email or password"}
    except Exception as err:
        print(err)
        return {"id": 0, "err": err}

def register(email, username, password):
    try:
        res = Database.Etudiant(email=email, username=username, password=password)
        Database.db.session.add(res)
        Database.db.session.commit()
        return {"username": username, "email": email}
    except Exception as err:
        if "UNIQUE constraint failed" in err.args[0]:
            return {"err": "Email already exists"}
        else:
            return {"err": err}
        
#####################################################################################


def __repr_etudiant__(self):
    return 'Username  %r' % self.username + '\n Email %r' % self.email


def __repr_post__(self):
    return '%r\n%r\n%r' % (self.date , self.contenu, self.auteur)

# Print passe la liste passé en paramêtre dans une boucle qui affiche le contenu avec repr
def print_etudiant(Etudiants):
    for Etudiant in Etudiants :
       print( __repr_etudiant__(Etudiant))

# pas fonctionnel encore
def print_inscription(etudiant):
    for  assoc in etudiant.cours :
        print( assoc.sigle )

def print_publications( sous_categorie_ ):
     posts= Database.Publication.query.filter_by(sous_categorie=sous_categorie_).all()
     for Publication in posts:
         print(__repr_post__( Publication))


