<template>
  <form action="/profile" onsubmit="return onSubmit()" class="mt-3 justify-content-center align-content-center mx-auto">
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
    <i class="bi-eye-slash"></i>
    <p class="fw-bold text-decoration-underline fs-6 m-auto">Mot de passe oublié</p>

    <div class="d-flex m-auto">
      <button
        type="submit"
        @click="connection"
        title="Soumettre"
        class="btn btn-outline-primary shadow rounded-pill text-center px-5 py-4 fw-bold my-4 mx-auto"
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
            this.$router.push("/");
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
  font-size: 1.15rem!important;
}

@media (min-width: 1440px) {
  form {
    max-width: 22.5%;
  }
}

@media (max-width: 1440px) {
  form {
    max-width: 30%;
  }
}

@media (max-width: 1080px) {
  form {
    max-width: 30%;
  }
}

@media (max-width: 1024px) {
  form {
    max-width: 37.5%;
  }
}

@media (max-width: 768px) {
  form {
    max-width: 35%;
  }
}
form {
  text-align: left;
}

</style>