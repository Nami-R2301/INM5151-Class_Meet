<template>
  <div class="container-fluid m-auto p-0">
    <div class="row mx-auto">
      <div class="col-2 sidebar bg-light">
        <SideBar/>
      </div>
      <div class="col-8">
        <Dashboard/>
      </div>
      <div class="col-2 student_bar bg-light">
          <Contacts :etudiants="students"/>
        </div>
    </div>
  </div>
</template>

<script>
import Dashboard from "../components/dashboard";
import SideBar from "../components/SideBar";
import Contacts from "../components/Contacts.vue";

export default {
  name: "Profile",
  components: {
    Contacts,
    Dashboard,
    SideBar
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

<style scoped>

.student_bar {
  border-left: 1px solid black;
}

.sidebar {
  border-right: 1px solid black;
}

</style>