<template>
  <div class="min-vh-100">
    <ul class="title-contacts m-auto mb-3 pb-1" style="font-size: 1.00rem">
      <li>
        <b-icon-person-circle class="me-2 text-black" style="vertical-align: middle"
                              font-scale="2"></b-icon-person-circle>
        <span style="vertical-align: middle" class="fs-5 fw-bold">Contacts</span>
      </li>
    </ul>
    <div class="row ms-0 me-auto px-0">
      <div
          v-for="etudiant in etudiants"
          :key="etudiant.name"
          class="mb-3"
      >
        <b-icon-person-circle v-if="etudiant.name !== $cookies.get('user').username" class="me-2 text-black"
                              style="vertical-align: middle"
                              font-scale="1.5"></b-icon-person-circle>
        <span v-if="etudiant.name !== $cookies.get('user').username"  style="vertical-align: middle"
              class="fs-6 me-0 mb-3">{{ etudiant.name }}</span>
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