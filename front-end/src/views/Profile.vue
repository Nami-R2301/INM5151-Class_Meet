<template>
  <div class="container-fluid m-auto p-0">
    <div class="row mx-auto">
      <div
          class="col-2 mx-1 mx-xxl-0 flex-grow-1 flex-xxl-grow-0 flex-wrap flex-column bg-light shadow"
          style="border-right: 1px solid rgba(0, 0, 0, .2);">
        <Sidebar :title="$cookies.get('user').username"/>
      </div>
      <div class="col-7 col-xxl-8 flex-shrink-1 flex-xxl-shrink-0">
        <Dashboard/>
      </div>
      <div
          class="col-2 px-0 me-0 flex-grow-1 flex-xxl-grow-0 ms-auto end-0 position-sticky overflow-scroll bg-light shadow"
          style="border-left: 1px solid rgba(0, 0, 0, .2);">
        <Contacts :etudiants="students"/>
      </div>
    </div>
  </div>
</template>

<script>
import Dashboard from "../components/dashboard";
import Contacts from "../components/contact-list.vue";
import Sidebar from "../components/sidebar-left";

export default {
  name: "Profile",
  components: {
    Sidebar,
    Contacts,
    Dashboard,
  },
  data: () => ({
    posts: [],
    students: [],
  }),
  mounted() {
    this.getStudents();
  },
  methods: {
    getStudents() {
      this.students = [
        {profilPicture: "", name: "Nami Reghbati"},
        {profilPicture: "", name: "Jules Hauchecorne"},
        {profilPicture: "", name: "Mehdi Collomb"},
      ];
    },
  }
}
</script>

<style>

</style>