@startuml
allow_mixing
package front-end {
class App
    package view {
        class Connection
    }
}
view -- App
package back-end {
    class main 
}



@enduml
