import Database

# Etudiant
list_etudiants = [
    {"username": 'Mehdi3', "email": 'test@test.test', "password": 'xxx'},
    {"username": 'jules', "email": 'youle21', "password": 'xxx'},
    {"username": 'Nami2122', "email": 'emailfoo', "password": 'xxx'},
    {"username": 'Mehdi22', "email": 'emailfoo2', "password": 'xxx'}
]

for etudiant in list_etudiants:
    db_etudiant = Database.Etudiant(username=etudiant["username"],
                                    email=etudiant["email"],
                                    password=etudiant["password"])
    Database.db.session.add(db_etudiant)

# Database.db.session.commit()
