<template>
  <div class="container-fluid m-auto p-0">
    <div class="row mx-auto px-0">
      <div class="col-2 flex-wrap flex-column position-fixed bg-light p-0 shadow">
        <Sidebar :dateTime="date"/>
      </div>
      <div class="col-8 m-auto">
        <Dashboard/>
      </div>
      <div class="col-2 px-0 me-0 ms-auto end-0 position-fixed overflow-scroll bg-light shadow">
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
    date: "",
  }),
  mounted() {
    this.getTime();
    this.updateClock();
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
    getTime() {
      const today = new Date();
      this.date = today.getFullYear() + '-' + ("0" + (today.getMonth() + 1)).slice(-2) + '-' +
          ("0" + today.getDate()).slice(-2) + ' ' + ("0" + today.getHours()).slice(-2) + ':' +
          ("0" + today.getMinutes()).slice(-2);
    },
    updateClock() {
      setInterval(this.getTime, 1000 / 60);
    },
  }
}
</script>

<style>

</style>