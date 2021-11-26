@startuml
allow_mixing
class main 
package front-end {
class App
class main 
package components {
    class Connection
    class Barre_de_navigation
    class Footer
    class main
    class Post  
    class SideBar
    class Student_bar
}
package router {
    class index
}
package store {
    class index2
}
    package view {
        class Connection
        class Forum
        class Home
    }
}
components -- view
view -- App
store -- App 
router -- App
package back-end {
    class main {
        + db : Database
        + inter : Interaction
        + data : Data
}
class server {
    + app : Flask
    + inter Interaction
    + publications( categorie )
    + connection()
    + etudiant()
    }

class Interaction {
    + db Database
    + ObjetPublication
    + retourne_Publications( list_publications)
    + list_publications( sous_categorie )
    + list_etudiants()
    + ajout_utilisateur(username, psw, email)
    + ajout_publication ( auteur, sigle , contenu )
    + connection ( email, password )
}
class Data {
add_testing_data()
}
class Database {
    + etudiant : Etudiant
    + publication : Publication
    + cours : Cours 
}

}
package Base_de_données{
database sqlite3
}


server -- main
server -- Interaction
Interaction -- Database
Database -- sqlite3
Data -- Database

App -- main

@enduml
