from server import db
from sqlalchemy import DateTime

# Association étudiant - cours
Inscription = db.Table(
    "Inscription",
    db.Column("etudiantId", db.Integer, db.ForeignKey("etudiant.etudiantId")),
    db.Column("coursId", db.Integer, db.ForeignKey("cours.coursId")),
)


# Etudiant
class Etudiant(db.Model):
    etudiantId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    listeCours = db.relationship(
        "Cours",
        secondary=Inscription,
        backref=db.backref("listeEtudiants", lazy="dynamic"),
    )

    def __repr__(self):
        return "Id: %d\nUsername: %r\nEmail: %r" % (
            self.id,
            self.username,
            self.username,
        )


# Cours
class Cours(db.Model):
    coursId = db.Column(db.Integer, primary_key=True)
    sigle = db.Column(db.String(7))
    session = db.Column(db.String(4))  # AU20 -> automne 2020


# Publication
class Publication(db.Model):
    __tablename__ = "Publication"
    id = db.Column(db.Integer, primary_key=True)
    auteur = db.Column(db.String(80))
    contenu = db.Column(db.String(200))
    sous_categorie = db.Column(db.String(20))  # mettre un sigle
    date = db.Column(DateTime)

    def __repr__(self):
        return "id: %r\nauteur: %r\nsous_categorie: %r\ndate: %r\ncontenu: %r\n" % (
            self.id,
            self.auteur,
            self.sous_categorie,
            self.date,
            self.contenu,
        )
