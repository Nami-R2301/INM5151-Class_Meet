<template>
  <div class="posts-hover" id="forum">
    <a href="#" class="text-black text-decoration-none">
      <div class="row flex-wrap mx-auto">
        <div class="col-auto text-start ms-2 me-auto">
          <p class="fw-bold"><i class="bi-person-circle mx-2"></i>{{ auteur }}</p>
        </div>
        <div class="col-auto text-end ms-auto me-auto me-md-3 me-xl-auto me-xxl-5">
          <small class="fst-italic text-muted">{{ dateTime }}</small>
        </div>
      </div>
      <div class="row flex-wrap mx-auto">
        <div class="col-auto ms-5 me-auto">
          <p class="ms-auto me-2" style="line-height: 1.25rem">{{ contenu }}</p>
        </div>
      </div>
    </a>
  </div>
</template>

<script>
export default {
  props: {
    auteur: String,
    contenu: String,
    dateTime: String,
  },
};
</script>

<style>

.posts-user {
  border: none;

}

.posts-hover {
  border-radius: 20px;
  border: none;
  transition: border .15s ease-in-out, box-shadow .15s ease-in-out, border-radius 0s;
}

.posts-hover:hover {
  border: 1px solid #2b2b2b;
  box-shadow: 0 0 2px #2b2b2b;
  border-radius: 20px;
}

</style>