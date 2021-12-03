<template>
  <div class="container-fluid">
    <div class="row forum">
      <div class="col-1"></div>
      <div class="col-9 posts">
        <div class="row post">
          <Post
            v-for="post in posts"
            :key="post.dateTime + '_' + generateHexString()"
            :auteur="post.auteur"
            :contenu="post.contenu"
            :dateTime="post.dateTime"
          ></Post>
          <div class="row">
            <div class="col-10">
              <div class="row">
                <div class="col-12 input-post">
                  logo
                  <input
                    id="send-post"
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
      <div class="col-2 student_bar">
        <Student_bar :etudiants="students"></Student_bar>
      </div>
    </div>
  </div>
</template>

<script>
import Post from "../components/Post.vue";
import Student_bar from "../components/Student_bar.vue";

export default {
  components: {
    Post,
    Student_bar,
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
        { profilPicture: "", name: "Nami iydrgitfy" },
        { profilPicture: "", name: "Jules gfdsgfdg" },
        { profilPicture: "", name: "Mehdi fgdsggds" },
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
  overflow-y: scroll;
  overflow-x: hidden;
  height: 75vh;
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
  padding: 0.5em;
  margin-left: 1em;
}

input#send-post {
  width: 95%;
  border: none;
  border-bottom: 1px solid gray;
  outline: none;
}
</style>