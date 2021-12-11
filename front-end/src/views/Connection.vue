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
          <div class="col-12 mt-4">
            <h1 class="fw-bold">{{ this[connectOrRegister].title }}</h1>
            <h1 class="msg_connexion fs-2 text-responsive fw-bold">Class Meet</h1>
          </div>
        </div>
        <div class="row">
          <div class="col-12 mt-2 fs-6">
            <Connexion v-if="isRegistered"/>
            <Inscription v-else/>
          </div>
        </div>
        <div class="text-center fw-bold mx-auto mt-4 text-info fs-5">
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
import Connexion from "../components/sign-in-form.vue";
import Inscription from "../components/sign-up-form.vue";

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
      email: "",
      pw: "",
    },
    inscription: {
      title: "Inscrivez-vous à ",
      labelRegister: "Déjà un compte ?",
      buttonRegister: "Connectez-vous",
      email: "",
      name: "",
      pw: "",
      confirm_password: "",
    },
  }),
  methods: {
    registerPage() {
      this.isRegistered = !this.isRegistered;
    },

  },
  mounted() {
    let validator_sign_in = document.createElement('script')
    validator_sign_in.setAttribute('src', '../store/onSubmit_sign_in.js')
    document.head.appendChild(validator_sign_in)
    let validator_sign_up = document.createElement('script')
    validator_sign_up.setAttribute('src', '../store/onSubmit_sign_up.js')
    document.head.appendChild(validator_sign_up)
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

  .sign-up-pic.col-xxl-2 {
    width: 15% !important;
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
