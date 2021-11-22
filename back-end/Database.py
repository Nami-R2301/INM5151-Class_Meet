from server import db

# Etudiant
class Etudiant(db.Model):
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
