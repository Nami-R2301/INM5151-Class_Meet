<template>
  <div class="connexion">
    <img class="img-fluid" alt="Vue logo" src="../assets/logo.png">
    <div class="container-fluid">
      <div class="text-center mt-3">
        <h1>{{ msg }}</h1>
        <h1 class="msg_connexion">Class Meet</h1>
      </div>
      <div class="row justify-content-lg-center">
        <form action="login">
          <div class="col-lg-6"><label>Adresse courriel :</label><br></div>
          <div class="col-lg-6"><input type="text" name="username"/><br></div>
          <div class="col-lg-6"><label>Mot de passe :</label><br></div>
          <div class="col-lg-6"><input type="password" name="password"/><br></div>
          <div class="col-lg-6"><input type="submit" name="Soumettre"/></div>
        </form>
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

.img-fluid {
  max-width: 40%;
  height: auto;
}

.msg_connexion {
  color: #87ceeb;
}

h1 {
  display: inline;
}

.connexion {
  margin-top: 5%;
}

form {
  margin-top: 2%;
  margin-left: 37%;
  position: relative;
  text-align: left;
  font-family: Sen, "Times New Roman", serif;
  font-size: 120%;
  font-weight: bold;
}

label {
  margin-left: 1%;
  text-align: left;
}

input[type=text] {
  display: inline-block;
  max-width: 50%;
  width: 40%;
  margin: 1% 1%;
  padding: 0.3%;
  text-align: left;
  border: 3px solid black;
  border-radius: 5px;
  color: black;
  background: white;
}

input[type=password] {
  display: inline-block;
  max-width: 50%;
  width: 40%;
  margin: 1% 1%;
  padding: 0.3%;
  text-align: left;
  border: 3px solid black;
  border-radius: 5px;
  color: black;
  background: white;
}

input[type=submit] {
  width: 15%;
  margin: 1% 0 1% 13.5%;
  padding: 1%;
  border: none;
  border-radius: 4px;
  background-color: #87ceeb;
  color: black;
  cursor: pointer;
  box-sizing: content-box;
  font-size: large;
  font-weight: bolder;
}

</style>