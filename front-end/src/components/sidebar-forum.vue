<template>
  <div id="sidebar">
    <div class="min-vh-100">
      <ul class="title-nav-user nav navbar ms-0 me-auto p-0" style="font-size: medium; font-family: Loma,sans-serif;"
          id="menu">
        <li class="title-course mt-0 pt-0 ms-0 me-auto">
          <a href="#" data-bs-toggle="collapse" class="nav-link">
            <i class="fs-2 mx-auto bi-chat-dots"></i><h4
              class="d-inline text-black fw-bold text-decoration-underline ms-3"
              style="font-family: 'Ubuntu', 'Lucida Grande', 'Lucida Sans Unicode', 'Geneva', 'Verdana', sans-serif">
            INF5151</h4>
            <p class="small mt-0 mx-auto" style="font-size: 0.95rem; color: #2b2b2b">DD/MM/YYYY HH:MM:SS</p>
          </a>
        </li>
        <li class="mb-3 ms-0 me-auto">
          <a href="/profile#dashboard" class="nav-link">
            <i class="fs-3 bi-table"></i><span class="px-3">Tableau de bord</span> </a>
        </li>
        <li class="mb-3 ms-0 me-auto">
          <a href="/profile#parcours" class="nav-link">
            <i class="fs-3 bi-clipboard-data"></i><span class="px-3">Mon parcours</span></a>
        </li>
        <li class="mb-3 ms-0 me-auto">
          <a href="#" class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" id="dropdown"
             aria-expanded="false">
            <i class="fs-3 bi-chat-text"></i><span class="px-3">Mes salons</span>
          </a>
          <ul class="dropdown-menu dropdown-menu-end shadow flex-column" aria-labelledby="dropdown">
            <li><a class="dropdown-item" href="/forum/INM5151">INM5151</a></li>
            <li><a class="dropdown-item" href="/forum/INF5153">INF5153</a></li>
            <li><a class="dropdown-item" href="/forum/INF5130">INF5130</a></li>
            <li><a class="dropdown-item" href="/forum/INM6000">INM6000</a></li>
          </ul>
        </li>
        <li class="ms-0 me-auto mb-3">
          <a href="#" class="nav-link">
            <i class="fs-3 bi-telephone-outbound"></i><span class="px-3">Contactez une personne</span></a>
        </li>
        <li class="ms-0 me-auto mb-3">
          <a href="#" class="nav-link">
            <i class="fs-3 bi-people"></i><span class="px-3">Déconnexion</span> </a>
        </li>
      </ul>
    </div>
  </div>

</template>

<script>
export default {
  name: "sidebar-forum",
  mounted() {
    let dropdown = document.createElement('script')
    dropdown.setAttribute('src', 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/js/bootstrap.bundle.min.js')
    document.head.appendChild(dropdown)
  }
}
</script>

<style scoped>

.title-course {
  margin: auto auto !important;
  border-bottom: 1px solid black;
}

.nav-link a, i, span {
  color: black;
}

.nav-link.dropdown-toggle {
  color: black;
}

.dropdown-menu {
  z-index: 1000;
  display: none;
  min-width: 10rem;
  padding: 0.5rem 0;
  margin: 0;
  font-size: 1rem;
  color: #212529;
  text-align: left;
  list-style: none;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, .15);
  border-radius: 0.25rem;
}

.dropdown-menu[data-bs-popper] {
  top: auto;
}

</style>