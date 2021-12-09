<template>
  <div id="dashboard" class="dashboard">
    <div class="col-auto">
      <div class="row centered mt-4">
        <img class="img-fluid w-25 col-auto" alt="Vue logo"
             src="../assets/user.png">
      </div>
      <div class="row">

      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "Dashboard",
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

</style>