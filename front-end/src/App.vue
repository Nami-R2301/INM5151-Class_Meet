<template>
  <div id="app">
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <script
      type="application/javascript"
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/js/bootstrap.bundle.min.js"
    ></script>
    <div class="container-fluid">
      <div class="row">
        <Barre_de_navigation class="col-12" />
      </div>
      <div class="row">
        <div class="col-12">
          <router-view />
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <Footer />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Barre_de_navigation from "./components/Barre_de_navigation";
import Footer from "./components/Footer";

export default {
  name: "App",
  components: {
    Barre_de_navigation,
    Footer,
  },
  beforeCreate() {
    // Disable for dev
    // this.checkLogin()
  },
  methods: {
    checkLogin() {
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

.row > [class^="col"] {
  padding: 0;
}

#app {
  font-family: Sen, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
