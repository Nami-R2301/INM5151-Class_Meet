<template>
  <div class="container-fluid forum">
    <div class="row">
      <div
          class="col-2 mx-1 mx-sm-0 mx-md-0 mx-lg-0 mx-xl-0 mx-xxl-0 flex-grow-1 flex-xxl-grow-0 flex-wrap
          flex-column position-fixed bg-light shadow"
          style="border-right: 1px solid rgba(0, 0, 0, .2);">
        <sidebar :title="$route.params.category"></sidebar>
      </div>
      <div class="col-8 col-sm-8 col-md-8 col-lg-8 col-xl-8 col-xxl-8 mx-auto flex-shrink-1 posts">
        <div class="row mx-auto text-start post">
          <div class="col-12">
            <Post
                v-for="post in posts"
                :key="post.dateTime + '_' + generateHexString()"
                :auteur="post.auteur"
                :contenu="post.contenu"
                :dateTime="post.dateTime"
            ></Post>
          </div>
          <div class="row m-auto col-8 col-md-7 col-lg-7 col-xl-7 col-xxl-8 d-flex position-absolute bottom-0">
            <div class="text-center align-items-center">
              <input
                  class="input-post mx-auto p-3 mb-3 mt-0 w-50"
                  type="text"
                  placeholder="Envoyer un message"
                  @keypress="sendPost"
                  v-model="contenu"
              />
              <i class="fs-2 ms-3 me-auto bi-plus-circle"></i>
            </div>
          </div>
        </div>
      </div>
      <div
          class="col-2 mx-auto ps-0 pe-1 text-break flex-grow-1 flex-column position-fixed end-0 overflow-scroll bg-light shadow"
          style="border-left: 1px solid rgba(0, 0, 0, .2);">
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

body {
  overflow-y: hidden;
}

.posts {
  max-height: 75vh !important;
  clear: both;
  overflow-y: scroll;
  overflow-x: hidden;
  display: flex;
  flex-direction: column-reverse;
}

.post {
  gap: 1.05rem;
}

.input-post {
  border: 1px solid black;
  border-radius: 10px;
  transition: border-color .05s linear, box-shadow .10s linear;
}
</style>