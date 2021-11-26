<template>
  <div>
    <div class="row">
      <div class="offset-1 col-3">
        <p>{{ auteur }}</p>
      </div>
      <div class="col-3">
        <p>{{ dateTime }}</p>
      </div>
    </div>
    <div class="row">
      <div class="offset-1 col-10">
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