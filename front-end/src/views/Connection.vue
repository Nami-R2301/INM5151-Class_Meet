<template>
  <div>
    <!-- <img alt="Vue logo" src="./../public/ClassMeetLogo.png" /> -->

    <div class="connection">
      <h1>TITRE</h1>
    </div>
    <div>
      <form action="login">
        <label>Adresse courriel ou identifiant du compte</label><br />
        <input type="text" name="username" /><br />
        <label>Mot de passe :</label><br />
        <input type="password" name="password" />
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Connection",
};
</script>

<style scoped>
</style>




