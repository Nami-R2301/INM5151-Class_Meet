import Database

# Etudiant
list_etudiants = [
    {"username": 'Mehdi3', "email": 'test@test.test', "password": 'xxx'},
    {"username": 'jules', "email": 'youle21', "password": 'xxx'},
    {"username": 'Nami2122', "email": 'emailfoo', "password": 'xxx'},
    {"username": 'Mehdi22', "email": 'emailfoo2', "password": 'xxx'}
]

list_cours = [
    {"sigle": "INF5151"},
    {"sigle": "INF5171"},
    {"sigle": "INF5153"},
]


for etudiant in list_etudiants:
    db_etudiant = Database.Etudiant(username=etudiant["username"],
                                    email=etudiant["email"],
                                    password=etudiant["password"])
    Database.db.session.add(db_etudiant)

for cours in list_cours:
    db_cours = Database.Sigle(sigle=cours["sigle"])
    Database.db.session.add(db_cours)
