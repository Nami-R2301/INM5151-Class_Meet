<template>
  <div>
    <div class="row title mb-3">
      <div class="col-12">
        <i class="bi-person-lines-fill fs-2"></i>
        <span class="ms-3 fs-5">Contacts</span>
      </div>
    </div>
    <div class="row">
      <div
          v-for="etudiant in etudiants"
          :key="etudiant.name"
          class="col-12 mb-3"
      >
        <i class="bi-person-circle me-3 fs-3 fs-lg-4 fs-sm-4 "></i>
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

body {
  overflow-x: hidden;
}

@media (min-width: 768px) {
  .row span {
    font-size: small;
  }
}

@media (min-width: 1080px) {
  .row span {
    font-size: medium;
  }
}

.title {
  border-bottom: 1px solid black;
}
</style>