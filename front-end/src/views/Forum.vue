<template>
  <div class="container-fluid p-0">
    <div class="row justify-content-evenly forum mx-auto">
      <div class="col-auto flex-grow-0 bg-light">
        <sidebarSignedIn/>
      </div>
      <div class="col-auto mx-auto posts">
        <div class="row text-start post">
          <Post
            v-for="post in posts"
            :key="post.dateTime + '_' + generateHexString()"
            :auteur="post.auteur"
            :contenu="post.contenu"
            :dateTime="post.dateTime"
          ></Post>
          <div class="row mx-auto p-0">
            <div class="col-12">
              <div class="row mx-auto">
                <div class="col-12 mx-auto input-post">
                  <i class="bi-chat-dots m-auto"></i>
                  <input
                    id="send-post"
                    class="mx-auto p-3"
                    type="text"
                    placeholder="Envoyer un message"
                    @keypress="sendPost"
                    v-model="contenu"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-2 float-end student_bar bg-light p-0">
        <Student_bar :etudiants="students"></Student_bar>
      </div>
    </div>
  </div>
</template>

<script>
import Post from "../components/Post.vue";
import student_list from "../components/student-list.vue";
import sidebarSignedIn from "../components/sidebar-signed-in";

export default {
  components: {
    Post,
    Student_bar: student_list,
    sidebarSignedIn
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
        { profilPicture: "", name: "Nami Reghbati" },
        { profilPicture: "", name: "Jules Hauchecorne" },
        { profilPicture: "", name: "Mehdi Collomb" },
      ];
    },
  },
};
</script>


<style scoped>

.right {
  display: flex;
  align-items: start;
  justify-content: end;
}
.forum {
  overflow-y: hidden;
}

.posts {
  overflow-y: scroll;
  overflow-x: hidden;
  height: 85vh;
  /* Reverse scroll bar */
  display: flex;
  flex-direction: column-reverse;
}

.post {
  gap: 1.5em;
}

.student_bar {
  border-left: 1px solid black;
}

.input-post {
  border: 1px solid black;
  border-radius: 10px;
}

input#send-post {
  width: 85%;
  border: none;
  outline: none;
}
</style>