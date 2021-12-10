<template>
  <div id="dashboard" class="dashboard">
    <div class="row mt-4">
      <div class="col-12 centered">
        <img class="img-fluid w-25" alt="Vue logo"
             src="../assets/user.png">
      </div>
    </div>
    <div class="row">
      <div class="col-12 d-flex justify-content-center" style="margin: 2% 25%;">
        <i class="bi-pie-chart bi-align-end"></i>
      </div>
    </div>
    <div class="row centered text-center">
      <p class="name fw-bold fs-5 mt-4 mb-0">Nami Reghbati</p>
      <p class="programme text-decoration-underline mt-2">Baccalauréat en génie logiciel et informatique</p>
    </div>
  </div>
</template>

<script>

export default {
  name: "Dashboard",
  props: {
    myname: String
  },
  data: () => ({
    students: [],
  }),
}
</script>

<style scoped>

.centered {
  display: flex;
  align-items: center;
  justify-content: center;
}

.name {
  font-family: 'Ubuntu', 'Lucida Grande', 'Lucida Sans Unicode', 'Geneva', 'Verdana', sans-serif;
}

</style>