<template>
  <div class="connexion">
    <div class="container-fluid">
      <div class="row centered">
        <div class="col-12">
          <img class="img-fluid col-8 col-sm-2 col-md-2 col-lg-3 col-xl-3 col-xxl-3" alt="Vue logo"
               src="../assets/logo.png">
        </div>
        <div class="row centered">
          <div class="col-12">
            <h1>{{ msg }}</h1>
            <h1 class="msg_connexion">Class Meet</h1>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <div class="centered_form">
            <form action="login">

              <label class="form-label">Adresse courriel :</label><br>
              <input type="text" v-model="email" class="form-control w-100 h-auto" name="username"/><br>
              <label class="form-label">Mot de passe :</label><br>
              <input type="password" v-model="password" class="form-control w-100 h-auto" name="password"/>
              <p class="forgot-pw">Mot de passe oublié</p>

              <div class="centered text-center">
                <button type="submit" @click="connection" title="Soumettre"
                        class="rounded-pill w-30 h-20" name="submit"
                      >Soumettre
                </button>
              </div>

            </form>
          </div>
        </div>
      </div>
      <div class="inscrire">
        <span style="font-weight: bolder; margin-right: 2%">Première fois ? </span>
        <a href="#" title="Inscription" class="btn btn-outline-primary" style="color: #06b8f6; border-color: #06b8f6;"
           role="button">Inscrivez-vous</a>
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
        body: JSON.stringify({email: this.email, password: this.password}),
      })
        .then((res) => res.json())
        .then((data) => {
          this.$store.commit("connect", data)
          this.$router.push("/")
        }).catch(err => {
          console.error(err)
        });
    },
  },
};

</script>

<style scoped>

.centered {
  display: flex;
  align-items: center;
  justify-content: center;
}

.centered_form {
  display: block;
  margin-left: 30%;
  margin-right: 30%;
  align-items: center;
  justify-content: center;
}

.connexion {
  margin-bottom: 10%;
}

.row {
  text-align: center;
}


.img-fluid {
  max-width: 40%;
  height: auto;
}

.msg_connexion {
  margin-top: 2%;
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
  margin-top: 5%;
  text-align: left;
  font-family: Sen, "Times New Roman", serif;
  font-size: 120%;
  font-weight: bold;
}

input[type=text] {
  display: inline-block;
  max-width: 100%;
  margin: 0 auto 3% auto;
  padding: 0.3%;
  text-align: left;
  border: 3px groove black;
  border-radius: 5px;
  color: black;
  background: white;
}

input[type=password] {
  display: inline-block;
  max-width: 100%;
  margin: 0 auto 3% auto;
  padding: 0.3%;
  text-align: left;
  border: 3px solid black;
  border-radius: 5px;
  color: black;
  background: white;
}

.forgot-pw {
  margin: 0;
  text-decoration-line: underline;
  font-size: medium;
}

button[type=submit] {
  max-width: 100%;
  margin: 10% 0;
  padding: 10% 20%;
  border: none;
  background-color: #87ceeb;
  color: black;
  cursor: pointer;
  text-align: center;
  font-size: large;
  font-weight: bolder;
}

.inscrire {
  position: center;
  margin: 2% auto 0 auto;
  max-width: 50%;
  align-content: center;
  text-align: center;
  color: #06b8f6;
  border-color: #06b8f6;
  border-width: 2px;
  font-weight: bolder;
  font-size: large;
}

/* Extra small devices (phones, less than 768px) */
@media (min-width: 320px) {
  h1 {
    font-size: 90%;
    font-weight: bolder;
  }

  label {
    font-size: x-small;
    margin-bottom: 0;
  }

  .forgot-pw {
    font-size: xx-small;
  }

  button[type=submit] {
    padding: 10% 15%;
    font-size: small;
    text-align: center;
  }

  .centered_form {
    margin-left: 33%;
    margin-right: 33%;
  }

  span {
    font-size: small;
  }

  button[type=submit] {
    font-size: small;
  }

  a[role=button] {
    font-size: small;
  }
}

/* Extra small devices (tablets, 768px and up) */
@media (min-width: 768px) {
  h1 {
    font-size: 125%;
  }

  label {
    font-size: medium;
    margin-bottom: 0;
  }

  .forgot-pw {
    font-size: small;
  }

  button[type=submit] {
    font-size: medium;
  }

  .centered_form {
    margin-left: 36%;
    margin-right: 36%;
  }

}

/* Medium devices (tablets, 768px and up) */
@media (min-width: 1080px) {
  h1 {
    font-size: 150%;
  }

  label {
    font-size: large;
  }

  .centered_form {
    margin-left: 38%;
    margin-right: 38%;
  }

}

/* Large devices (large desktops, 1200px and up) */
@media (min-width: 1400px) {
  h1 {
    font-size: 175%;
  }

  .centered_form {
    margin-left: 40%;
    margin-right: 40%;
  }

  label {
    font-size: large;
  }

  .forgot-pw {
    font-size: medium;
  }

  span {
    font-size: large;
  }

  a[role=button] {
    font-size: large;
  }
}

@media (min-width: 2000px) {
  h1 {
    font-size: 500%;
  }

  label {
    font-size: 200%;
  }
}

</style>
