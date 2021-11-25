<template>
  <nav class="container-fluid navbar-nav m-lg-auto navbar-light bg-light sticky-md-top">
    <ul class="row">
      <li class="col-1 align-content-start">
        <img class="accessibility" src="../assets/icon-menu.png" alt="Icone de menu deroulant">
      </li>
      <li class="col-2 col-sm-3 col-md-3 col-lg-3 col-xl-2 col-xxl-2">
        <a href="Connexion.vue"
           title="Cliquez ici pour revenir à la page principale">
          <img class="logo" alt="logo Class Meet" src="../assets/logo.png">
          <img class="class_Meet" alt="Class Meet" src="../assets/Class_Meet.png"></a>
      </li>
      <li class="col-4 col-sm-5 col-md-5 col-lg-5 col-xl-4 col-xxl-4">
        <form class="d-flex justify-content-sm-start">
          <input class="form-control" type="search" placeholder="Rechercher des programmes"
                 aria-label="Rechercher">
          <button class="btn btn-outline-success" type="submit">Rechercher</button>
        </form>
      </li>
      <li class="col-5 col-sm-3 col-md-3 col-lg-3 col-xl-5 col-xxl-5 justify-content-end">
        <a class="connection" href="Connexion.vue"
           title="Connectez-vous">Connectez-vous</a>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "Barre_de_navigation",
}
</script>

<style>

.connection {
  float: right;
  margin: 2% 5%;
  color: #000000;
  font-weight: bold;
  text-decoration: none;
}

.connection:hover {
  color: #06b8f6;
}

@media (min-width: 260px) {
  .logo {
    max-width: 35%;
  }

  .class_Meet {
    max-width: 55%;
    margin: 0 2%;
  }

  .accessibility {
    margin: 10% 0;
    max-width: 55%;
  }

  input[type=search] {
    margin: 1% 0;
  }

  .connection {
    margin: 5% 5%;
  }
}

@media (min-width: 1080px) {
  .logo {
    max-width: 35%;
  }

  .class_Meet {
    max-width: 45%;
    margin: 0 2%;
  }

  .accessibility {
    margin: 7.5% 0;
    max-width: 30%;
  }

  .connection {
    margin: 2.5% 5%;
  }
}

@media (min-width: 1440px) {
  .logo {
    max-width: 35%;
  }

  .class_Meet {
    max-width: 45%;
    margin: 0 2%;
  }

  .accessibility {
    margin: 7.5% 0;
    max-width: 30%;
  }

  .connection {
    margin: 2.5% 5%;
  }
}

.container-fluid {
  display: inline-block;
}

.row {
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