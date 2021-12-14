<template>
  <div class="container-fluid m-auto p-0">
    <div class="row forum mx-auto pe-0">
      <div class="col-2 flex-wrap flex-column position-fixed bg-light p-0 shadow">
        <sidebar :title="$route.params.category"></sidebar>
      </div>
      <div class="col-8 m-auto posts">
        <div class="row text-start post">
          <div class="col-12 m-auto">
            <Post
                v-for="post in posts"
                :key="post.dateTime + '_' + generateHexString()"
                :auteur="post.auteur"
                :contenu="post.contenu"
                :dateTime="post.dateTime"
            ></Post>
          </div>
          <div class="row d-flex position-absolute bottom-0 ms-5 me-auto">
            <div class="col-12 tm-auto">
              <input
                  class="input-post mx-auto p-3 mb-3 mt-0 w-50"
                  type="text"
                  placeholder="Envoyer un message"
                  @keypress="sendPost"
                  v-model="contenu"
              />
              <i class="fs-2 ms-3 me-auto my-auto bi-plus-circle"></i>
            </div>
          </div>
        </div>
      </div>
      <div
          class="col-2 px-0 me-0 ms-auto end-0 position-fixed overflow-scroll bg-light shadow">
        <Student_bar :etudiants="students"></Student_bar>
      </div>
    </div>
  </div>
</template>

<script>
import Post from "../components/Post.vue";
import student_list from "../components/student-list.vue";
import Sidebar from "../components/sidebar-left";

export default {
  components: {
    Sidebar,
    Post,
    Student_bar: student_list,
  },
  data: () => ({
    posts: [],
    contenu: "",
    students: [],
  }),
  mounted() {
    this.getPost();
    this.getStudents();
    let validator_sign_in = document.createElement("script");
    validator_sign_in.setAttribute("src", "../store/onSubmit_sign_in.js");
    document.head.appendChild(validator_sign_in);
  },
  methods: {
    // Used only to make the post unique.
    generateHexString() {
      return [...Array(20)]
          .map(() => Math.floor(Math.random() * 16).toString(16))
          .join("");
    },
    sendPost(key) {
      if (key.keyCode !== 13) return;
      const date = new Date();
      fetch(
          `${this.$store.getters.baseUrlBackEnd}api/forum/${this.$route.params.category}`,
          {
            method: "POST",
            body: JSON.stringify({
              auteur: this.$cookies.get("user").username,
              contenu: this.contenu,
              categorie: this.$route.params.category,
              dateTime: `${date.toJSON().slice(0, 10).replaceAll("-", "/")} ${date
                  .toTimeString()
                  .slice(0, 8)}`,
            }),
          }
      )
          .then((res) => res.json())
          .then((data) => {
            console.log(data);
            this.contenu = "";
            this.getPost();
          })
          .catch((err) => {
            console.error(err);
          });
    },
    getPost() {
      fetch(
          `${this.$store.getters.baseUrlBackEnd}api/forum/${this.$route.params.category}`
      )
          .then((res) => res.json())
          .then((data) => {
            this.posts = data;
          })
          .catch((err) => {
            console.error(err);
          });
    },
    getStudents() {
      fetch(
          `${this.$store.getters.baseUrlBackEnd}api/cours/${this.$route.params.category}`
      )
          .then((res) => res.json())
          .then((data) => {
            this.students = data.map((el) => ({name: el}));
          });
    },
  },
};
</script>


<style scoped>
.forum {
  overflow-y: hidden;
}

.posts {
  max-height: 75vh !important;
  clear: both;
  overflow-y: auto;
  overflow-x: hidden;
  display: flex;
  flex-direction: column-reverse;
}

.post {
  gap: 1.05rem;
}

.input-post {
  max-height: 25vh !important;
  border: 1px solid black;
  border-radius: 10px;
  transition: border-color .05s linear, box-shadow .10s linear;
}
</style>