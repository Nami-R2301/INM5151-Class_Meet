<template>
  <div id="sidebar">
        <div class="col-auto d-flex">
          <div
              class="d-flex flex-sm-column flex-column align-items-center align-items-sm-start px-3 pt-2 min-vh-100 text-white">
            <ul class="nav nav-pills fw-bold flex-sm-column flex-row flex-nowrap flex-shrink-1 flex-sm-grow-0 flex-grow-1 mb-sm-auto mb-0 justify-content-center align-items-center align-items-sm-start"
                id="menu">
              <li>
                <a href="/profile/dashboard" data-bs-toggle="collapse" class="nav-link px-sm-0 px-2">
                  <i class="fs-5 bi-clipboard-data"></i><span class="text-size ms-1 px-3 d-none d-sm-inline">Tableau de bord</span> </a>
              </li>
              <li>
                <a href="/profile/parcours" class="nav-link px-sm-0 px-2">
                  <i class="fs-5 bi-table"></i><span class="text-size ms-1 px-3 d-none d-sm-inline">Mon parcours</span></a>
              </li>
              <li class="dropdown">
                <a href="#" class="nav-link dropdown-toggle px-sm-0 px-1" id="dropdown" data-bs-toggle="dropdown"
                   aria-expanded="false">
                  <i class="fs-5 bi-bootstrap"></i><span class="text-size ms-1 px-3 d-none d-sm-inline">Mes salons</span>
                </a>
                <ul class="dropdown-menu fs-6 dropdown-menu-dark text-small shadow" aria-labelledby="dropdown">
                  <li><a class="dropdown-item" href="#">INM5151</a></li>
                  <li><a class="dropdown-item" href="#">INF5153</a></li>
                  <li><a class="dropdown-item" href="#">INF5130</a></li>
                  <li><a class="dropdown-item" href="#">INM6000</a></li>
                  <li>
                    <hr class="dropdown-divider">
                  </li>
                </ul>
              </li>
              <li>
                <a href="#" class="nav-link px-sm-0 px-2">
                  <i class="fs-5 bi-grid"></i><span class="text-size ms-1 px-3 d-none d-sm-inline">Contactez une personne</span></a>
              </li>
              <li>
                <a href="#" class="nav-link px-sm-0 px-2">
                  <i class="fs-5 bi-people"></i><span class="text-size ms-1 px-3 d-none d-sm-inline">Déconnexion</span> </a>
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

<style scoped>

ul li a {
  font-family: Sen, Helvetica, Arial, sans-serif;
  color: black;
  margin: 5% auto;
}

.text-size {

}

@media (min-width: 768px) {
  .text-size {
    font-size: small;
  }
}

@media (min-width: 1080px) {
  .text-size {
    font-size: medium;
  }
}
</style>