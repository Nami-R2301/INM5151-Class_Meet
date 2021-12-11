<template>
  <div id="sidebar">
    <div class="col-auto">
      <div
          class="align-items-sm-start mx-2 min-vh-100">
        <ul class="nav flex-column fw-bold mx-auto mt-2 col-auto" style="font-size: medium"
            id="menu">
          <li class="navbar-brand col-auto mb-3">
            <a href="/profile#dashboard" data-bs-toggle="collapse" class="nav-link px-sm-0 px-2">
              <i class="fs-1 mx-auto bi-person-circle"></i><span
                class="fs-3 text-black text-decoration-underline ms-3">Nami R.</span>
              <p class="small mt-0 my-auto me-auto ms-5 ps-2" style="font-size: 0.95rem; color: #2b2b2b">DD/MM/YYYY HH:MM:SS</p>
            </a>
          </li>
          <li role="separator" class="dropdown-divider">
          </li>
          <li class="nav-item col-auto mb-3">
            <a href="/profile#dashboard" data-bs-toggle="collapse" class="nav-link px-sm-0 px-2">
              <i class="fs-3 bi-clipboard-data"></i><span class="px-3">Tableau de bord</span> </a>
          </li>
          <li class="nav-item col-auto mb-3">
            <a href="/profile#parcours" class="nav-link px-sm-0 px-2">
              <i class="fs-3 bi-table"></i><span class="px-3">Mon parcours</span></a>
          </li>
          <li class="nav-item col-auto dropdown mb-3">
            <a href="#" class="nav-link dropdown-toggle px-sm-0 px-1" role="button"
               aria-expanded="false">
              <i class="fs-3 bi-bootstrap"></i><span class="px-3">Mes salons</span>
            </a>
            <ul class="dropdown-menu fs-sm-4 shadow" aria-labelledby="dropdown">
              <li><a class="dropdown-item" href="#">INM5151</a></li>
              <li><a class="dropdown-item" href="#">INF5153</a></li>
              <li><a class="dropdown-item" href="#">INF5130</a></li>
              <li><a class="dropdown-item" href="#">INM6000</a></li>
              <li>
                <hr class="dropdown-divider mt-2">
              </li>
            </ul>
          </li>
          <li>
            <a href="#" class="nav-link px-sm-0 px-2 mb-3">
              <i class="fs-3 bi-telephone-outbound"></i><span class="px-3">Contactez une personne</span></a>
          </li>
          <li>
            <a href="#" class="nav-link px-sm-0 px-2 mb-3">
              <i class="fs-3 bi-people"></i><span class="px-3">Déconnexion</span> </a>
          </li>
        </ul>
        <hr>
      </div>
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

.nav-link a, i, span {
  color: black;
}

.nav-link.dropdown-toggle {
  color: black;
}

</style>