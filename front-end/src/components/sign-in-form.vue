<template>
  <form action="/profile"
        class="col-6 col-sm-4 col-md-4 col-lg-4 col-xl-3 col-xxl-3 mt-3 text-start mx-auto">
    <p v-if="this.error_backend.length === 0" style="color: red; font-size: 1.10rem; font-weight: bold">{{
        error_email
      }}</p>
    <p v-else style="color: red; font-size: 1.10rem; font-weight: bold">{{ error_backend }}</p>
    <label class="form-label fw-bold mx-auto mb-2">Adresse courriel :</label>
    <b-form-input
        :required="true"
        type="email"
        v-model="email"
        @change="resetButton"
        lazy
        :state="checkEmail"
        placeholder="Ex: *****.****@gmail.com"
        class="form-control py-1 px-3 rounded-pill border-2 mx-auto mb-2"
        name="email"
        id="email"
        trim
    ></b-form-input>
    <label class="form-label fw-bold mx-auto mb-2">Mot de passe :</label>
    <b-form-input
        :required="true"
        type="password"
        @change="resetButton"
        v-model="pw"
        :state="checkPw"
        class="form-control py-1 px-3 rounded-pill border-2 m-auto"
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
  name: "sign-in-form",
  props: {
    error_email: String,
  },
  computed: {
    checkEmail() {
      let valide = null
      if (this.error_backend.length > 0) valide = false
      else if (this.email.length !== 0) valide = connection.check_email(this.email).length === 0
      if (document.getElementById('submit') !== null) this.validate_form()
      return valide
    },
    checkPw() {
      let valide = null
      if (this.error_backend.length > 0) valide = false
      else if (this.pw.length === 0) {
        if (this.email.length > 0) {
          document.getElementById('password').style.borderColor = "#2b2b2b"
          valide = connection.check_password(this.pw).length === 0
        }
      } else valide = connection.check_password(this.pw).length === 0
      if (document.getElementById('submit') !== null) this.validate_form()
      return valide
    },
  },
  data: () => ({
    error_backend: "",
    email: "",
    pw: "",
  }),
  mounted() {
    this.validate_form();
  },
  methods: {
    validate_form() {
      document.getElementById('submit').disabled = this.error_email.length !== 0
          || this.pw.length === 0 || this.email.length === 0 || this.error_backend.length !== 0;
    },
    resetButton() {
      this.error_backend = ""
    },
    connection(e) {
      e.preventDefault();
      fetch(`${this.$store.getters.baseUrlBackEnd}api/connection`, {
        method: "POST",
        body: JSON.stringify({email: this.email, password: this.pw}),
      })
          .then((res) => res.json())
          .then((data) => {
            if (data.err) {
              this.error_backend = "Adresse courriel ou mot de passe invalide!";
              document.getElementById('email').style.borderColor = "red"
              document.getElementById('password').style.borderColor = "red"
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
}
</script>

<style scoped>

.form-control {
  border-color: #2b2b2b;
}

b-form-input::placeholder {
  font-size: small;

}

</style>