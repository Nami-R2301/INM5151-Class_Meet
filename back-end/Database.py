from server import db
from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Base = declarative_base()

# Forum associative table
inscription = Table('association', db.Model.metadata, 
    Column('left_id', ForeignKey('left_id')),
    Column('right_id', ForeignKey('right_id'))
        )

# Sigle cours
class Sigle(db.Model):
    __tablename__ = 'right'
    id = db.Column(db.Integer , primary_key = True)
    sigle = db.Column(db.String(7))
    eutdiants_inscrits = relationship("Etudiant", secondary=inscription)

# Etudiant
class Etudiant(db.Model):
    __tablename__ = 'left'
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)


    # Permet de sortir en string des éléments de l'objets passé en parametre
def __repr__(self):
    return 'Username  %r' % self.username + '\n Email %r' % self.email














db.create_all()

# Print passe la liste passé en paramêtre dans une boucle qui affiche le contenu avec repr
def print_etudiant(Etudiants):
    for Etudiant in Etudiants :
       print( __repr__(Etudiant))
