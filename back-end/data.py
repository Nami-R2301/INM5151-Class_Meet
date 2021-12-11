import Database
import Interation as i

# Etudiant
def add_testing_data():
    Database.db.drop_all()
    Database.db.create_all()

    # ajout de publications
    i.ajout_publication('jules', 'INF5151', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut commodo turpis, sit amet porttitor nibh. In hac habitasse platea dictumst. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla dapibus ex non purus dapibus, sit amet ultrices orci dictum. Etiam auctor non orci tempus ultricies. Ut molestie risus massa, sit amet auctor arcu viverra in. Cras vulputate purus vitae lacus ultricies, vitae gravida enim gravida. Vestibulum risus lorem, semper non lorem condimentum, hendrerit fringilla ipsum. Duis sed tellus nec erat feugiat imperdiet. Duis vitae sem ut nulla posuere malesuada. Aliquam et lacus a orci porttitor finibus.')
    i.ajout_publication('jules', 'INF5153', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut commodo turpis, sit amet porttitor nibh. In hac habitasse platea dictumst. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla dapibus ex non purus dapibus, sit amet ultrices orci dictum. Etiam auctor non orci tempus ultricies. Ut molestie risus massa, sit amet auctor arcu viverra in. Cras vulputate purus vitae lacus ultricies, vitae gravida enim gravida. Vestibulum risus lorem, semper non lorem condimentum, hendrerit fringilla ipsum. Duis sed tellus nec erat feugiat imperdiet. Duis vitae sem ut nulla posuere malesuada. Aliquam et lacus a orci porttitor finibus.')
    i.ajout_publication('jules', 'INF5151', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut commodo turpis, sit amet porttitor nibh. In hac habitasse platea dictumst. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla dapibus ex non purus dapibus, sit amet ultrices orci dictum. Etiam auctor non orci tempus ultricies. Ut molestie risus massa, sit amet auctor arcu viverra in. Cras vulputate purus vitae lacus ultricies, vitae gravida enim gravida. Vestibulum risus lorem, semper non lorem condimentum, hendrerit fringilla ipsum. Duis sed tellus nec erat feugiat imperdiet. Duis vitae sem ut nulla posuere malesuada. Aliquam et lacus a orci porttitor finibus.')
    i.ajout_publication('jules', 'INF5151', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut commodo turpis, sit amet porttitor nibh. In hac habitasse platea dictumst. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla dapibus ex non purus dapibus, sit amet ultrices orci dictum. Etiam auctor non orci tempus ultricies. Ut molestie risus massa, sit amet auctor arcu viverra in. Cras vulputate purus vitae lacus ultricies, vitae gravida enim gravida. Vestibulum risus lorem, semper non lorem condimentum, hendrerit fringilla ipsum. Duis sed tellus nec erat feugiat imperdiet. Duis vitae sem ut nulla posuere malesuada. Aliquam et lacus a orci porttitor finibus.')
    
    # ajout d'étudiants
    i.ajout_utilisateur("Jules", "xxx", "youle21@yahoo.ca")
    i.ajout_utilisateur("Mehdi", "xxx", "test@test.test")
    i.ajout_utilisateur("Nami", "xxx", "nami.reghbati@gmail.ca")
    
    # ajout cours
    i.ajout_cours("INF5151", "AU21")
    i.ajout_cours("INF5171", "AU21")
    i.ajout_cours("INF5153", "AU20")
    i.ajout_cours("INF1132", "H19")

    # ajout inscription
    i.ajout_inscription( "youle21@yahoo.ca", "INF5151" )
    i.ajout_inscription( "youle21@yahoo.ca", "INF5153" )
    i.ajout_inscription( "test@test.test", "INF1132" )
    i.ajout_inscription( "test@test.test", "INF5151" )
    i.ajout_inscription( "nami.reghbati@gmail.ca", "INF5151" )

    

