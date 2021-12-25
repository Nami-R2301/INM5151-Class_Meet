<template>
  <form action="/login" class="col-6 col-sm-4 col-md-4 col-lg-4 col-xl-3 col-xxl-3 mt-3 text-start mx-auto">
    <p v-if="this.error_backend.length === 0" style="color: red; font-size: 1.10rem; font-weight: bold">{{
        error_email
      }}</p>
    <p v-else-if="this.error_backend.length !== 0" style="color: red; font-size: 1.10rem; font-weight: bold">
      {{ error_backend }}</p>
    <p style="color: green; font-size: 1.10rem; font-weight: bold">{{ this.confirm_email }}</p>
    <label class="form-label fw-bold mb-2 mx-auto">Adresse courriel :</label>
    <b-form-input
        type="email"
        :state="checkEmail"
        v-model="email"
        class="form-control  py-1 px-3 rounded-pill border-3 mb-4"
        name="email"
        id="email"
    />
    <p style="color: red; font-size: 1.10rem; font-weight: bold">{{ error_username }}</p>
    <label class="form-label fw-bold mx-auto">Nom d'utilisateur :</label>
    <b-form-input
        type="text"
        :state="checkUsername"
        v-model="username"
        class="form-control py-1 px-3 rounded-pill border-3 mb-4"
        name="username"
        id="username"
    />
    <p style="color: red; font-size: 1.10rem; font-weight: bold">{{ error_pw }}</p>
    <label class="form-label fw-bold mb-2 mx-auto">Mot de passe :</label>
    <b-form-input
        type="password"
        :state="checkPw"
        v-model="password"
        class="form-control py-1 px-3 rounded-pill border-3 mb-4"
        name="password"
        id="password"
    />
    <p style="color: red; font-size: 1.10rem; font-weight: bold">{{ error_confirm_pw }}</p>
    <label class="form-label fw-bold mb-2 mx-auto">Confirmer le mot de passe :</label>
    <b-form-input
        type="password"
        :state="checkConfirmPw"
        v-model="confirmPassword"
        class="form-control  py-1 px-3 rounded-pill border-3 mb-4"
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
      if (this.email.length === 0 || document.getElementById('email').style.borderColor === "green") return
      return this.validate_email() && this.validate_form()
    },
    checkUsername() {
      if (this.username.length === 0) return
      return connection.check_username(this.username).length === 0 && this.validate_form()
    },
    checkPw() {
      if (this.password.length === 0) return
      return connection.check_password(this.password).length === 0 && this.validate_form()
    },
    checkConfirmPw() {
      if (this.confirmPassword.length === 0) return
      return connection.check_confirm_pw(this.password, this.confirmPassword).length === 0 && this.validate_form()
    }
  },
  data: () => ({
    email: "",
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
      this.error_email = ""
      if (connection.check_email(this.email).length > 0) {
        document.getElementById("email").style.borderColor = "red"
      } else if(document.getElementById("email").style.borderColor !== "green") {
        document.getElementById("email").style.borderColor = "#2b2b2b"
        this.error_backend = "";
        fetch(`${this.$store.getters.baseUrlBackEnd}api/checkEmail`, {
          method: "POST",
          body: JSON.stringify({
            email: this.email,
          }),
        })
            .then((res) => res.json())
            .then((data) => {
              if (data.err) {
                this.confirm_email = "Cette adresse courriel est libre !"
                document.getElementById('email').style.borderColor = "green"
              }
            })
            .catch((err) => {
              console.error(err);
              this.error_email = "Cette adresse courriel est déjà associé à un compte Class Meet !";
              document.getElementById("email").style.borderColor = "red"
            });
      }
    },
    validate_form() {
      document.getElementById('submit').disabled = this.email.length === 0 ||
          this.password.length === 0 || this.username.length === 0 ||
          this.confirmPassword.length === 0 || document.getElementById('email').style.borderColor !== "green"
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
.fs-5 {
  font-size: 1.15rem !important;
}

.form-control {
  border-color: #2b2b2b;
}

</style>