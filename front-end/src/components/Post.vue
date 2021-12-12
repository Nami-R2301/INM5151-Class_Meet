<template>
  <div class="posts-hover" id="forum">
      <div class="row flex-wrap m-auto">
        <div class="col-auto align-content-start me-auto">
          <i class="fs-2 bi-person-circle ms-0 me-3"></i><span class="fw-bold">{{ auteur }}</span>
        </div>
        <div class="col-auto text-end ms-auto me-auto me-lg-0 me-xxl-0">
          <small class="fst-italic text-muted">{{ dateTime }}</small>
        </div>
      </div>
      <div class="row text-break text-wrap justify-content-center mx-xxl-5 mx-lg-5">
        <div>
          <p class="mx-auto" style="line-height: 1.25rem">{{ contenu }}</p>
        </div>
      </div>
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