from server import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


# Base = declarative_base() # Not necessary yet , might use later dont remove

# Etudiant
class Etudiant(db.Model):
    __tablename__ = 'etudiant'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    publications = relationship("Publication")

    def __repr__(self):
        return "Id: %d\nUsername: %r\nEmail: %r" % (self.id, self.username, self.username)

# Publication


class Publication(db.Model):
    __tablename__ = 'publication'
    id = db.Column(db.Integer, primary_key=True)
    idEtudiant = db.Column(db.Integer, ForeignKey('etudiant.id'))
#    auteur = relationship("Etudiant", back_populates="publications")
    # idParentPost
    contenu = db.Column(db.String(200))


# Cours
class Cours(db.Model):
    __tablename__ = 'cours'
    id = db.Column(db.Integer, primary_key=True)
    sigle = db.Column(db.String(7))
    session = db.Column(db.String(4))  # AU20 -> automne 2020


# TODO pas fonctionnel encore
class Inscription(db.Model):
    __tablename__ = 'inscription'
    db.Column("etudiant_id", db.Integer, ForeignKey('etudiant.id'), primary_key=True)
    db.Column("sigle_id", db.Integer, ForeignKey('cours.id'), primary_key=True)

