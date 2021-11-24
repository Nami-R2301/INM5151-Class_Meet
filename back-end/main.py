import Database
import data

# Accède à la db pour faire une liste actuelle des étudiants dans la table étudiant
list_etudiants = Database.Etudiant.query.all()

for etudiant in list_etudiants:
  print(etudiant)

