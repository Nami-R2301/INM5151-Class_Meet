<template>
  <div id="sidebar">
    <div class="min-vh-100" style="border-right: 1px solid rgba(0, 0, 0, .2);">
      <ul class="border-bottom border-dark nav navbar-nav flex-column"
          style="font-size: 1.00rem; font-family: Loma,sans-serif;"
          id="menu">
        <li class="border-bottom border-dark text-center justify-content-center mt-0 pt-0">
          <a href="#" class="nav-link">
            <i class="fs-2 ms-0 me-2 bi-chat-dots"></i><h4
              class="text-black d-inline fw-bold mx-auto"
              style="font-family: 'Ubuntu', 'Lucida Grande', 'Lucida Sans Unicode', 'Geneva', 'Verdana', sans-serif">
            INF5151</h4>
            <p class="small mt-0 mx-auto text-break"
               style="font-size: 0.95rem; color: #2b2b2b"> {{dateTime}}</p>
          </a>
        </li>
        <li class="mb-3 ms-0 me-auto">
          <a href="/profile#dashboard" class="nav-link px-lg-0 px-xl-3 px-xxl-3">
            <i class="fs-3 bi-table"></i><span class="px-lg-2 px-xl-3 px-xxl-3">Tableau de bord</span> </a>
        </li>
        <li class="mb-3 ms-0 me-auto">
          <a href="/profile#parcours" class="nav-link px-lg-0 px-xl-3 px-xxl-3">
            <i class="fs-3 bi-clipboard-data"></i><span class="px-lg-2 px-xl-3 px-xxl-3">Mon parcours</span></a>
        </li>
        <li class="mb-3 ms-0 me-auto">
          <a href="#" class="nav-link px-lg-0 px-xl-3 px-xxl-3 dropdown-toggle text-wrap" role="button"
             data-bs-toggle="dropdown"
             id="dropdown"
             aria-expanded="false">
            <i class="fs-3 d-inline bi-chat-text"></i><span
              class="px-lg-2 px-xl-3 px-xxl-3 text-break">Mes salons</span>
          </a>
          <ul class="dropdown-menu dropdown-menu-end shadow flex-column" aria-labelledby="dropdown">
            <li><a class="dropdown-item" href="/forum/INM5151">INM5151</a></li>
            <li><a class="dropdown-item" href="/forum/INF5153">INF5153</a></li>
            <li><a class="dropdown-item" href="/forum/INF5130">INF5130</a></li>
            <li><a class="dropdown-item" href="/forum/INM6000">INM6000</a></li>
          </ul>
        </li>
        <li class="ms-0 me-auto mb-3">
          <a href="#" class="nav-link px-lg-0 px-xl-3 px-xxl-3">
            <i class="fs-3 d-lg-inline bi-telephone-outbound"></i><span
              class="px-lg-2 px-xl-3 px-xxl-3">Messages privés</span></a>
        </li>
        <li class="ms-0 me-auto mb-3">
          <a href="#" class="nav-link px-lg-0 px-xl-3 px-xxl-3">
            <i class="fs-3 d-inline bi-people"></i><span class="px-lg-2 px-xl-3 px-xxl-3 text-break">Déconnexion</span>
          </a>
        </li>
      </ul>
    </div>
  </div>

</template>

<script>
export default {
  name: "sidebar-forum",
  props: {
    dateTime: String,
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

.dropdown-menu {
  position: absolute;
  z-index: 1000;
  display: flex;
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


</style>