<template>
  <div class="connexion mx-auto">
    <div class="container-fluid">
      <div class="row centered text-center">
        <div class="col-12">
          <img
              v-if="isRegistered"
              class="
              img-fluid
              col-4 col-xl-3 col-xxl-2 mt-2"
              alt="Vue logo"
              src="../assets/logo.png"
          />
          <img v-else class="img-fluid sign-up-pic
              col-3 col-xl-2 col-xxl-2 mt-2"
               alt="Ajout utilisateur."
               src="../assets/add-user.png"
          />
        </div>
        <div class="row centered">
          <div class="col-6 mt-4 px-0">
            <h1 class="fw-bold text-responsive">{{ this[connectOrRegister].title }}</h1>
            <h1 class="msg_connexion fs-2 text-responsive fw-bold">Class Meet</h1>
          </div>
        </div>
        <div class="row">
          <div class="col-12 mt-2 fs-6">
            <SignInForm v-if="isRegistered"/>
            <SignUpForm v-else/>
          </div>
        </div>
        <div class="text-center fw-bold m-auto my-4 text-info fs-5">
          <span class="me-4"
          >{{ this[connectOrRegister].labelRegister }}
          </span>
          <a
              @click="registerPage"
              title="Inscription"
              class="btn btn-outline-info m-auto rounded-pill px-4 fs-5"
              role="button"
          >{{ this[connectOrRegister].buttonRegister }}</a
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SignInForm from "../components/sign-in-form.vue";
import SignUpForm from "../components/sign-up-form.vue";

export default {
  name: "Connection",
  components: {
    SignUpForm,
    SignInForm,
  },
  computed: {
    connectOrRegister: function () {
      return this.isRegistered ? "SignInForm" : "SignUpForm"
    },
  },
  data: () => ({
    isRegistered: true,
    SignInForm: {
      title: "Connectez-vous à ",
      labelRegister: "Première fois ?",
      buttonRegister: "Inscrivez-vous",
      email: "",
      error_email: "",
      error_pw: "",
      pw: "",
    },
    SignUpForm: {
      title: "Inscrivez-vous à ",
      labelRegister: "Déjà un compte ?",
      buttonRegister: "Connectez-vous",
      email: "",
      name: "",
      pw: "",
      confirm_password: "",
      error_email: "",
      error_pw: "",
      error_username: "",
      error_confirm_pw: "",
    },
  }),
  methods: {
    registerPage() {
      this.isRegistered = !this.isRegistered;
    },
  },
  check_email(email) {
    const reg_email = new RegExp('\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b');
    this.error_email = "";
    let msgE2 = "\tL'adresse courriel saisie n'est pas une adresse de format valide !";

    if (email.toString().match(reg_email) === null || email.length < 4) {
      console.log("Email not valid!\n");
      this.error_email = msgE2;
    }
    return this.error_email
  },
  check_username(username) {
    this.error_username = "";
    let msgE = "\tLe nom d'utilisateur saisi n'est pas un nom valide !";
    if(username === "") {
      console.log("Username is not valid!\n");
      this.error_username = msgE;
    }
    return this.error_username;
  },
  check_password(pw) {
    this.error_pw = "";
    let msgE = "\tLe mot de passe ne peut être laissé vide !";
    if (pw === "") {
      console.log("Pw not valid!\n");
      this.error_pw = msgE;
    }
    return this.error_pw;
  },
  check_confirm_pw(pw, confirm_pw) {
    this.error_confirm_pw = "";
    let msgE = "\tCe mot de passe n'est pas identique au mot de passe saisi dans le champ précédent !";
    if (confirm_pw === "" || confirm_pw !== pw) {
      console.log("Confirm_pw is not valid!\n")
      this.error_confirm_pw = msgE;
    }
    return this.error_confirm_pw;
  },
  beforeCreate() {
    if (this.$route.path === "/login") this.isRegistered = 1;
    else this.isRegistered = 0;
  },
};
</script>

<style scoped>

.centered {
  display: flex;
  align-items: center;
  justify-content: center;
}

.msg_connexion {
  color: #06b8f6;
}

h1 {
  font-size: 1.70rem !important;
  display: inline;
}

img {
  -webkit-filter: drop-shadow(3px 3px 3px #2b2b2b);
  filter: drop-shadow(3px 3px 3px #2b2b2b);
}

.fs-5 {
  font-size: 1.15rem !important;
}

@media (min-width: 1440px) {

  img.col-xxl-2 {
    width: 20% !important;
  }

}

button:hover {
  opacity: 70%;
}

button:disabled {
  opacity: 50%;
}

.text-responsive {
  font-size: calc(100% + 1vw + 1vh);
}


</style>
