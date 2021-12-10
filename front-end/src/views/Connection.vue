<template>
  <div class="connexion">
    <div class="container-fluid">
      <div class="row centered">
        <div class="col-12">
          <img
            class="
              img-fluid
              col-8 col-sm-2 col-md-3 col-lg-3 col-xl-3 col-xxl-3
            "
            alt="Vue logo"
            src="../assets/logo.png"
          />
        </div>
        <div class="row centered">
          <div class="col-12">
            <h1>{{ this[connectOrRegister].title }}</h1>
            <h1 class="msg_connexion">Class Meet</h1>
          </div>
        </div>
        <div class="row">
          <div class="col-12">
            <div class="centered_form">
              <Connexion v-if="isRegistered" />
              <Inscription v-else />
            </div>
          </div>
        </div>
        <div class="inscrire">
          <span style="font-weight: bolder; margin-right: 2%"
            >{{this[connectOrRegister].labelRegister}}
          </span>
          <a
            @click="registerPage"
            title="Inscription"
            class="btn btn-outline-primary mb-0"
            style="color: #06b8f6; border-color: #06b8f6"
            role="button"
            >{{this[connectOrRegister].buttonRegister}}</a
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Connexion from "../components/Connection_form.vue";
import Inscription from "../components/Inscription_form.vue";

export default {
  name: "Connection",
  components: {
    Connexion,
    Inscription,
  },
  computed: {
    connectOrRegister: function () {
      return this.isRegistered ? "connection" : "inscription"
    },
  },
  data: () => ({
    isRegistered: true,
    connection: {
      title: "Connectez-vous à ",
      labelRegister: "Première fois ?",
      buttonRegister: "Inscrivez-vous",
    },
    inscription: {
      title: "Inscrivez-vous à ",
      labelRegister: "Déjà un compte ?",
      buttonRegister: "Connectez-vous",
    },
  }),
  methods: {
    registerPage() {
      this.isRegistered = !this.isRegistered;
    },
  },
  beforeCreate() {
    if (this.$route.path === "/login") this.isRegistered = 1;
    else this.isRegistered = 0;
  },
};
</script>

<style scoped>

body {
  overflow-x: hidden;
}

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

  button[type="submit"] {
    font-size: small;
  }

  .centered_form {
    margin-left: 33%;
    margin-right: 33%;
  }

  span {
    font-size: small;
  }
  a[role="button"] {
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

  .centered_form {
    margin-left: 36%;
    margin-right: 36%;
  }

  span {
    font-size: large;
  }

  a[role="button"] {
    font-size: small;
  }
}

/* Medium devices (tablets, 768px and up) */
@media (min-width: 1024px) {
  h1 {
    font-size: 135%;
  }

  label {
    font-size: medium;
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

  span {
    font-size: large;
  }

  a[role="button"] {
    font-size: large;
  }
}

@media (min-width: 2000px) {
  h1 {
    font-size: 300%;
  }

  label {
    font-size: 150%;
  }

  button[type="submit"] {
    font-size: x-large;
  }
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
</style>
