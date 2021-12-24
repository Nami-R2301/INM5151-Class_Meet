<template>
  <form action="/profile"
        class="col-6 col-sm-4 col-md-4 col-lg-4 col-xl-3 col-xxl-3 mt-3 text-start mx-auto">
    <p v-if="this.error_backend.length === 0" style="color: red; font-size: 1.10rem; font-weight: bold">{{
          error_email
        }}</p>
      <p v-else style="color: red; font-size: 1.10rem; font-weight: bold">{{ error_backend }}</p>
    <label class="form-label fw-bold mx-auto fs-5">Adresse courriel :</label><br/>
    <b-form-input
        type="text"
        v-model="email"
        :state="checkEmail"
        placeholder="Entrez votre courriel"
        class="form-control py-1 px-3 rounded-pill border-3 m-auto fs-5"
        name="username"
        id="email"
    ></b-form-input>
    <label class="form-label fw-bold mx-auto fs-5">Mot de passe :</label><br/>
    <b-form-input
        type="password"
        v-model="password"
        :state="checkPw"
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

export default {
  name: "sign-in-form",
  computed: {
    checkEmail() {
      if(this.email.length === 0) return
      return this.check_email(this.email)
    },
    checkPw() {
      if(this.password.length === 0) return
      return this.validate_pw()
    },
  },
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
    check_email(email) {
      const reg_email = new RegExp('\\b(^[a-zA-z0-9-.]+@[a-zA-Z]+.(\\bcom\\b|\\bca\\b|\\borg\\b|\\bedu\\b|\\bfr\\b)$)\\b');
      this.error_email = "";
      let msgE2 = "\tL'adresse courriel saisie n'est pas une adresse de format valide !";

      document.getElementById("email").style.borderColor = "#2b2b2b"
      if(email.length === 0) return false;
      if (email.toString().match(reg_email) === null || email.length < 4) {
        console.log("Email not valid!\n");
        document.getElementById("email").style.borderColor = "red"
        this.error_email = msgE2;
      }
      this.validate_form()
      return this.error_email.length === 0
    },
    validate_pw() {
      this.error_pw = ""
      document.getElementById("password").style.borderColor = "#2b2b2b"
      if (this.password.length === 0) {
        document.getElementById("password").style.borderColor = "red"
      }
      this.validate_form()
    },
    validate_form() {
      document.getElementById('submit').disabled = this.email.length === 0 ||
          this.password.length === 0;
    },
    connection(e) {
      e.preventDefault();
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