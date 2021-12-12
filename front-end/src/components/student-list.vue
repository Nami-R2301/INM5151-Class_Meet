<template>
  <div>
    <ul class="title-camarade m-auto mb-3 pb-3" style="font-size: medium">
      <li>
        <i class="bi-person-lines-fill m-auto fs-3"></i>
        <span class="ms-3 fs-5 fw-bold">Camarades</span>
      </li>
    </ul>
    <div class="row mx-auto ps-1">
      <div
          v-for="etudiant in etudiants"
          :key="etudiant.name"
          class="mb-3 mx-auto"
      >
        <i class="bi-person-circle me-3 fs-3 fs-lg-4 fs-4"></i>
        <span class="fs-6">{{ etudiant.name }}</span>
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

.title-camarade {
  border-bottom: 1px solid black;
  border-bottom-width: thin;
  align-content: center;
}
</style>