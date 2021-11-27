import Database 
import Interation as i
import data

### Main 

# add some testing data after reseting database
#data.add_testing_data()


# Accède à la db pour faire une liste actuelle des étudiants dans la table étudiant
list_etudiants = Database.Etudiant.query.all()
# Méthode qui renvois les éleves inscrits
#i.print_etudiant(Etudiants=list_etudiants)
# affiche les publication du la catégorie cours INF5151
#i.print_publications( 'INF5151' )

