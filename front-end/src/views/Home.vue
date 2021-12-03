<template>
  <div>
    <Main />
  </div>
</template>

<script>
import Main from "../components/Main";

export default {
  name: "Home",
  components: {
    Main,
  },
  mounted() {
    console.log("dev:", this.$cookies.get("user"))
  }
};
</script>

<style>
</style>