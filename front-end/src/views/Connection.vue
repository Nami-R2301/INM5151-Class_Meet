<template>
  <div class="container-fluid">
    <div class="row">
      <Barre_de_navigation class="col-12" />
    </div>
    <div class="row">
      <div class="col-12">
        <Connexion msg="Connectez-vous à " />
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <Footer />
      </div>
    </div>
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




