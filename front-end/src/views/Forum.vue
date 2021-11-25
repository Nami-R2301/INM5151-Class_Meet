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
      this.posts = [
        {
          auteur: "name",
          contenu: "Lorem ipsium",
          dateTime: new Date().toString(),
        },
        {
          auteur: "name",
          contenu: "Lorem ipsium",
          dateTime: new Date().toString(),
        },
        {
          auteur: "name",
          contenu: "Lorem ipsium",
          dateTime: new Date().toString(),
        },
      ];
    },
  },
};
</script>

<style>
</style>