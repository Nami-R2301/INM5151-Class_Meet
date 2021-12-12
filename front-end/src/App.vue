<template>
  <div id="app" class="m-auto p-0">
    <head>
      <title>Connexion</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" rel="stylesheet">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
    </head>
    <div class="content-body">
      <Navbar/>
      <router-view/>
    </div>
  </div>
</template>

<script>
import Navbar from "./components/main-navbar";
import jQuery from "jQuery";

export default {
  name: "App",
  components: {
    Navbar,
  },
  mounted() {
    let popper = document.createElement('script')
    popper.setAttribute('src', 'node_modules/@popperjs/core/dist/cjs/popper.js')
    document.head.appendChild(popper)
    let dropdown = document.createElement('script')
    dropdown.setAttribute('src', 'node_modules/bootstrap/dist/js/bootstrap.bundle.min.js')
    document.head.appendChild(dropdown)

  },
  methods: {
    function() {
      jQuery('.dropdown-toggle').dropdown()
    }
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

html {
  min-height: 100%;
}

#app {
  font-family: 'Ubuntu', 'Lucida Grande', 'Lucida Sans Unicode', 'Geneva', 'Verdana', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.content-body {
  min-height: 100%;
}
</style>
