<template>
  <div class="connexion">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12">
          <img class="img-fluid col-auto" alt="Vue logo" src="../assets/logo.png">
          <br>
          <h1>{{ msg }}</h1>
          <h1 class="msg_connexion">Class Meet</h1>
        </div>
      </div>
      <div class="row">
        <div class="col-xl-4 col-sm-3 col-md-3 col-xxl-6 col-lg-3"></div>
        <form action="login" class="col-6-5 col-xxl-4">
          <label class="form-label">Prénom :</label><br>
          <input type="text" class="form-control" name="first_name"/><br>
          <label class="form-label">Nom :</label><br>
          <input type="text" class="form-control" name="last_name"/><br>
          <label class="form-label">Adresse courriel :</label><br>
          <input type="text" class="form-control" name="username"/><br>
          <label class="form-label">Mot de passe :</label><br>
          <input type="password" class="form-control" name="password"/><br>
          <div class="col-auto">
          <span id="passwordHelpInline" class="form-text">
              Doit être de longueur 8-20 caractères.
            </span>
          </div>
          <button type="submit" title="Soumettre" class="rounded-pill col-auto" name="Soumettre" disabled>Soumettre
          </button>
        </form>
        <div class="col-2-5"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Connexion",
  props: {
    msg: String,
    msg2: String,
  }
}
</script>


<style scoped>

.row {
  text-align: center;
}

.col-0-5 {
  width: 5%;
}

.col-1-5 {
  width: 12.5%;
}

.col-2-5 {
  width: 20.83333%;
}

.col-3-5 {
  width: 29.16667%;
}

.col-sm-3-5 {
  width: 29.16667%;
}

.col-md-3-5 {
  width: 29.16667%;
}

.col-lg-3-5 {
  width: 29.16667%;
}

.col-4-5 {
  width: 37.5%;
}

.col-5-5 {
  width: 45.83333%;
}

.col-6-5 {
  width: 54.16667%;
}

.col-7-5 {
  width: 62.5%;
}

.col-8-5 {
  width: 70.83333%;
}

.col-9-5 {
  width: 79.16667%;
}

.col-10-5 {
  width: 87.5%;
}

.col-11-5 {
  width: 95.8333%;
}

@media (min-width: 768px) {
  .col-md-3 {
    width: 32%;
  }
}

@media (min-width: 1400px) {
  .col-xxl-4 {
    width: 40%
  }

  .col-xxl-6 {
    width: 37%
  }
}


@media (min-width: 2560px) {
  .col-xxl-4 {
    width: 35%;
  }

  .col-xxl-6 {
    width: 40%
  }
}

.img-fluid {
  max-width: 40%;
  height: auto;
}

.msg_connexion {
  text-align: center;
  color: #06b8f6;
}

h1 {
  display: inline;
}

button:hover {
  opacity: 70%;
}

button:disabled {
  opacity: 50%;
}

form {
  margin-top: 2%;
  text-align: left;
  font-family: Sen, "Times New Roman", serif;
  font-size: 120%;
  font-weight: bold;
}

input[type=text] {
  display: inline-block;
  width: 100%;
  max-width: 60%;
  margin: 0 1% 1% 0;
  padding: 0.3%;
  text-align: left;
  border: 3px groove black;
  border-radius: 5px;
  color: black;
  background: white;
}

input[type=password] {
  display: inline-block;
  width: 100%;
  max-width: 60%;
  margin: 0 1% 1% 0;
  padding: 0.3%;
  text-align: left;
  border: 3px solid black;
  border-radius: 5px;
  color: black;
  background: white;
}

button[type=submit] {
  width: 100%;
  max-width: 20%;
  margin: 3% 0 1% 15%;
  padding: 2.5%;
  border: none;
  background-color: #87ceeb;
  color: black;
  cursor: pointer;
  box-sizing: content-box;
  font-size: large;
  text-align: center;
  font-weight: bolder;
}

</style>