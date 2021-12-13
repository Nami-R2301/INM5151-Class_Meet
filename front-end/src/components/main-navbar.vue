<template>
    <nav class="container-fluid m-auto p-0 navbar-light bg-light sticky-top">
      <ul class="row m-auto" style="background-color: rgb(230,237,248);">
        <li class="col-1 text-start my-auto px-2 py-3">
          <button type="button" class="navbar-toggler" data-bs-target="#collapsibleNavbar" aria-expanded="false"
                  aria-controls="collapseNavbar">
            <span class="navbar-toggler-icon my-auto"></span>
          </button>
        </li>
        <li class="col-2 text-center my-auto">
          <a class="navbar-brand" href="/home"
             title="Cliquez ici pour revenir à la page principale">
            <img class=" col-7 col-xxl-5" alt="logo Class Meet" src="../assets/logo.png"></a>
        </li>
        <li class="col-auto col-xl-5 my-auto">
          <form class="d-flex justify-content-start">
            <input class="form-control flex-shrink-1 w-75" type="search" placeholder="Rechercher des programmes"
                   aria-label="Rechercher">
            <button class="btn btn-outline-success text-center my-auto"
                    type="submit">Rechercher
            </button>
          </form>
        </li>
        <li class="col-auto m-auto text-center">
          <a class="nav-link active fw-bold" href="/forum/INF5151"
             title="Connectez-vous">Forum</a>
        </li>
        <li class="col-auto my-auto ms-auto me-0 text-end">
          <a class="nav-link active fw-bold" href="/login"
             title="Connectez-vous">Connectez-vous</a>
        </li>
      </ul>
    </nav>
</template>

<script>
export default {
  name: "Navbar",
}
</script>

<style>

li {
  list-style-type: none;
}

a:hover {
  opacity: 50%;
  color: cyan;
}
</style>
