<template>
    <nav>
      <ul class="menu">
        <li>
          <a class="container_accessibility" href="Connexion.vue" title="Défiler les fonctionnalités vers la droite">
          <img class="accessibility" alt="icône de menu" src="../assets/icon-menu.png">
        </a>
        </li>
        <li class="container_brand">
          <a href="Connexion.vue" title="Cliquez ici pour revenir à la page principale">
          <img class="logo" alt="logo Class Meet" src="../assets/logo.png">
          <img class="class_Meet" alt="Class Meet" src="../assets/Class_Meet.png"></a>
        </li>
        <li><a class="lien-connexion" href="Connexion.vue" title="Connectez-vous">Connectez-vous</a></li>
      </ul>
    </nav>
</template>

<script>
export default {
  name: "Barre_de_navigation",
}
</script>

<style>

.menu {
  position: fixed;
  font-family: Sen, "Times New Roman", serif;
  font-size: 120%;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  top: 0;
  left: 0;
  z-index: 3;
  margin: 0 0 1% 0;
  padding: 0;
  width: 100%;
  list-style-type: none;
  overflow: hidden;
  background: aliceblue;
}

.menu a {
  float: left;
  display: block;
  padding: 1.5625% 2%;
  color: black;
  font-weight: bold;
  overflow: hidden;
  text-decoration: none;
}


a.lien-connexion {
  float: right;
  padding: 0 2%;
  margin: 2% 0;
  text-align: center;
}

.container_accessibility {
  max-width: 3%;
  text-align: left;
}


.accessibility {
  width: 60%;
  height: 5%;
  padding-left: 1%;
  text-align: left;
}

.container_brand a {
  max-width: 25%;
  text-align: left;
  margin: 1% 2%;
  padding: 0;
}

.logo {
  padding: 0;
  width: 15%;
  height: auto;
}

.class_Meet {
  max-width: 100%;
  width: 40%;
  height: auto;
  margin: 0 auto;
}

.menu a:hover {
  opacity: 50%;
  color: cyan;
}
</style>