<template>
  <div class="connexion">
    <img alt="Vue logo" src="../assets/logo.png" />
    <div>
      <h1>{{ msg }}</h1>
      <h1 class="msg_connexion">Class Meet</h1>
      <form>
        <label>Adresse courriel :</label><br />
        <input type="text" v-model="email" name="username" /><br />
        <label>Mot de passe :</label><br />
        <input type="password" v-model="password" name="password" /><br />
        <input
          type="submit"
          @click="connection"
          name="submit"
          value="Se connecter"
        />
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Connexion",
  props: {
    msg: String,
    msg2: String,
  },
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
          console.log(data);
        }).catch(err => {
          console.error(err)
        });
    },
  },
};
</script>

<style scoped>
.msg_connexion {
  color: #87ceeb;
}

h1 {
  display: inline;
}

.connexion {
  margin-top: 5%;
}

form {
  margin-top: 2%;
  margin-left: 37%;
  position: relative;
  text-align: left;
  font-family: Sen, "Times New Roman", serif;
  font-size: 120%;
  font-weight: bold;
}

label {
  margin-left: 1%;
  text-align: left;
}

input[type="text"] {
  display: inline-block;
  max-width: 50%;
  width: 40%;
  margin: 1% 1%;
  padding: 0.3%;
  text-align: left;
  border: 3px solid black;
  border-radius: 5px;
  color: black;
  background: white;
}

input[type="password"] {
  display: inline-block;
  max-width: 50%;
  width: 40%;
  margin: 1% 1%;
  padding: 0.3%;
  text-align: left;
  border: 3px solid black;
  border-radius: 5px;
  color: black;
  background: white;
}

input[type="submit"] {
  width: 15%;
  margin: 1% 0 1% 13.5%;
  padding: 1%;
  border: none;
  border-radius: 4px;
  background-color: #87ceeb;
  color: black;
  cursor: pointer;
  box-sizing: content-box;
  font-size: large;
  font-weight: bolder;
}
</style>