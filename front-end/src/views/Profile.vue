<template>
  <div class="container-fluid m-auto p-0">
    <div class="row">
      <div class="col-2">
        <SideBar/>
      </div>
      <div class="col-7">
        <Dashboard/>
      </div>
      <div class=" col-3 student_bar">
          <Student_bar :etudiants="students"/>
        </div>
    </div>
  </div>
</template>

<script>
import Dashboard from "../components/dashboard";
import SideBar from "../components/SideBar";
import Student_bar from "../components/Student_bar";

export default {
  name: "Profile",
  components: {
    Student_bar,
    Dashboard,
    SideBar
  },
  data: () => ({
    posts: [],
    students: [],
    contenu: "",
  }),
  mounted() {
    this.getStudents();
  },
  methods: {
    getStudents() {
      this.students = [
        {profilPicture: "", name: "Nami iydrgitfy"},
        {profilPicture: "", name: "Jules gfdsgfdg"},
        {profilPicture: "", name: "Mehdi fgdsggds"},
      ];
    },
  }
}
</script>

<style scoped>

.student_bar {
  border-left: 1px solid black;
}

</style>