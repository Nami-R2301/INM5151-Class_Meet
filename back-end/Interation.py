from datetime import datetime 
import Database

class Objet_publication():
    def __init__ ( self , auteur_, contenu_,  ):
#        self.date = date_
        self.auteur = auteur_
        self.contenu = contenu_

def __repr_etudiant__(self):
    return 'Username  %r' % self.username + '\n Email %r' % self.email


def __repr_post__(self):
    return '%r' % self.contenu  


def ajout_utilisateur( username_, psw_, email_ ):
   n = Database.Etudiant( username=username_, password=psw_, email=email_) 
   Database.db.session.add(n)
   Database.db.session.commit()

def ajout_publication(username_, sigle_,  contenu_  ):
    n = Database.Publication( contenu=contenu_, auteur=username_ , sous_categorie=sigle_ )
    Database.db.session.add(n)
    Database.db.session.commit()

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

def retourne_Publication( Publication_ ):
    return  Objet_publication( auteur_=Publication_.auteur , contenu_=Publication_.contenu )


def list_publication( sous_categorie_ ):
     posts= Database.Publication.query.filter_by(sous_categorie=sous_categorie_).all()
     list = []
     for Publication in posts:
        list.append(retourne_Publication( Publication ))
     return list     


# Permet de sortir en string des éléments de l'obnjet passé en parametre s'il possède l'attribut username et email , modifiable
