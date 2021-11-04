<template>
  <div class="connexion">
  <h1>{{msg}}</h1>
    <img alt="Vue logo" src="../assets/logo.png">
    <div>
        <form action="login">
            <label>Adresse courriel :</label><br>
            <input type="text" name="username"/><br>
            <label>Mot de passe :</label><br>
            <input type="password" name="password"/>
        </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Connexion",
  props: {
    msg: String
  }
}
</script>

<style scoped>

</style>