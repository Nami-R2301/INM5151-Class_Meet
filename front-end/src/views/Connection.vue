<template>
  <div>
    <Barre_de_navigation/>
    <Connexion msg="Connectez-vous à "/>
    <Footer/>
  </div>
</template>

<script>
import Connexion from "../components/Connexion.vue";
import Barre_de_navigation from "../components/Barre_de_navigation";
import Footer from "../components/Footer";

export default {
  name: "Connection",
  components: {
    Barre_de_navigation,
    Connexion,
    Footer,
  },
};
</script>

<style scoped>
</style>




