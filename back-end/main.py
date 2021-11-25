import Database 
import Interation as i
import data

### Main 

# add some testing data after reseting database
data.add_testing_data()


# Accède à la db pour faire une liste actuelle des étudiants dans la table étudiant
list_etudiants = Database.Etudiant.query.all()
# Méthode qui renvois les éleves inscrits
i.print_etudiant(Etudiants=list_etudiants)
i.print_publications( 'INF5151' )

