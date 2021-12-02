<template>
  <div id="barre-nav" class="Barre_de_navigation">
    <nav class="container-fluid navbar-nav m-auto navbar-light bg-light sticky-top">
      <ul class="row flex-nowrap py-3" style="background-color: rgb(230,237,248); padding-left: 2%">
        <li class="col-1 centered  py-3">
          <button type="button" class="navbar-toggler" data-bs-target="#collapsibleNavbar" aria-expanded="false"
                  aria-controls="collapseNavbar">
            <span class="navbar-toggler-icon"></span>
          </button>
        </li>
        <li class="col-3 co-lg-3 col-xl-3 col-xxl-2 py-1 py-lg-0 py-xl-0 py-xxl-0">
          <a class="navbar-item" href="/"
             title="Cliquez ici pour revenir à la page principale">
            <img class="logo offset-lg-1 offset-xl-1 offset xxl-0 col-4" alt="logo Class Meet" src="../assets/logo.png">
            <img class="class_Meet col-6" alt="Class Meet" src="../assets/Class_Meet.png"></a>
        </li>
        <li class="col-4 col-lg-5 col-xxl-4 py-3">
          <form class="d-flex justify-content-sm-start">
            <input class="form-control" type="search" placeholder="Rechercher des programmes"
                   aria-label="Rechercher">
            <button class="btn btn-outline-success w-auto"
                    type="submit">Rechercher
            </button>
          </form>
        </li>
        <li class="col-4 col-lg-3 col-xxl-5 py-3">
          <a class="nav-link active connection" href="/login"
             title="Connectez-vous"><span class="glyphicon glyphicon-log-in"></span>Connectez-vous</a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Barre_de_navigation",
}
</script>

<style>

.centered {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.container-fluid {
  margin: 0 auto;
  max-width: 100%;
}

.logo {
  margin: 0 auto;
  max-width: 100%;
}

span, a {
  text-align: left;
}

.class_Meet {
  margin: 0 auto;
  max-width: 100%;
}


.connection {
  float: right;
  padding: 0;
  margin-right: 5%;
  color: #000000;
  font-weight: bold;
  text-decoration: none;
}

.connection:hover {
  color: #06b8f6;
}

.container-fluid {
  display: inline-block;
}

.row {
  margin: 0 auto;
  flex-wrap: nowrap;
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