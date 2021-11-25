<template>
  <div id="barre-nav" class="Barre_de_navigation">
    <nav class="container-fluid navbar-nav m-lg-auto navbar-light bg-light sticky-md-top">
      <ul class="row flex-nowrap" style="background-color: rgb(230,237,248); padding-left: 2%">
        <li class="col-1 col-sm-2 col-md-1 col-lg-1 col-xl-1 col-xxl-1 align-content-start">
          <button type="button" class="navbar-toggler" data-bs-target="#collapsibleNavbar" aria-expanded="false"
                  aria-controls="collapseNavbar">
            <span class="navbar-toggler-icon"></span>
          </button>
        </li>
        <li class="col-4 col-sm-3 col-md-3 col-lg-3 col-xl-3 col-xxl-2">
          <a class="navbar-brand" href="Connexion.vue"
             title="Cliquez ici pour revenir à la page principale">
            <img class="logo" alt="logo Class Meet" src="../assets/logo.png">
            <img class="class_Meet" alt="Class Meet" src="../assets/Class_Meet.png"></a>
        </li>
        <li class="col-4 col-sm-5 col-md-5 col-lg-5 col-xl-5 col-xxl-4">
          <form class="d-flex justify-content-sm-start">
            <input class="form-control" type="search" placeholder="Rechercher des programmes"
                   aria-label="Rechercher">
            <button class="btn btn-outline-success" type="submit">Rechercher</button>
          </form>
        </li>
        <li class="col-3 col-sm-2 col-md-3 col-lg-3 col-xl-3 col-xxl-5 nav-item">
          <a class="nav-link active connection" href="Connexion.vue"
             title="Connectez-vous"><span class="glyphicon glyphicon-log-in"></span>Connectez-vous</a>
        </li>
      </ul>
    </nav>
    <div class="collapse" id="collapsibleNavbar">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "Barre_de_navigation",
}
</script>

<style>


.connection {
  float: right;
  padding: 0;
  margin: 0 5% 0 0;
  color: #000000;
  font-weight: bold;
  text-decoration: none;
}

.connection:hover {
  color: #06b8f6;
}

@media (min-width: 320px) {
  .logo {
    margin: 2% 0;
    max-width: 35%;
  }

  .container-fluid {
    font-size: small;
  }

  button[type=button] {
    margin-top: 20%;
  }

  li span {
    font-size: xx-small;
  }

  .class_Meet {
    max-width: 55%;
    margin: 2% 2%;
  }

  input[type=search] {
    margin: 3% 0;
  }

  li button[type=submit] {
    font-size: xx-small;
  }

  .connection {
    margin: 5% 5%;
    font-size: xx-small;
  }
}

@media (min-width: 768px) {
  .container-fluid {
    font-size: medium;
  }

  button[type=button] {
    margin-top: 20%;
  }

  li span {
    font-size: small;
  }

  li button[type=submit] {
    font-size: small;
  }

  .connection {
    margin: 5% 5%;
    font-size: medium;
  }
}

@media (min-width: 1080px) {
  .logo {
    max-width: 35%;
  }

  button[type=button] {
    margin-top: 30%;
  }

  .container-fluid {
    font-size: medium;
  }

  li span {
    font-size: small;
  }

  .class_Meet {
    max-width: 45%;
    margin: 0 2%;
  }

  .connection {
    margin: 10% 5%;
  }

  input[type=search] {
    margin: 5% 0;
  }
}

@media (min-width: 1440px) {
  .logo {
    margin: 2.5% 0;
    max-width: 35%;
  }

  li span {
    font-size: medium;
  }

  button[type=button] {
    margin-top: 17%;
  }

  .class_Meet {
    max-width: 45%;
    margin: 2% 2%;
  }

  .connection {
    margin: 3.5% 5%;
  }

  input[type=search] {
    margin: 4% 0;
  }
}

@media (min-width: 2000px) {
  li a {
    font-size: 500%;
  }
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