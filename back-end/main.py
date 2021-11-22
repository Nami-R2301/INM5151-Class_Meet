import Database

#create object Etudiant that can go in Db
#jules = Database.etudiant(username='jules',email='youle21' , password='xxx')
#Nami = Database.Etudiant(username='Nami2122',email='emailfoo' , password='xXxx')
#Mehdi = Database.Etudiant(username='Mehdi22',email='emailfoo2' , password='xXx')


# Need to add and commit to save it in Db
#Database.db.session.add(Mehdi)
#Database.db.session.commit()


# Accède à la db pour faire une liste actuelle des étudiants dans la table étudiant
list_etudiants = Database.Etudiant.query.all()

Database.print_etudiant(Etudiants=list_etudiants)

