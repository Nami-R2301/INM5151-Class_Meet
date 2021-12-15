<template>
  <form action="/profile"
        class="col-6 col-sm-4 col-md-4 col-lg-4 col-xl-3 col-xxl-3 mt-3 text-start mx-auto">
    <p v-if="this.error_backend.length === 0" style="color: red; font-size: 1.10rem; font-weight: bold">{{
        error_email
      }}</p>
    <p v-else style="color: red; font-size: 1.10rem; font-weight: bold">{{ error_backend }}</p>
    <label class="form-label fw-bold mx-auto fs-5">Adresse courriel :</label><br/>
    <input
        @focusout="validate_email"
        @keypress="validate_form"
        type="text"
        v-model="email"
        class="form-control py-1 px-3 rounded-pill border-3 m-auto fs-5"
        name="username"
        id="email"
    /><br/>
    <p style="color: red; font-size: 1.10rem; font-weight: bold">{{ error_pw }}</p>
    <label class="form-label fw-bold mx-auto fs-5">Mot de passe :</label><br/>
    <input
        @keyup="validate_pw"
        type="password"
        v-model="password"
        class="form-control fs-5 py-1 px-3 rounded-pill border-3 m-auto"
        name="password"
        id="password"
    />
    <!--    <i class="bi-eye-slash"></i>-->
    <p class="fw-bold text-decoration-underline small mt-2 mx-auto">Mot de passe oublié</p>

    <div class="d-flex m-auto">
      <button
          type="submit"
          @click="connection"
          title="Soumettre"
          class="btn btn-outline-primary text-break rounded-pill border-3 text-center col-sm-9 col-lg-7 py-4 fw-bold my-4 mx-auto"
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
  name: "sign-in-form",
  data: () => ({
    error_backend: "",
    email: "",
    error_email: "",
    error_pw: "",
    password: "",
  }),
  mounted() {
    this.validate_form();
  },
  methods: {
    validate_email() {
      this.error_email = connection.check_email(this.email)
      if (this.error_email.length > 1) document.getElementById("email").style.borderColor = "red"
      else document.getElementById("email").style.borderColor = "#2b2b2b"
      this.validate_form()
    },
    validate_pw() {
      this.error_pw = connection.check_password(this.password)
      if (this.error_pw.length > 1) document.getElementById("password").style.borderColor = "red"
      else document.getElementById("password").style.borderColor = "#2b2b2b"
      this.validate_form()
    },
    validate_form() {
      document.getElementById('submit').disabled = this.email.length === 0 ||
          this.password.length === 0 || this.error_email.length !== 0 || this.error_pw.length !== 0;
    },
    connection(e) {
      e.preventDefault();
      this.validate_email(this.email);
      this.validate_pw(this.password);
      if (this.error_pw.length === 0 && this.error_email.length === 0) {
        fetch(`${this.$store.getters.baseUrlBackEnd}api/connection`, {
          method: "POST",
          body: JSON.stringify({email: this.email, password: this.password}),
        })
            .then((res) => res.json())
            .then((data) => {
              if (data.err) {
                this.error_backend = "Adresse courriel ou mot de passe invalide!";
              } else {
                this.$store.dispatch("connection")
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
}
</script>

<style scoped>

.fs-5 {
  font-size: 1.10rem !important;
}

.form-control {
  border-color: #2b2b2b;
}

</style>