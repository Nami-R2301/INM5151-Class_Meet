<template>
  <div class="min-vh-100">
    <ul class="title-contacts m-auto mb-3 pb-1 ps-3" style="font-size: 1.00rem">
      <li>
        <i class="bi-person-lines-fill m-auto fs-3"></i>
        <span class="ms-2 fw-bold">Camarades</span>
      </li>
    </ul>
    <div class="row ms-auto me-0 ps-0">
      <div
          v-for="etudiant in etudiants"
          :key="etudiant.name"
          class="mb-3 mx-auto" style="font-size: 1.00rem"
      >
        <i class="bi-person-circle me-2 fs-4"></i>
        <span class="me-0">{{ etudiant.name }}</span>
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

.title-contacts {
  border-bottom: 1px solid black;
  border-bottom-width: thin;
  align-content: center;
}
</style>