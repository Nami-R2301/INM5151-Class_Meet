import Database
from server import db
import data

### Main 

# Méthode d'ajout d'utilisateur de la classe Interaction  exemple


# Comment instancier des étudiants 
Jules = Database.Etudiant(username='jules',email='youle21' , password='xxx')
#Nami = Database.Etudiant(username='Nami2122',email='emailfoo' , password='xXxx')
#Mehdi = Database.Etudiant(username='Mehdi22',email='emailfoo2' , password='xXx')

# Comment instancier des cours
#inf5151 = Database.Sigle(sigle='INF5151')
#inf5171 = Database.Sigle(sigle='INF5171')
#inf5153 = Database.Sigle(sigle='INF5153')


# Comment instancier un post écrit par un élève.
#fooPost2 = Database.Publication( idEtudiant=(Jules.id), contenu="some random post2!" )
#Database.db.session.add(fooPost2)


# Need to add and commit to save it in Db
# evidemment ce sera fait automatiquement 
#Database.db.session.add(Jules)
#Database.db.session.add(Nami)
#Database.db.session.add(Mehdi)
#Database.db.session.add(inf5151)
#Database.db.session.add(inf5171)
#Database.db.session.add(inf5153)
Database.db.session.commit()

Database.db.create_all()

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
list_etudiants = Database.Etudiant.query.all()
#for Etudiant in list_etudiants:
#    print( Etudiant.id )

for etudiant in list_etudiants:
  print(etudiant)


