<template>
  <div id="sidebar">
    <div class="min-vh-100">
      <ul class="border-bottom border-dark nav navbar-nav text-break flex-column"
          style="font-size: 1.00rem; font-family: Loma,sans-serif;"
          id="menu">
        <li class="border-bottom border-dark text-center align-items-center mt-0 pt-0">
          <a href="#" class="nav-link">
            <i class="fs-3 ms-0 me-2 bi-chat-dots"></i><h4
              class="text-black d-inline fw-bold mx-auto"
              style="font-family: 'Ubuntu', 'Lucida Grande', 'Lucida Sans Unicode', 'Geneva', 'Verdana', sans-serif">
            {{ title }}</h4>
            <p class="small mt-0 mx-auto text-break"
               style="font-size: 0.95rem; color: #2b2b2b"> {{ dateTime }}</p>
          </a>
        </li>
        <li class="mb-1 ms-0 me-auto">
          <a href="/profile#dashboard" class="nav-link px-lg-0 px-xl-2">
            <i class="fs-3 bi-table"></i><span class="px-2">Tableau de bord</span></a>
        </li>
        <li class="mb-3 ms-0 me-auto">
          <a href="/profile#parcours" class="nav-link px-lg-0 px-xl-2">
            <i class="fs-3 bi-clipboard-data"></i><span class="px-2">Mon parcours</span></a>
        </li>
        <li class="mb-3 ms-0 me-auto">
          <a href="#" class="nav-link p-0 m-0 bg-transparent px-lg-0 px-xl-2 dropdown-toggle text-wrap"
             role="button"
             data-bs-toggle="dropdown"
             id="dropdown"
             aria-expanded="false"
             style="font-size: 1.00rem">
            <i class="fs-3 d-inline bi-chat-text"></i><span
              class="px-2 text-break">Mes salons</span>
          </a>
          <ul class="dropdown-menu dropdown-menu-end shadow flex-column" aria-labelledby="dropdown">
            <li v-for="c in cours" :key="c"><a class="dropdown-item" :href="`/forum/${c}`">{{ c }}</a></li>
          </ul>
        </li>
        <li class="ms-0 me-auto mb-3">
          <a href="#" class="nav-link px-lg-0 px-xl-2">
            <i class="fs-3 d-lg-inline bi-telephone-outbound"></i><span
              class="px-2">Messages privés</span></a>
        </li>
      </ul>
    </div>
  </div>

</template>

<script>
export default {
  name: "sidebar-left",
  props: {
    title: String,
  },
  data: () => ({
    dateTime: "",
    cours: Array
  }),
  mounted() {
    this.getTime();
    this.updateClock();
    this.getCours();
  },
  methods: {
    getCours() {
      fetch(`${this.$store.getters.baseUrlBackEnd}api/etudiant/${this.$cookies.get('user').email}`)
          .then(res => res.json())
          .then(data => {
            this.cours = data
          })
    },
    getTime() {
      const today = new Date();
      const date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
      const time = today.getHours() + ":" + ("0" + today.getMinutes()).slice(-2);
      this.dateTime = date + ' ' + time;
    },
    updateClock() {
      setInterval(this.getTime, 1000);
    },
  }
}
</script>

<style>


.nav-link a, i, span {
  color: black;
}

.nav-link.dropdown-toggle {
  color: black;
}

#sidebar {
  vertical-align: middle;
}


</style>