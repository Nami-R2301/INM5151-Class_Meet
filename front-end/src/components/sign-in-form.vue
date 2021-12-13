<template>
  <form action="/profile" onsubmit="return onSubmit()" class="col-6 col-sm-4 col-md-4 col-lg-4 col-xl-3 col-xxl-2 mt-3 text-start mx-auto">
    <label class="form-label fw-bold mx-auto fs-5">Adresse courriel :</label><br />
    <input
      type="text"
      v-model="email"
      class="form-control py-1 px-3 rounded-pill border-2 border-secondary m-auto fs-5"
      name="username"
    /><br />
    <label class="form-label fw-bold mx-auto fs-5">Mot de passe :</label><br />
    <input
      type="password"
      v-model="password"
      class="form-control fs-5 py-1 px-3 rounded-pill border-2 border-bottom border-secondary m-auto"
      name="password"
    />
<!--    <i class="bi-eye-slash"></i>-->
    <p class="fw-bold text-decoration-underline small mt-2 mx-auto">Mot de passe oublié</p>

    <div class="d-flex m-auto">
      <button
        type="submit"
        @click="connection"
        title="Soumettre"
        class="btn btn-outline-primary rounded-pill text-center col-6 py-4 fw-bold my-4 mx-auto"
        name="submit"
      >
        Soumettre
      </button>
    </div>
  </form>
</template>

<script>
export default {
  name: "Connexion",
  data: () => ({
    email: "",
    password: "",
  }),
  methods: {
    connection(e) {
      e.preventDefault();

      fetch(`${this.$store.getters.baseUrlBackEnd}api/connection`, {
        method: "POST",
        body: JSON.stringify({ email: this.email, password: this.password }),
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.err) {
            alert(data.err);
          } else {
            this.$cookies.set("user", data);
            this.$router.push("/profile");
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>

<style scoped>

.fs-5 {
  font-size: 1.10rem!important;
}

button[type=submit] {
  -webkit-filter: drop-shadow(3px 3px 3px #2b2b2b);
  filter: drop-shadow(3px 3px 3px #2b2b2b);
}

</style>