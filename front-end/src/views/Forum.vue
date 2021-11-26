<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12">FORUM</div>
    </div>
    <div class="row posts">
      <Post
        v-for="post in posts"
        :key="post.dateTime + '_' + generateHexString()"
        :auteur="post.auteur"
        :contenu="post.contenu"
        :dateTime="post.dateTime"
      ></Post>
    </div>
  </div>
</template>

<script>
import Post from "../components/Post.vue";

export default {
  components: {
    Post,
  },
  data: () => ({
    posts: [],
  }),
  mounted() {
    this.getPost();
  },
  methods: {
    // Used only to make the post unique.
    generateHexString() {
      return [...Array(20)]
        .map(() => Math.floor(Math.random() * 16).toString(16))
        .join("");
    },
    getPost() {
      fetch(`${this.$store.getters.baseUrlBackEnd}`)
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
        })
        .catch((err) => {
          console.error(err);
        });
      this.posts = [
        {
          auteur: "name",
          contenu:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut commodo turpis, sit amet porttitor nibh. In hac habitasse platea dictumst. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla dapibus ex non purus dapibus, sit amet ultrices orci dictum. Etiam auctor non orci tempus ultricies. Ut molestie risus massa, sit amet auctor arcu viverra in. Cras vulputate purus vitae lacus ultricies, vitae gravida enim gravida. Vestibulum risus lorem, semper non lorem condimentum, hendrerit fringilla ipsum. Duis sed tellus nec erat feugiat imperdiet. Duis vitae sem ut nulla posuere malesuada. Aliquam et lacus a orci porttitor finibus.",
          dateTime: new Date().toDateString(),
        },
        {
          auteur: "name",
          contenu:
            "Praesent neque ipsum, tempus nec laoreet nec, blandit sit amet ex. Proin luctus rutrum laoreet. Duis nibh justo, hendrerit sit amet purus non, congue facilisis massa. Suspendisse eget lectus et diam euismod dapibus. Donec vitae interdum sapien, in luctus felis. Praesent porttitor lectus a purus faucibus dignissim et ac mi. Suspendisse facilisis nisl velit, et mattis quam suscipit ut. Duis porttitor rutrum diam a pharetra. Nam ipsum neque, porta nec nibh id, molestie egestas nibh. Proin pretium vestibulum nunc, sed consequat orci laoreet in. Nunc in nisi egestas, iaculis erat vitae, aliquet tellus. Nam non nibh mi. Nulla at hendrerit dolor, eu euismod quam. Praesent ut leo leo. Etiam sodales mi a turpis vulputate condimentum. Nam non ligula arcu.",
          dateTime: new Date().toDateString(),
        },
        {
          auteur: "name",
          contenu:
            "Quisque blandit pulvinar erat, at cursus neque imperdiet a. Sed augue lorem, dapibus et pulvinar et, pulvinar quis ipsum. Praesent non finibus nisl, vitae auctor eros. Suspendisse odio augue, facilisis in vulputate sit amet, tempor ac sem. Mauris scelerisque magna sit amet fermentum vehicula. Morbi volutpat interdum cursus. Vestibulum mattis massa vel felis egestas consequat. Curabitur turpis quam, laoreet at augue et, dictum faucibus ligula. Nulla condimentum arcu ut neque ultricies, nec dictum tortor cursus. Nam in lacinia mi.",
          dateTime: new Date().toDateString(),
        },
      ];
    },
  },
};
</script>

<style scoped>
.posts {
  gap: 1.5em;
}
</style>