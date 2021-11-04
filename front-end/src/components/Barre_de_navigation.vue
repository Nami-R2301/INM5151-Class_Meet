<template>
  <v-img
      class="icon"
      :src="require('../assets/icon-menu.png')"
        ></v-img>
  <nav>
    <ul class="menu">
      <li><a href="Connexion.vue" title="Défiler les fonctionnalités vers la droite">
      </a></li>
      <li><a class="logo" href="Connexion.vue" title="Cliquez ici pour revenir à la page principale">
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
  Font-family: Sen, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  font-size: large;
  top: 0;
  left: 0;
  z-index: 3;
  margin: 0;
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
  padding: 1.5625% 2%;
  margin: 0 auto;
}

.logo {
  max-width: 100%;
  width: 20%;
  height: auto;
  padding: 0 2%;
  text-align: left;
}

.icon {
  height: auto;
  text-align: left;
  float: left;
  padding: 0;
  margin: 0 auto;
}


.class_Meet {
  max-width: 100%;
  width: 50%;
  height: auto;
  margin: 0 auto;
}

.menu a:hover {
  opacity: 50%;
  color: cyan;
}
</style>