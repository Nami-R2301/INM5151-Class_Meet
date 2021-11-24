<template>
  <div id="app">
    <head>
      <title>Connexion</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" rel="stylesheet">
      <script type="application/javascript"
              src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <Barre_de_navigation/>
    <Connexion msg="Connectez-vous à "/>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: "App",

  beforeCreate() {
    if (
      this.$router.currentRoute.fullPath !== "/login" &&
      !this.$store.state.session_id
    ) {
      this.$router.push("/login");
    } else if (
      this.$router.currentRoute.fullPath === "/login" &&
      this.$store.state.session_id
    ) {
      this.$router.push("/");
    }
  },
};
</script>

<style>
body {
  margin: 0;
}

.container-fluid {
  width: auto;
}

.row > * {
  padding: 0;
}

#app {
  font-family: Sen, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
