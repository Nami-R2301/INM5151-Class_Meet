<template>
  <div>
    <div class="row flex-wrap mx-auto">
      <div class="col-auto text-start ms-4 me-auto">
        <p class="fw-bold">{{ auteur }}</p>
      </div>
      <div class="col-auto text-end ms-auto me-0">
        <small class="fst-italic">{{ dateTime }}</small>
      </div>
    </div>
    <div class="row flex-wrap mx-auto">
      <div class="col-auto me-auto">
        <p class="ms-auto me-2" style="line-height: 1.25rem">{{ contenu }}</p>
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