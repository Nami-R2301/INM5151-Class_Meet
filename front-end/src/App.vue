<template>
  <div id="app">
    <router-view />
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

#app {
  font-family: Sen, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
