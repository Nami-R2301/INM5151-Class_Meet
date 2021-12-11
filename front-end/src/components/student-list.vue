<template>
  <div>
    <div class="title mb-3">
      <ul class="flex-column mx-auto">
        <li>
        <i class="bi-person-lines-fill fs-2"></i>
        <span class="ms-3 fs-5">Camarades</span>
      </li>
      </ul>
    </div>
    <div class="row mx-auto">
      <div
          v-for="etudiant in etudiants"
          :key="etudiant.name"
          class="col-12 mb-3"
      >
        <i class="bi-person-circle me-3 fs-3 fs-lg-4 fs-sm-4"></i>
        <span class="fw-bold fs-sm-4 fs-xl-3">{{ etudiant.name }}</span>
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

.title {
  border-bottom: 1px solid black;
}
</style>