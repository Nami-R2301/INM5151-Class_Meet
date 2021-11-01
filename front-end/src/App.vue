<template>
  <img alt="Vue logo" src="./assets/logo-Class_Meet.png">
  <Connexion msg="Bienvenue à Class Meet"></Connexion>
</template>

<script>
import Connexion from "./components/Connexion";

export default {
  name: 'App',
  components: {
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
  color: #87ceeb;
  margin-top: 60px;
}
</style>
