<template>
  <div id="navbar-main">
    <nav class="container-fluid m-auto p-0 navbar-light bg-light sticky-top">
      <ul class="row m-auto" style="background-color: rgb(230,237,248);">
        <li class="col-1 text-start my-auto px-2 py-3">
          <button type="button" class="navbar-toggler" data-bs-toggle="offcanvas" data-bs-target="#menu"
                  aria-expanded="false"
                  aria-controls="collapseNavbar">
            <span class="navbar-toggler-icon my-auto"></span>
          </button>
          <div class="offcanvas offcanvas-x-axis col-lg-3 col-xxl-2 p-0 mx-auto" tabindex="-1" id="menu"
               data-bs-keyboard="true"
               data-bs-backdrop="false" aria-labelledby="offcanvasExampleLabel">
            <div class="offcanvas-header">
              <img class="col-8" href="/" title="Class Meet" alt="Logo de Class Meet"
                   src="../assets/ClassMeet+logo-inline.png">
              <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas"
                      aria-label="Close"></button>
            </div>
            <div class="offcanvas-body fw-bold">
              <ul class="border-bottom border-dark nav navbar-nav flex-column"
                  style="font-size: 1.00rem; font-family: Loma,sans-serif; color: black"
                  id="sidebar">
                <li class="mb-3 ms-0 me-auto">
                  <a href="/" class="nav-link px-3">
                    <i class="fs-3 bi-table"></i><span class="px-3">Accueil</span> </a>
                </li>
                <li class="mb-3 ms-0 me-auto">
                  <a href="/programs" class="nav-link px-3">
                    <i class="fs-3 bi-clipboard-data"></i><span class="px-3">Programmes</span></a>
                </li>
                <li class="mb-3 ms-0 me-auto">
                  <a href="/Contact-us" class="nav-link px-3 dropdown-toggle text-wrap" role="button"
                     data-bs-toggle="dropdown"
                     id="dropdown"
                     aria-expanded="false">
                    <i class="fs-3 d-inline bi-chat-text"></i><span
                      class="px-3 text-break fs-6 text-start">Contactez-nous</span>
                  </a>
                  <ul class="dropdown-menu dropdown-menu-end shadow flex-column" aria-labelledby="dropdown">
                    <li><a class="dropdown-item" href="/FAQ">FAQ</a></li>
                    <li><a class="dropdown-item" href="/report-bug">Signaler un bug</a></li>
                    <li><a class="dropdown-item" href="/report-person">Signaler un camarade</a></li>
                    <li><a class="dropdown-item" href="/donate">Faire un don</a></li>
                  </ul>
                </li>
                <li class="ms-0 me-auto mb-3">
                  <a href="#" class="nav-link px-3">
                    <i class="fs-3 d-lg-inline bi-telephone-outbound"></i><span
                      class="px-3">Messages privés</span></a>
                </li>
                <li class="ms-0 me-auto mb-3">
                  <a href="#" class="nav-link px-3">
                    <i class="fs-3 d-inline bi-people"></i><span
                      class="px-3 text-break">S'inscrire</span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </li>
        <li class="col-2 text-center my-auto">
          <a class="navbar-brand" href="/"
             title="Cliquez ici pour revenir à la page principale">
            <img class=" col-7 col-xxl-5" alt="logo Class Meet" src="../assets/logo.png"></a>
        </li>
        <li class="col-auto col-xl-5 my-auto">
          <form class="d-flex justify-content-start">
            <input class="form-control flex-shrink-1 w-75" type="search" placeholder="Rechercher des étudiant(e)s"
                   aria-label="Rechercher">
            <button class="btn btn-outline-success text-center my-auto"
                    type="submit">Rechercher
            </button>
          </form>
        </li>
        <li v-if="$store.state.connected" class="col-auto my-auto ms-auto me-0 text-end">
          <a href="#" class="nav-link p-0 m-auto bg-transparent dropdown-toggle text-wrap"
             role="button"
             data-bs-toggle="dropdown"
             id="dropdown-user"
             aria-expanded="false"
             style="color: royalblue; font-size: 1.10rem;"><i class="d-inline fs-3 me-2 bi-person-circle"></i>Nami
            Reghbati</a>
          <ul class="dropdown-menu dropdown-menu-end shadow flex-column fixed-top" aria-labelledby="dropdown-user">
            <li><a class="dropdown-item" href="/profile#dashboard">Tableau de bord</a></li>
            <li><a class="dropdown-item" @click="disconnect" href="/">Déconnexion</a></li>
          </ul>
        </li>
        <li v-else class="col-auto my-auto ms-auto me-0 text-end">
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
    }
  }
}
</script>

<style>

body {
  overflow-x: hidden;
}

li {
  list-style-type: none;
}

.navbar-light .navbar-nav .nav-link {
  color: rgba(0, 0, 0, 1) !important;
}

.offcanvas-x-axis {
  top: 0;
  left: 0;
  width: auto;
  border-right: 1px solid rgba(0, 0, 0, .2);
  transform: translateX(-100%);
}

a:hover {
  opacity: 50%;
  color: cyan;
}

</style>
