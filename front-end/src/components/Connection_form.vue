<template>
  <form action="login">
    <label class="form-label">Adresse courriel :</label><br />
    <input
      type="text"
      v-model="email"
      class="form-control w-100 py-auto h-auto"
      name="username"
    /><br />
    <label class="form-label">Mot de passe :</label><br />
    <input
      type="password"
      v-model="password"
      class="form-control w-100 h-auto"
      name="password"
    />
    <p class="forgot-pw">Mot de passe oublié</p>

    <div class="centered text-center">
      <button
        type="submit"
        @click="connection"
        title="Soumettre"
        class="rounded-pill w-30 h-20"
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
form {
  margin-top: 5%;
  text-align: left;
  font-family: Sen, "Times New Roman", serif;
  font-size: 120%;
  font-weight: bold;
}

input[type="text"] {
  display: inline-block;
  max-width: 100%;
  margin: 0 auto 3% auto;
  padding: 0.3%;
  text-align: left;
  border: 3px groove black;
  border-radius: 5px;
  color: black;
  background: white;
}

input[type="password"] {
  display: inline-block;
  max-width: 100%;
  margin: 0 auto 3% auto;
  padding: 0.3%;
  text-align: left;
  border: 3px solid black;
  border-radius: 5px;
  color: black;
  background: white;
}

.forgot-pw {
  margin: 0;
  text-decoration-line: underline;
  font-size: medium;
}

button[type="submit"] {
  max-width: 100%;
  margin: 10% 0;
  padding: 5% 10%;
  border: none;
  background-color: #87ceeb;
  color: black;
  cursor: pointer;
  text-align: center;
  font-size: large;
  font-weight: bolder;
}
</style>