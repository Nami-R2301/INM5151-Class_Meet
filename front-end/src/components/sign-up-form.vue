<template>
  <form action="/login" class="col-6 col-sm-4 col-md-4 col-lg-4 col-xl-3 col-xxl-3 mt-3 text-start mx-auto">
    <p v-if="this.error_backend.length === 0" style="color: red; font-size: 1.10rem; font-weight: bold">{{
        error_email
      }}</p>
    <p v-else-if="this.error_backend.length !== 0" style="color: red; font-size: 1.10rem; font-weight: bold">
      {{ error_backend }}</p>
    <p class="valid-feedback" style="color: green; font-size: 1.10rem; font-weight: bold">{{ this.confirm_email }}</p>
    <label class="form-label fw-bold mb-2 mx-auto">Adresse courriel :</label>
    <b-form-input
        type="email"
        :state="checkEmail"
        v-model="email"
        placeholder="Ex: *****.****@gmail.com"
        class="form-control rounded-pill border-2 mb-4"
        name="email"
        id="email"
    />
    <p style="color: red; font-size: 1.10rem; font-weight: bold">{{ error_username }}</p>
    <label class="form-label fw-bold mx-auto">Nom d'utilisateur :</label>
    <b-form-input
        type="text"
        :state="checkUsername"
        v-model="username"
        class="form-control rounded-pill border-2 mb-4"
        name="username"
        id="username"
    />
    <p style="color: red; font-size: 1.10rem; font-weight: bold">{{ error_pw }}</p>
    <label class="form-label fw-bold mb-2 mx-auto">Mot de passe :</label>
    <b-form-input
        type="password"
        :state="checkPw"
        v-model="password"
        placeholder="Au moins 1 caractère"
        class="form-control rounded-pill border-2 mb-4"
        name="password"
        id="password"
    />
    <p style="color: red; font-size: 1.10rem; font-weight: bold">{{ error_confirm_pw }}</p>
    <label class="form-label fw-bold mb-2 mx-auto">Confirmer le mot de passe :</label>
    <b-form-input
        type="password"
        :state="checkConfirmPw"
        v-model="confirmPassword"
        class="form-control rounded-pill border-2 mb-4"
        name="confirmPassword"
        id="confirmPassword"
    />

    <div class="centered text-center">
      <button
          type="submit"
          @click="signup"
          title="Soumettre"
          class="btn btn-outline-primary text-break rounded-pill border-3 text-center col-sm-9 col-lg-6 py-4 fw-bold my-4 mx-auto"
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
  props: {
    error_username: String,
    error_pw: String,
    error_confirm_pw: String,
  },
  computed: {
    checkEmail() {
      let valide = null
      if (this.error_backend.length > 0) valide = false
      else if (this.email !== this.copy_email) valide = this.validate_email().length === 0;
      else if (this.email.length > 0) valide = this.confirm_email.length > 0
      if (document.getElementById('submit') !== null) this.validate_form()
      return valide
    },
    checkUsername() {
      let valide = null
      if (this.username.length !== 0) valide = connection.check_username(this.username).length === 0
      if (document.getElementById('submit') !== null) this.validate_form()
      return valide
    },
    checkPw() {
      let valide = null
      if (this.password.length !== 0) valide = connection.check_password(this.password).length === 0
      if (document.getElementById('submit') !== null) this.validate_form()
      return valide
    },
    checkConfirmPw() {
      let valide = null
      if (this.password.length !== 0 && this.confirmPassword.length !== 0) {
        valide = connection.check_confirm_pw(this.password, this.confirmPassword).length === 0
      } else if (this.password.length === 0 && this.confirmPassword.length !== 0) valide = false
      if (document.getElementById('submit') !== null) this.validate_form()
      return valide
    }
  },
  data: () => ({
    email: "",
    copy_email: "",
    confirm_email: "",
    username: "",
    password: "",
    confirmPassword: "",
    error_email: "",
    error_backend: "",
  }),
  mounted() {
    this.validate_form();
  },
  methods: {
    validate_email() {
      this.confirm_email = ""
      this.copy_email = this.email
      this.error_email = connection.check_email(this.email)
      if (this.email.length > 0 && this.error_email.length === 0) {
        this.error_backend = "";
        fetch(`${this.$store.getters.baseUrlBackEnd}api/checkEmail`, {
          method: "POST",
          body: JSON.stringify({
            email: this.email,
          }),
        })
            .then((res) => res.json())
            .then((data) => {
              if (data.err) this.confirm_email = "Cette adresse courriel est libre !"
            })
            .catch((err) => {
              console.error(err);
              this.error_email = "Cette adresse courriel est déjà associé à un compte Class Meet !";
            });
      }
      return this.error_email
    },
    validate_form() {
      document.getElementById('submit').disabled = this.email.length === 0 ||
          this.password.length === 0 || this.username.length === 0 ||
          this.confirmPassword.length === 0 || this.confirm_email.length === 0 || this.error_username === null
          || this.error_pw === null || this.error_confirm_pw === null || this.password !== this.confirmPassword
    },
    signup(e) {
      e.preventDefault();

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
              document.getElementById('submit').disabled = true;
            } else {
              this.$store.dispatch("connection")
              this.$cookies.set("user", data);
              this.$router.push("/profile");
            }
          })
          .catch((err) => {
            console.error(err);
          });
    },
  }
};
</script>

<style scoped>

.form-control {
  border-color: var(--bs-orange);
}

.form-control.is-valid, .was-validated .form-control:valid {
  border-color: #198754;
}
.form-control.is-invalid, .was-validated .form-control:invalid {
  border-color: #dc3545;
  border-width: 3px!important;
}
</style>