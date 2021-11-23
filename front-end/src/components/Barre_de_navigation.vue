<template>
  <nav class="navbar navbar-expand-md navbar-light bg-light sticky-md-top">
      <ul class="container-fluid justify-content-md-start">
        <li class="navbar-brand">
            <img src="../assets/icon-menu.png" class="accessibility" alt="Icone de menu deroulant">
        </li>
        <li class="nav-item">
          <a class="nav-link active col-md-4" href="Connexion.vue"
             title="Cliquez ici pour revenir à la page principale">
            <img class="logo" alt="logo Class Meet" src="../assets/logo.png">
            <img class="class_Meet" alt="Class Meet" src="../assets/Class_Meet.png"></a>
          <form class="d-flex">
            <input class="form-control me-2 col-md-2" type="search" placeholder="Rechercher des programmes"
                   aria-label="Rechercher">
            <button class="btn btn-outline-success" type="submit">Rechercher</button>
          </form>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="Connexion.vue"
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

li {
  margin: 0 auto;
  height: auto;
  padding: 0 1.2%;
  text-align: left;
  list-style-type: none;
}

.accessibility {
  max-width: 10%;
  height: auto;
  padding-left: 1%;
  text-align: left;
}

.accessibility:hover {
  opacity: 50%;
}

.logo {
  width: 30%;
  margin: 0 2%;
  height: auto;
}

.class_Meet {
  width: 40%;
  height: auto;
  margin: 0 auto;
}

a:hover {
  opacity: 50%;
  color: cyan;
}
</style>