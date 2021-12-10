<template>
  <div id="app">
    <head>
      <title>Connexion</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" rel="stylesheet">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
    </head>
    <Navbar/>
    <router-view/>
    <Footer/>
  </div>
</template>

<script>
import Footer from "./components/Footer";
import Navbar from "./components/Navbar";

export default {
  name: "App",
  components: {
    Navbar,
    Footer,
  },

  beforeCreate() {
    if (
        window.location.pathname !== "/login" &&
        !this.$cookies.get("user")
    ) {
      this.$router.push("/login");
    } else if (
      window.location.pathname === "/login" &&
        this.$cookies.get("user")
    ) {
      this.$router.push("/");
    }
  },
};
</script>

<style>

#app {
  font-family: Sen, Helvetica, Arial,serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
