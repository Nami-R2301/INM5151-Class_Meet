from server import db

# Etudiant
class Etudiant(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    # Permet de sortir en string des éléments de l'objets passé en parametre
    def __repr__(self):
        return "Username: %r\nEmail: %r" %(self.username, self.username)

db.create_all()
