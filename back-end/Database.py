from server import db
from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Base = declarative_base()



class Inscription(db.Model):
    __tablename__= 'inscription'
    etudiant_id = Column(ForeignKey('etudiant_.id'), primary_key=True)
    sigle_id = Column(ForeignKey('sigle_.id'), primary_key=True)

    postMaybe = Column(db.String(200))

    sigle = relationship('Sigle', backref=('etudiant_inscription'))
    etudiant = relationship('Etudiant',  backref=('sigle_inscription'))


# Sigle cours
class Sigle(db.Model):
    __tablename__ = 'sigle_'
    id = db.Column(db.Integer , primary_key = True)
    sigle = db.Column(db.String(7))

# Etudiant
class Etudiant(db.Model):
    __tablename__ = 'etudiant_'
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
#    cours = relationship('Inscription')


    # Permet de sortir en string des éléments de l'objets passé en parametre
def __repr__(self):
    return 'Username  %r' % self.username + '\n Email %r' % self.email


db.create_all()


# Print passe la liste passé en paramêtre dans une boucle qui affiche le contenu avec repr
def print_etudiant(Etudiants):
    for Etudiant in Etudiants :
       print( __repr__(Etudiant))

def print_inscription(etudiant):
    for  assoc in etudiant.cours :
        print( assoc.sigle )
