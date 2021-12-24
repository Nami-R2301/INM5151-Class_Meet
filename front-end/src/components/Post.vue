<template>
  <div class="posts-hover" id="forum">
    <div class="row flex-wrap">
      <div class="col-auto align-content-start ms-0 me-auto">
        <b-icon-person-circle class="me-2 text-black" style="vertical-align: middle"
                              font-scale="1.5"></b-icon-person-circle>
        <span class="fw-bold">{{ auteur }}</span>
      </div>
      <div class="col-auto text-end mx-auto me-0">
        <small class="fst-italic text-muted mx-auto">{{ dateTime }}</small>
      </div>
    </div>
    <div class="row ms-1 me-auto me-xxl-5 p-0 text-break text-wrap">
      <div>
        <p class="ps-4"
           style="line-height: 1.25rem; font-family: 'Ubuntu', 'Lucida Grande', 'Lucida Sans Unicode', 'Geneva'
           , 'Verdana', sans-serif;">
          {{ contenu }}</p>
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