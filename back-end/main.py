import Database
import server

#create object Etudiant that can go in Db
Jules = Database.Etudiant(username='jules',email='youle21' , password='xxx')
#Nami = Database.Etudiant(username='Nami2122',email='emailfoo' , password='xXxx')
#Mehdi = Database.Etudiant(username='Mehdi22',email='emailfoo2' , password='xXx')
#
#
#inf5151 = Database.Sigle(sigle='INF5151')
#inf5171 = Database.Sigle(sigle='INF5171')
#inf5153 = Database.Sigle(sigle='INF5153')
fooPost = Database.Publication( idEtudiant=Jules.id, contenu="some random post!" )
Database.db.session.add(fooPost)
## Need to add and commit to save it in Db
#Database.db.session.add(Jules)
#Database.db.session.add(Nami)
#Database.db.session.add(inf5151)
#Database.db.session.add(inf5171)
#Database.db.session.add(inf5153)
#Database.db.session.add(Mehdi)
Database.db.session.commit()
print( fooPost )
print( fooPost.contenu )

# Accède à la db pour faire une liste actuelle des étudiants dans la table étudiant
list_etudiants = Database.Etudiant.query.all()
##list_inscriptions = Database.Inscription.query.all()
#test = Database.Inscription()
#test.sigle = Database.Sigle.query.all()
#Jules.cours.append(test)
#Database.Inscription.sigle = Database.Sigle
#Jules.cours.append( Database.Inscription.sigle )
#Database.print_etudiant(Etudiants=list_etudiants)


#for assoc in Jules.cours:
#    print(assoc.sigle)
#Database.print_inscription( Jules )
