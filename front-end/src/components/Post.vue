<template>
  <div>
    <div class="row">
      <div class="offset-1 col-3 mx-auto">
        <p>{{ auteur }}</p>
      </div>
      <div class="col-2 mx-auto">
        <p>{{ dateTime }}</p>
      </div>
    </div>
    <div class="row mx-auto">
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