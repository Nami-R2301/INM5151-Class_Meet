<template>
  <div id="sidebar">
      <div
          class="align-items-start ms-2 min-vh-100">
        <ul class="title-nav-user nav navbar ms-0 me-auto p-0" style="font-size: medium; font-family: Loma,sans-serif;"
            id="menu">
          <li class="title-nav-user mt-0 pt-0 ms-0 me-auto">
            <a href="/profile#dashboard" data-bs-toggle="collapse" class="nav-link">
              <i class="fs-1 mx-auto bi-person-circle"></i><span
                class="fs-3 text-black fw-bold text-decoration-underline ms-3">Nami R.</span>
              <p class="small mt-0 mx-auto" style="font-size: 0.95rem; color: #2b2b2b">DD/MM/YYYY HH:MM:SS</p>
            </a>
          </li>
          <li class="mb-3 ms-0 me-auto">
            <a href="/profile#dashboard" data-bs-toggle="collapse" class="nav-link">
              <i class="fs-3 bi-clipboard-data"></i><span class="px-3">Tableau de bord</span> </a>
          </li>
          <li class="mb-3 ms-0 me-auto">
            <a href="/profile#parcours" class="nav-link">
              <i class="fs-3 bi-table"></i><span class="px-3">Mon parcours</span></a>
          </li>
          <li class="mb-3 ms-0 me-auto">
            <a href="#" class="nav-link dropdown-toggle" role="button"
               aria-expanded="false">
              <i class="fs-3 bi-bootstrap"></i><span class="px-3">Mes salons</span>
            </a>
            <ul class="dropdown-menu fs-sm-4 shadow" aria-labelledby="dropdown">
              <li><a class="dropdown-item" href="#">INM5151</a></li>
              <li><a class="dropdown-item" href="#">INF5153</a></li>
              <li><a class="dropdown-item" href="#">INF5130</a></li>
              <li><a class="dropdown-item" href="#">INM6000</a></li>
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
import jQuery from "jQuery";

export default {
  name: "SideBar",
  mounted() {
    this.$nextTick(() => {
      jQuery('.SideBar').ready(function () {
        jQuery('#sidebarCollapse').on('click', function () {
          jQuery('#sidebar').toggleClass('active');
          jQuery(this).toggleClass('active');
        });
      });
    });
  }
}
</script>

<style>

.title-nav-user {
  margin: auto auto!important;
  border-bottom: 1px solid black;
}

.nav-link a, i, span {
  color: black;
}

.nav-link.dropdown-toggle {
  color: black;
}

</style>