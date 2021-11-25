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
          <input type="text" v-model="email" class="form-control" name="username"/><br>
          <label class="form-label">Mot de passe :</label><br>
          <input type="password" v-model="password" class="form-control" name="password"/><br>
          <div class="col-auto">
          <span id="passwordHelpInline" class="form-text">
              Doit être de longueur 8-20 caractères.
            </span>
          </div>
          <button type="submit" @click="connection" title="Soumettre" class="rounded-pill col-auto" name="submit" disabled>Soumettre
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
  },
   data: () => ({
    email: "",
    password: "",
  }),
  methods: {
    connection(e) {
      e.preventDefault();
      fetch(`${this.$store.getters.baseUrlBackEnd}api/connection`, {
        method: "POST",
        body: JSON.stringify({ email: this.email, password: this.password }),
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
        }).catch(err => {
          console.error(err)
        });
    },
  },
};

</script>

<style scoped>

.row {
  text-align: center;
}

.col-2-5 {
  width: 20.83333%;
}


.col-6-5 {
  width: 54.16667%;
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
