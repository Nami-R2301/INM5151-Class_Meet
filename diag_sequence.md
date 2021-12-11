@startuml
title Publier message dans un salon
User -> System : fetch( url, publication )
activate System
System -> System : ajout_publication(auteur, categorie, contenu )
System -> System : Publication( auteur, categorie, contenu )
System -> System : session.add()
System -> System : session.commit()
System -> User : publication 
deactivate System
User -> System : fetch(url)
activate System
System -> System : list_publication( sigle )
System -> System : Publication( auteur, categorie, contenu )
System -> User : list_publication
deactivate System
@enduml
