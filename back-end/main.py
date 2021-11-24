import Database
from server import db
import data

### Main 

Database.db.session.commit()
Database.db.create_all()

# Comment instancier un post écrit par un élève.
#fooPost2 = Database.Publication( idEtudiant=(Jules.id), contenu="some random post2!" )
#Database.db.session.add(fooPost2)

# Afficher un post
#print( fooPost )
#print( fooPost.contenu )

# filtrer query 
#idTmp = Database.Etudiant.query.filter_by(username='jules').all()
#Database.print_etudiant( idTmp )

#list_post = Database.Publication.query.all() 
#for  Database.Publication in list_post:
#        print(Database.Publication.id,  Database.Publication.idEtudiant )

# Accède à la db pour faire une liste actuelle des étudiants dans la table étudiant
for etudiant in Database.Etudiant.query.all():
    print(etudiant)
