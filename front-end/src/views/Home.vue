<template>
  <div>
    <Barre_de_navigation/>
    <SideBar/>
    <Main/>
    <Footer/>
  </div>
</template>

<script>
import Barre_de_navigation from "../components/Barre_de_navigation";
import SideBar from "../components/SideBar";
import Footer from "../components/Footer";
import Main from "../components/Main";

export default {
  name: "Home",
  components: {
    Barre_de_navigation,
    SideBar,
    Main,
    Footer,
  }
}
</script>

<style>

</style>