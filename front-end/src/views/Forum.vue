<template>
  <div class="container-fluid p-0">
    <div class="row forum mx-auto pe-0">
      <div class="col-2 flex-wrap flex-column position-fixed bg-light shadow">
        <sidebar-forum/>
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
        </div>
        <div class="row fixed-bottom m-auto">
          <div class="col-6 m-auto">
            <input
                class="input-post ms-5 me-auto p-3 mb-3 mt-0 w-75"
                type="text"
                placeholder="Envoyer un message"
                @keypress="sendPost"
                v-model="contenu"
            />
            <i class="fs-2 ms-3 me-auto my-auto bi-plus-circle"></i>
          </div>
        </div>
      </div>
      <div class="col-2 px-0 mx-auto end-0 position-fixed overflow-scroll bg-light">
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
    let validator_sign_in = document.createElement('script')
    validator_sign_in.setAttribute('src', '../store/onSubmit_sign_in.js')
    document.head.appendChild(validator_sign_in)
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
  transition: border-color .15s linear, box-shadow .15s linear;
}

</style>