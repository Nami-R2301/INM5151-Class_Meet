<template>
  <Barre_de_navigation/>
  <Connexion msg="Connectez-vous à Class Meet"/>
</template>

<script>
import Connexion from './components/Connexion.vue'
import Barre_de_navigation from "./components/Barre_de_navigation";

export default {
  name: 'App',
  components: {
    Barre_de_navigation,
    Connexion
  }
}
</script>

<style>
#app {
  font-family: Sen, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
