# INM5151-Class_Meet
Dépôt pour notre projet de session dans le cours INM5151 de la session A-21

## Navigation
Le projet est divisé en deux repertoire, le **front-end** et le **back-end**.

/front-end
  /src : Tout notre code
    /App.vue : La page principale
    /assets : L'endroit où les images sont stockés
    /components : Les components sont des parties de HTML ré-utilisable
    /main.js : L'endroit où est utilisé l'instance de vue
    /router : Un simple routeur qui permet la redirection dans notre site web
    /store : Le store est en quelque sorte un endroit où sont les vari
    /views : Les vues sont des pages que le routeur appellera
 
/back-end
  /data.py : Ce fichier represente notre jeux de données
  /Database.py : Ce fichier represente les tables de notre base de données
  /Database.sqlite3 : Notre base de données
  /Interation.py : Permet de creer l'intermediaire entre le server et la database
  /main.py : Permet de reinitialiser la base de donnees
  /server.py : Ce que flask a besoin comme fichier. Il représente toute les routes de notre back-end


## Comment lancer le projet Front-end
1. Installer [node.js](https://nodejs.org/en/)
2. Faites la commande `npm i`
3. Puis `npm run serve`

## Librairie à installer pour le back-end
* [Python](https://www.python.org/downloads/) 
* Flask: `python -m pip install flask`
* flask sqlalchemy: `python -m pip install Flask-SQLAlchemy`
* flask cors: `python -m pip install flask-cors`



## En savoir plus
- [Architecture de dossiers](https://itnext.io/how-to-structure-my-vue-js-project-e4468db005ac) avec Vue.
- Install **sqlalchemy** for DB with flask with command 'pip install flask-sqlalchemy' or 'pip3 install flask-sqlalchemy'
- Install **flask-cors** for allow *Access-Control-Allow-Origin* with command `pip install flask-cors` or `pip install -U flask-cors`

