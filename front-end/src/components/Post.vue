<template>
  <div>
    <div class="row">
      <div class="col-1">
        <p>{{ auteur }}</p>
      </div>
      <div class="col-2">
        <p>{{ dateTime }}</p>
      </div>
    </div>
    <div class="row justify-content-start">
      <div class="col-10">
        <p>{{ contenu }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    auteur: String,
    contenu: String,
    dateTime: String,
  },
};
</script>

<style>
</style>