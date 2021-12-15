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
      <main-navbar/>
      <router-view/>
    </div>
  </div>
</template>

<script>
import jQuery from "jQuery";
import mainNavbar from "./components/main-navbar";

export default {
  name: "App",
  components: {
    mainNavbar,
  },
  mounted() {
    this.initOnReload()

    let popper = document.createElement('script')
    popper.setAttribute('src', 'node_modules/@popperjs/core/dist/cjs/popper.js')
    document.head.appendChild(popper)
    let dropdown = document.createElement('script')
    dropdown.setAttribute('src', 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/js/bootstrap.bundle.min.js')
    document.head.appendChild(dropdown)

  },
  methods: {
    initOnReload() {
      if(this.$cookies.get("user")) {
        this.$store.state.connected = true
      }
    },
    function() {
      jQuery('.dropdown-toggle').dropdown()
    }
  },
  beforeCreate() {
    if (
        window.location.pathname !== "/login" &&
        !this.$cookies.get("user")
    ) {
      this.$router.push("/");
    } else if (
        window.location.pathname === "/login" &&
        this.$cookies.get("user")
    ) {
      this.$router.push("/profile");
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

i {
  vertical-align: middle;
}

.content-body {
  min-height: 100%;
}
</style>
