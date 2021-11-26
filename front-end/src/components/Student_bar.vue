<template>
  <div class="container-fluid">
    <div class="row title">
      <div class="col-2">
        Logo
      </div>
      <div class="col-10">
        <h4>Liste des etudiant(e)s</h4>
      </div>
    </div>
    <div class="row">
      <div
        v-for="etudiant in etudiants"
        :key="etudiant.name"
        class="offset-2 col-10"
      >
        <p>{{ etudiant.name }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    etudiants: Array
  },
};
</script>

<style scoped>
.title {
  border-bottom: 1px solid black;
}
</style>