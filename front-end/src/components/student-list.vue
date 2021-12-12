<template>
  <div class="shadow min-vh-100">
    <ul class="title-contacts m-auto mb-3 ps-1 ps-lg-2 ps-xl-3 ps-xxl-3 pb-1" style="font-size: medium">
      <li>
        <i class="bi-person-lines-fill align-content-center mx-auto fs-4"></i>
        <span class="ms-2 fs-5 fw-bold">Camarades</span>
      </li>
    </ul>
    <div class="row mx-auto ps-0">
      <div
          v-for="etudiant in etudiants"
          :key="etudiant.name"
          class="mb-3 mx-auto"
      >
        <i class="bi-person-circle me-2 fs-4"></i>
        <span class="fs-6 me-0">{{ etudiant.name }}</span>
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