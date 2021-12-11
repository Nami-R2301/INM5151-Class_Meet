<template>
  <div id="sidebar">
        <div class="col-auto">
          <div
              class="d-flex flex-column align-items-sm-start min-vh-100 mx-2">
            <ul class="nav fw-bold mx-auto mt-2 col-auto"
                id="menu">
              <li class="nav-item col-auto mb-3">
                <a href="/profile#dashboard" data-bs-toggle="collapse" class="nav-link px-sm-0 px-2">
                  <i class="fs-5 bi-clipboard-data"></i><span class="text-responsive px-3 d-sm-inline">Tableau de bord</span> </a>
              </li>
              <li class="nav-item col-auto mb-3">
                <a href="/profile#parcours" class="nav-link px-sm-0 px-2">
                  <i class="fs-5 bi-table"></i><span class="text-responsive px-3 d-sm-inline">Mon parcours</span></a>
              </li>
              <li class="nav-item col-auto dropdown mb-3">
                <a href="#" class="nav-link dropdown-toggle px-sm-0 px-1" role="button"
                   aria-expanded="false">
                  <i class="fs-5 bi-bootstrap"></i><span class="px-3 d-sm-inline">Mes salons</span>
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
                  <i class="bi-telephone-outbound"></i><span class="px-3 d-sm-inline">Contactez une personne</span></a>
              </li>
              <li>
                <a href="#" class="nav-link px-sm-0 px-2 mb-3">
                  <i class="fs-5 bi-people"></i><span class="px-3 d-sm-inline">Déconnexion</span> </a>
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

.text-responsive {
  font-size: calc(100% + 1vw + 1vh);
}

</style>