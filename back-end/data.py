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

    i.ajout_publication('jules', 'INF5151', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut commodo turpis, sit amet porttitor nibh. In hac habitasse platea dictumst. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla dapibus ex non purus dapibus, sit amet ultrices orci dictum. Etiam auctor non orci tempus ultricies. Ut molestie risus massa, sit amet auctor arcu viverra in. Cras vulputate purus vitae lacus ultricies, vitae gravida enim gravida. Vestibulum risus lorem, semper non lorem condimentum, hendrerit fringilla ipsum. Duis sed tellus nec erat feugiat imperdiet. Duis vitae sem ut nulla posuere malesuada. Aliquam et lacus a orci porttitor finibus.')
    i.ajout_publication('jules', 'INF5153', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut commodo turpis, sit amet porttitor nibh. In hac habitasse platea dictumst. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla dapibus ex non purus dapibus, sit amet ultrices orci dictum. Etiam auctor non orci tempus ultricies. Ut molestie risus massa, sit amet auctor arcu viverra in. Cras vulputate purus vitae lacus ultricies, vitae gravida enim gravida. Vestibulum risus lorem, semper non lorem condimentum, hendrerit fringilla ipsum. Duis sed tellus nec erat feugiat imperdiet. Duis vitae sem ut nulla posuere malesuada. Aliquam et lacus a orci porttitor finibus.')
    i.ajout_publication('jules', 'INF5151', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut commodo turpis, sit amet porttitor nibh. In hac habitasse platea dictumst. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla dapibus ex non purus dapibus, sit amet ultrices orci dictum. Etiam auctor non orci tempus ultricies. Ut molestie risus massa, sit amet auctor arcu viverra in. Cras vulputate purus vitae lacus ultricies, vitae gravida enim gravida. Vestibulum risus lorem, semper non lorem condimentum, hendrerit fringilla ipsum. Duis sed tellus nec erat feugiat imperdiet. Duis vitae sem ut nulla posuere malesuada. Aliquam et lacus a orci porttitor finibus.')
    i.ajout_publication('jules', 'INF5151', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut commodo turpis, sit amet porttitor nibh. In hac habitasse platea dictumst. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla dapibus ex non purus dapibus, sit amet ultrices orci dictum. Etiam auctor non orci tempus ultricies. Ut molestie risus massa, sit amet auctor arcu viverra in. Cras vulputate purus vitae lacus ultricies, vitae gravida enim gravida. Vestibulum risus lorem, semper non lorem condimentum, hendrerit fringilla ipsum. Duis sed tellus nec erat feugiat imperdiet. Duis vitae sem ut nulla posuere malesuada. Aliquam et lacus a orci porttitor finibus.')

    Database.db.session.commit()

