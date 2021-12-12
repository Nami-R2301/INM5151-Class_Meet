<template>
  <div class="container-fluid p-0">
    <div class="row forum mx-auto pe-0">
      <div class="col-2 col-lg-3 col-xxl-2 flex-wrap flex-column position-fixed bg-light shadow">
        <sidebar-forum/>
      </div>
      <div class="col-8 col-lg-8 col-xl-8 col-xxl-8 mx-auto my-5">
        <div class="row offset-0 offset-lg-1 offset-xl-1 offset-xxl-0 text-start">
          <Post
              v-for="post in posts"
              :key="post.dateTime + '_' + generateHexString()"
              :auteur="post.auteur"
              :contenu="post.contenu"
              :dateTime="post.dateTime"
          ></Post>
        </div>
        <div class="row fixed-bottom bg-light">
          <div class="col-6 mx-auto">
            <input
                class="input-post mx-auto p-3 w-100"
                type="text"
                placeholder="Envoyer un message"
                @keypress="sendPost"
                v-model="contenu"
            />
          </div>
        </div>
      </div>
      <div class="col-2 col-lg-3 col-xxl-2 px-0 end-0 position-fixed overflow-scroll bg-light">
        <Student_bar :etudiants="students"></Student_bar>
      </div>
    </div>
  </div>
</template>

<script>
import Post from "../components/Post.vue";
import student_list from "../components/student-list.vue";
import SidebarForum from "../components/sidebar-forum";

export default {
  components: {
    SidebarForum,
    Post,
    Student_bar: student_list,
  },
  data: () => ({
    posts: [],
    students: [],
    contenu: "",
  }),
  mounted() {
    this.getPost();
    this.getStudents();
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
      this.students = [
        {profilPicture: "", name: "Nami Reghbati"},
        {profilPicture: "", name: "Jules Hauchecorne"},
        {profilPicture: "", name: "Mehdi Collomb"},
      ];
    },
  },
};
</script>


<style scoped>

.forum {
  overflow-y: hidden;
}

.posts {
  overflow-y: auto;
  overflow-x: hidden;
  display: flex;
  flex-direction: column-reverse;
}

.post {
  gap: 1.5em;
}

.input-post {
  border: 1px solid black;
  border-radius: 10px;
  transition: border-color .15s ease-in-out, box-shadow .15s ease-in-out;
}

</style>