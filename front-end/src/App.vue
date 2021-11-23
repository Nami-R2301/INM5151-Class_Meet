<template>
  <div id="app">
    <router-view/>
    <head>
      <link rel="stylesheet" href="node_modules/bootstrap/dist/css/bootstrap.min.css"/>
      <script type="application/javascript" href="node_modules/bootstrap/dist/js/bootstrap.bundle.min.js"/>
    </head>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {
  }
};
</script>

<style>
#app {
  font-family: Sen, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
