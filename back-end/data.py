import Database
import Interation as i

# Etudiant
def add_testing_data():
    Database.db.drop_all()
    Database.db.create_all()

    list_etudiants = [
            {"username": 'Mehdi3', "email": 'test@test.test', "password": 'xxx'},
        {"username": 'jules', "email": 'youle21', "password": 'xxx'},
        {"username": 'Nami2122', "email": 'emailfoo', "password": 'xxx'},
        {"username": 'Mehdi22', "email": 'emailfoo2', "password": 'xxx'}
    ]

    list_cours = [
        {"sigle": "INF5151", "session": "AU21"},
        {"sigle": "INF5171", "session": "AU21"},
        {"sigle": "INF5153", "session": "AU21"},
    ]


    for etudiant in list_etudiants:
        db_etudiant = Database.Etudiant(username=etudiant["username"],
                                        email=etudiant["email"],
                                        password=etudiant["password"])
        Database.db.session.add(db_etudiant)

    for cours in list_cours:
        db_cours = Database.Cours(sigle=cours["sigle"])
        Database.db.session.add(db_cours)

    i.ajout_publication('jules', 'INF5151', 'testing post 1')
    i.ajout_publication('jules', 'INF5153', 'testing post 2')
    i.ajout_publication('jules', 'INF5151', 'testing post 3')
    i.ajout_publication('jules', 'INF5151', 'testing post 4')

    Database.db.session.commit()

