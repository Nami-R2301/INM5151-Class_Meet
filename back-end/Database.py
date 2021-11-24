from server import db
from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


# Base = declarative_base() # Not necessary yet , might use later dont remove

# Etudiant
class Etudiant(db.Model):
    __tablename__ = 'etudiant'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    publications = relationship("Publication")

    
    def ajout_etudiant(self, username_, psw_, email_):
        n = self(username=username_, password=psw_, email=email_)
        self.db.session.add(n)
        self.db.session.commit()

    def __repr__(self):
        return "Username: %r\nEmail: %r" % (self.username, self.username)

# Publication


class Publication(db.Model):
    __tablename__ = 'publication'
    id = db.Column(db.Integer, primary_key=True)
    idEtudiant = db.Column(db.Integer, ForeignKey('etudiant.id'))
#    auteur = relationship("Etudiant", back_populates="publications")
    # idParentPost
    contenu = db.Column(db.String(200))


# Sigle cours
class Sigle(db.Model):
    __tablename__ = 'sigle'
    id = db.Column(db.Integer, primary_key=True)
    sigle = db.Column(db.String(7))

# Permet de sortir en string des éléments de l'obnjet passé en parametre s'il possède l'attribut username et email , modifiable


def __repr__(self):
    return 'Username  %r' % self.username + '\n Email %r' % self.email


# TODO pas fonctionnel encore
class Inscription(db.Model):
    __tablename__ = 'inscription'
    etudiant_id = Column(ForeignKey('etudiant.id'), primary_key=True)
    sigle_id = Column(ForeignKey('sigle.id'), primary_key=True)

    postMaybe = Column(db.String(200))

    sigle = relationship('Sigle', backref=('etudiant_inscription'))
    etudiant = relationship('Etudiant',  backref=('sigle_inscription'))


# Print passe la liste passé en paramêtre dans une boucle qui affiche le contenu avec repr
def print_etudiant(Etudiants):
    for Etudiant in Etudiants:
        print(__repr__(Etudiant))

# pas fonctionnel encore


def print_inscription(etudiant):
    for assoc in etudiant.cours:
        print(assoc.sigle)
