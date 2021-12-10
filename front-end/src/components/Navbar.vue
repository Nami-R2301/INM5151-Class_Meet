<template>
    <nav class="container-fluid m-auto p-0 navbar-light bg-light sticky-top ">
      <ul class="row m-auto p-0" style="background-color: rgb(230,237,248);">
        <li class="col-1 text-center m-auto py-3">
          <button type="button" class="navbar-toggler" data-bs-target="#collapsibleNavbar" aria-expanded="false"
                  aria-controls="collapseNavbar">
            <span class="navbar-toggler-icon my-auto"></span>
          </button>
        </li>
        <li class="col-1 text-start m-auto">
          <a class="navbar-brand my-auto" href="/home"
             title="Cliquez ici pour revenir à la page principale">
            <img class=" col-12 col-lg-12 col-xxl-10 my-auto" alt="logo Class Meet" src="../assets/logo.png"></a>
        </li>
        <li class="col-5 text-start m-auto">
          <form class="d-flex">
            <input class="form-control w-75" type="search" placeholder="Rechercher des programmes"
                   aria-label="Rechercher">
            <button class="btn btn-outline-success text-center my-auto"
                    type="submit">Rechercher
            </button>
          </form>
        </li>
        <li class="col-1 my-auto text-end">
          <a class="nav-link active connection my-auto" href="/forum/INF5151"
             title="Connectez-vous">Forum</a>
        </li>
        <li class="col-3 my-auto text-end">
          <a class="nav-link active connection" href="/login"
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

.connection {
  padding: 0;
  color: #000000;
  font-size: medium;
  font-weight: bold;
  text-decoration: none;
}

.connection:hover {
  color: #06b8f6;
}

li {
  list-style-type: none;
}

.logo:hover {
  opacity: 70%;
}

a:hover {
  opacity: 50%;
  color: cyan;
}
</style>
