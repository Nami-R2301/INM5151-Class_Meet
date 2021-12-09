<template>
  <div>
    <div class="row title mb-3">
      <div class="col-auto">
        <span>Logo</span>
      </div>
      <div class="col-auto">
        <h4>Contacts</h4>
      </div>
    </div>
    <div class="row">
      <div
          v-for="etudiant in etudiants"
          :key="etudiant.name"
          class="offset-1 row col-auto"
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