<template>
  <div>
    <div class="row title mb-3 m-auto">
      <div class="col-12 m-auto">
        <i class="bi-person-lines-fill fs-2"></i>
        <span class="ms-3 fs-5">Contacts</span>
      </div>
    </div>
    <div class="row">
      <div
          v-for="etudiant in etudiants"
          :key="etudiant.name"
          class="mb-3"
      >
        <i class="bi-person-circle me-3 fs-3"></i>
        <span class="fw-bold">{{ etudiant.name }}</span>
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

<style>

body {
  overflow-x: hidden;
}
.title {
  border-bottom: 1px solid black;
}
</style>