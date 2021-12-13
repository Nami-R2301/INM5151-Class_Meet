<template>
  <div class="container-fluid m-auto p-0">
    <div class="row mx-auto px-0">
      <div class="col-2 px-0 flex-wrap flex-column bg-light shadow">
        <Sidebar/>
      </div>
      <div class="col-8">
        <Dashboard/>
      </div>
      <div class="col-2 px-0 flex-wrap flex-column bg-light shadow">
          <Contacts :etudiants="students"/>
        </div>
    </div>
  </div>
</template>

<script>
import Dashboard from "../components/dashboard";
import Contacts from "../components/contact-list.vue";
import Sidebar from "../components/sidebar-user";

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