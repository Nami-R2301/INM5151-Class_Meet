<template>
  <div id="app">
    <head>
      <title>Connexion</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: "App",

  /*beforeCreate() {
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
*/
}
</script>

<style>

#app {
  font-family: Sen, Helvetica, Arial,serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
