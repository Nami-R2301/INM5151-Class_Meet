<template>
  <form action="/login" class="col-6 col-sm-4 col-md-4 col-lg-4 col-xl-3 col-xxl-3 mt-3 text-start mx-auto">
    <p v-if="this.error_backend.length === 0" style="color: red; font-size: 1.10rem; font-weight: bold">{{
        error_email
      }}</p>
    <p v-else style="color: red; font-size: 1.10rem; font-weight: bold">{{ error_backend }}</p>
    <label class="form-label fw-bold mb-2 mx-auto fs-5">Adresse courriel :</label>
    <input
        type="email"
        @focusout="validate_email"
        v-model="email"
        class="form-control  py-1 px-3 rounded-pill border-3 mb-4 fs-5"
        name="email"
        id="email"
    />
    <p style="color: red; font-size: 1.10rem; font-weight: bold">{{ error_username }}</p>
    <label class="form-label fw-bold mx-auto fs-5">Nom d'utilisateur :</label>
    <input
        type="text"
        @focusout="validateUsername"
        v-model="username"
        class="form-control  py-1 px-3 rounded-pill border-3 mb-4 fs-5"
        name="username"
        id="username"
    />
    <p style="color: red; font-size: 1.10rem; font-weight: bold">{{ error_pw }}</p>
    <label class="form-label fw-bold mb-2 mx-auto fs-5">Mot de passe :</label>
    <input
        type="password"
        @focusout="validate_pw"
        v-model="password"
        class="form-control py-1 px-3 rounded-pill border-3 mb-4 fs-5"
        name="password"
        id="password"
    />
    <p style="color: red; font-size: 1.10rem; font-weight: bold">{{ error_confirm_pw }}</p>
    <label class="form-label fw-bold mb-2 mx-auto fs-5">Confirmer le mot de passe :</label>
    <input
        type="password"
        @focusout="validate_confirm_pw"
        v-model="confirmPassword"
        class="form-control  py-1 px-3 rounded-pill border-3 mb-4 fs-5"
        name="confirmPassword"
        id="confirmPassword"
    />

    <div class="centered text-center">
      <button
          type="submit"
          @click="signup"
          title="Soumettre"
          class="btn btn-outline-primary shadow rounded-pill text-center px-5 py-4 fw-bold my-4 mx-auto"
          name="submit"
          id="submit"
      >
        Soumettre
      </button>
    </div>
  </form>
</template>

<script>
import connection from "../views/Connection";

export default {
  name: "sign-up-form",
  data: () => ({
    email: "",
    username: "",
    password: "",
    confirmPassword: "",
    error_email: "",
    error_username: "",
    error_pw: "",
    error_confirm_pw: "",
    error_backend: "",
  }),
  mounted() {
    this.validate_form();
  },
  methods: {
    validate_email() {
      this.error_email = connection.check_email(this.email)
      if (this.error_email.length > 1) document.getElementById("email").style.borderColor = "red"
      else {
        document.getElementById("email").style.borderColor = "#2b2b2b"
        this.error_backend = "";
      }
      this.validate_form()
    },
    validateUsername() {
      this.error_username = connection.check_username(this.username)
      if(this.error_username.length > 1) document.getElementById("username").style.borderColor = "red"
      else {
        document.getElementById("username").style.borderColor = "#2b2b2b"
        this.error_backend = "";
      }
      this.validate_form()
    },
    validate_pw() {
      this.error_pw = connection.check_password(this.password)
      if (this.error_pw.length > 1) document.getElementById("password").style.borderColor = "red"
      else {
        document.getElementById("password").style.borderColor = "#2b2b2b"
        this.error_backend = "";
      }
      this.validate_form()
    },
    validate_confirm_pw() {
      this.error_confirm_pw = connection.check_confirm_pw(this.password, this.confirmPassword)
      if (this.error_confirm_pw.length > 1) document.getElementById("confirmPassword").style.borderColor = "red"
      else {
        document.getElementById("confirmPassword").style.borderColor = "#2b2b2b"
        this.error_backend = "";
      }
      this.validate_form()
    },
    validate_form() {
      document.getElementById('submit').disabled = this.email.length === 0 ||
          this.password.length === 0 || this.username.length === 0 ||
          this.confirmPassword.length === 0 || this.error_email.length !== 0 || this.error_pw.length !== 0 ||
          this.error_username.length !== 0 || this.error_confirm_pw.length !== 0 || this.error_backend.length !== 0;
    },
    signup(e) {
      e.preventDefault();
      this.validate_email(this.email)
      this.validate_pw(this.password)
      this.validateUsername()
      this.validate_confirm_pw()
      if (this.error_pw.length === 0 && this.error_email.length === 0) {

        fetch(`${this.$store.getters.baseUrlBackEnd}api/register`, {
          method: "POST",
          body: JSON.stringify({
            email: this.email,
            username: this.username,
            password: this.password,
          }),
        })
            .then((res) => res.json())
            .then((data) => {
              if (data.err) {
                this.error_backend = "Cette adresse courriel est déjà associé à un compte Class Meet !";
                this.validate_form();
              } else {
                this.$cookies.set("user", data);
                this.$router.push("/profile");
              }
            })
            .catch((err) => {
              console.error(err);
            });
      }
    },
  }
};
</script>

<style scoped>
.fs-5 {
  font-size: 1.15rem !important;
}

.form-control {
  border-color: #2b2b2b;
}

</style>