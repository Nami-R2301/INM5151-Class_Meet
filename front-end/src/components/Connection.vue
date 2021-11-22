<template>
     <div class=connection>
        <h1> {{ msg }}</h1>
    </div>
    <div>
        <form action="login">
            <label>Adresse courriel ou identifiant du compte</label><br>
            <input type="text" name="username"/><br>
            <label>Mot de passe :</label><br>
            <input type="password" name="password"/>
        </form>
    </div>
</template>

    <script>
export default {
  name: 'Connection',
  props: {
    msg: String
  }
}
    </script>

    <style scoped>

    </style>




