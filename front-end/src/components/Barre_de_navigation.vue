<template>
  <div id="barre-nav" class="Barre_de_navigation">
    <nav class="container-fluid navbar-nav m-auto navbar-light bg-light sticky-md-top">
      <ul class="row flex-nowrap" style="background-color: rgb(230,237,248); padding-left: 2%">
        <li class="col-1 col-sm-1 col-md-1 col-lg-1 col-xl-1 col-xxl-1 align-content-start">
          <button type="button" class="navbar-toggler py-0 px-0 mx-2 my-2 my-md-3" data-bs-target="#collapsibleNavbar" aria-expanded="false"
                  aria-controls="collapseNavbar">
            <span class="navbar-toggler-icon px-0 py-0 my-xxl-1"></span>
          </button>
        </li>
        <li class="col-4 col-sm-3 col-md-3 col-lg-3 col-xl-3 col-xxl-2 align-content-center">
          <a class="navbar-brand my-auto" href="/"
             title="Cliquez ici pour revenir à la page principale">
            <img class="logo offset-1 my-2 my-sm-2 my-lg-1 my-xl-3 my-xxl-2" alt="logo Class Meet" src="../assets/logo.png">
            <img class="class_Meet my-3 my-xl-4" alt="Class Meet" src="../assets/Class_Meet.png"></a>
        </li>
        <li class="col-4 col-sm-5 col-md-5 col-lg-5 col-xl-5 col-xxl-4">
          <form class="d-flex justify-content-sm-start my-1">
            <input class="form-control py-1 my-2 my-xl-2 my-xxl-3" type="search" placeholder="Rechercher des programmes"
                   aria-label="Rechercher">
            <button class="btn btn-outline-success col-4 col-sm-5 col-md-5 col-lg-5 col-xl-2 col-xxl-4 py-1 my-2"
                    type="submit">Rechercher
            </button>
          </form>
        </li>
        <li class="col-3 col-sm-3 col-md-3 col-lg-3 col-xl-3 col-xxl-5 nav-item">
          <a class="nav-link active connection my-1 my-sm-2 my-lg-2 my-xxl-3" href="/login"
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

.logo {
  max-width: 30%;
}

.class_Meet {
  max-width: 40%;
}


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

  .container-fluid {
    font-size: small;
  }

  li span {
    font-size: xx-small;
  }

  li button[type=submit] {
    font-size: 5px;
    max-width: 5%;
  }

  input[type=search] {
    font-size: 2%;
  }

  .connection {
    font-size: 5%;
  }

}

@media (min-width: 768px) {
  .container-fluid {
    font-size: medium;
  }

  li span {
    font-size: small;
  }

  li button[type=submit] {
    font-size: small;
    max-width: 30%;
  }

  input[type=search] {
    font-size: small;
  }

  .connection {
    font-size: small;
  }
}

@media (min-width: 1024px) {
  .container-fluid {
    font-size: medium;
  }

  li span {
    font-size: small;
  }

  li button[type=submit] {
    font-size: small;
    max-width: 30%;
  }

  input[type=search] {
    font-size: small;
  }

  .connection {
    font-size: small;
  }

}

@media (min-width: 1440px) {

  li span {
    font-size: medium;
  }

  input[type=search] {
    font-size: large;
  }
}

@media (min-width: 2000px) {

  input[type=search] {
    font-size: xx-large;
  }

  li span {
    font-size: xx-large;
  }

  li button[type=submit] {
    font-size: xx-large;
    max-width: 25%;
  }

  .connection {
    font-size: xx-large;
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