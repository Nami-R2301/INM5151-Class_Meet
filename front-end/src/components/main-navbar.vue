<template>
  <div id="navbar-main">
    <nav class="container-fluid m-auto p-0 navbar-light bg-light sticky-top">
      <ul class="row m-auto" style="background-color: rgb(230,237,248);">
        <li class="col-1 text-start my-auto px-1 py-3">
          <b-button v-b-toggle.sidebar variant="transparent" class="navbar-toggler-icon p-3"></b-button>
          <div>
            <b-sidebar id="sidebar" title="Class Meet" shadow>
              <ul class="border-bottom border-dark nav navbar-nav flex-column ms-3"
                  style="font-size: 1.00rem; font-family: Loma,sans-serif; color: black"
                  id="sidebar">
                <li class="mb-3 me-auto">
                  <a href="/" class="nav-link px-2">
                    <b-icon-person-circle scale="1" shift-h="4" style="vertical-align: middle"
                                          class="text-black mx-auto"></b-icon-person-circle>
                    <span style="vertical-align: middle" class="px-3">Accueil</span> </a>
                </li>
                <li class="mb-3 me-auto">
                  <a href="/programs" class="nav-link px-2">
                    <b-icon-person-circle scale="1" shift-h="4" style="vertical-align: middle"
                                          class="text-black mx-auto"></b-icon-person-circle>
                    <span style="vertical-align: middle" class="px-3">Programmes</span></a>
                </li>
                <li class="mb-3 me-auto">
                  <a href="/Contact-us" class="nav-link px-2 dropdown-toggle text-wrap" role="button"
                     data-bs-toggle="dropdown"
                     id="dropdown"
                     aria-expanded="false">
                    <b-icon-person-circle scale="1" shift-h="4" style="vertical-align: middle"
                                          class="text-black mx-auto"></b-icon-person-circle>
                    <span
                        style="vertical-align: middle" class="px-3 text-break fs-6 text-start">Contactez-nous</span>
                  </a>
                  <ul class="dropdown-menu dropdown-menu-end shadow flex-column" aria-labelledby="dropdown">
                    <li><a class="dropdown-item" href="/FAQ">FAQ</a></li>
                    <li><a class="dropdown-item" href="/report-bug">Signaler un bug</a></li>
                    <li><a class="dropdown-item" href="/report-person">Signaler un camarade</a></li>
                    <li><a class="dropdown-item" href="/donate">Faire un don</a></li>
                  </ul>
                </li>
                <li class="me-auto mb-3">
                  <a href="#" class="nav-link px-2">
                    <b-icon-person-circle scale="1" shift-h="4" style="vertical-align: middle"
                                          class="text-black mx-auto"></b-icon-person-circle>
                    <span
                        style="vertical-align: middle" class="px-3">Messages privés</span></a>
                </li>
                <li class="me-auto mb-3">
                  <a href="/login" class="nav-link px-2">
                    <b-icon-person-circle scale="1" shift-h="4" style="vertical-align: middle"
                                          class="text-black mx-auto"></b-icon-person-circle>
                    <span
                        style="vertical-align: middle" class="px-3 text-break">Se connecter</span>
                  </a>
                </li>
              </ul>
            </b-sidebar>
          </div>
        <li class="col-2 text-center my-auto">
          <a class="navbar-brand" href="/"
             title="Cliquez ici pour revenir à la page principale">
            <img class="ms-2 me-auto d-inline-flex justify-content-center col-7 col-xxl-5" alt="logo Class Meet"
                 src="../assets/logo.png"></a>
        </li>
        <li class="col-5 my-auto">
          <form class="d-flex justify-content-start">
            <input class="form-control flex-shrink-1 w-75" type="search" placeholder="Rechercher des étudiant(e)s"
                   aria-label="Rechercher">
            <button class="btn btn-outline-success text-center my-auto"
                    type="submit">Rechercher
            </button>
          </form>
        </li>
        <li v-if="$store.state.connected" class="col-4 p-0 d-flex justify-content-end my-auto ms-auto me-0">
          <a href="#" class="nav-link py-0 ps-auto pe-0 pe-md-3 bg-transparent dropdown-toggle text-wrap"
             role="button"
             data-bs-toggle="dropdown"
             id="dropdown-user"
             aria-expanded="false"
             style="color: royalblue; font-size: 1.10rem; vertical-align: middle;">
            <b-icon-person-circle class="text-black" shift-v="1" shift-h="-1" style="vertical-align: middle"
                                  font-scale="2"></b-icon-person-circle>
            {{ $cookies.get("user").username }}</a>
          <ul class="dropdown-menu dropdown-menu-end shadow flex-column fixed-top" aria-labelledby="dropdown-user">
            <li><a class="dropdown-item" href="/profile#dashboard">Tableau de bord</a></li>
            <li><a class="dropdown-item" @click="disconnect" href="/">Déconnexion</a></li>
          </ul>
        </li>
        <li v-else class="col-4 p-0 d-flex justify-content-end my-auto ms-auto me-0">
          <a class="nav-link active fw-bold" href="/login"
             title="Connectez-vous">Connectez-vous</a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  methods: {
    disconnect() {
      this.$store.dispatch("connection")
      this.$cookies.remove("user")
      this.$router.push("/")
    },
  }
}
</script>

<style>

li {
  list-style-type: none;
}

.navbar-light .navbar-nav .nav-link {
  color: rgba(0, 0, 0, 1) !important;
}

header.b-sidebar-header {
  color: #06b8f6;
}

a:hover {
  opacity: 50%;
  color: cyan;
}

</style>
