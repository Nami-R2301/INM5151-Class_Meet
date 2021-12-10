<template>
  <div id="sidebar" class="sidebar">
        <div class="col-auto d-flex sticky-top bg-light">
          <div
              class="d-flex flex-sm-column flex-column align-items-center align-items-sm-start px-3 pt-2 min-vh-100 text-white">
            <ul class="nav nav-pills fw-bold flex-sm-column flex-row flex-nowrap flex-shrink-1 flex-sm-grow-0 flex-grow-1 mb-sm-auto mb-0 justify-content-center align-items-center align-items-sm-start"
                id="menu">
              <li>
                <a href="#submenu1" data-bs-toggle="collapse" class="nav-link px-sm-0 px-2">
                  <i class="fs-5 bi-speedometer2"></i><span class=" fs-6 ms-1 px-3 d-none d-sm-inline">Dashboard</span> </a>
              </li>
              <li>
                <a href="#" class="nav-link px-sm-0 px-2">
                  <i class="fs-5 bi-table"></i><span class=" fs-6 ms-1 px-3 d-none d-sm-inline">Orders</span></a>
              </li>
              <li class="dropdown">
                <a href="#" class="nav-link dropdown-toggle px-sm-0 px-1" id="dropdown" data-bs-toggle="dropdown"
                   aria-expanded="false">
                  <i class="fs-5 bi-bootstrap"></i><span class=" fs-6 ms-1 px-3 d-none d-sm-inline">Bootstrap</span>
                </a>
                <ul class="dropdown-menu fs-6 dropdown-menu-dark text-small shadow" aria-labelledby="dropdown">
                  <li><a class="dropdown-item" href="#">New project...</a></li>
                  <li><a class="dropdown-item" href="#">Settings</a></li>
                  <li><a class="dropdown-item" href="#">Profile</a></li>
                  <li>
                    <hr class="dropdown-divider">
                  </li>
                  <li><a class="dropdown-item" href="#">Sign out</a></li>
                </ul>
              </li>
              <li>
                <a href="#" class="nav-link px-sm-0 px-2">
                  <i class="fs-5 bi-grid"></i><span class="fs-6 ms-1 px-3 d-none d-sm-inline">Products</span></a>
              </li>
              <li>
                <a href="#" class="nav-link px-sm-0 px-2">
                  <i class="fs-5 bi-people"></i><span class="fs-6 ms-1 px-3 d-none d-sm-inline">Customers</span> </a>
              </li>
            </ul>
            <hr>
          </div>
        </div>
      </div>
</template>

<script>
export default {
  name: "SideBar"
}
</script>

<style scoped>

ul li a {
  font-family: Sen, Helvetica, Arial, sans-serif;
  color: black;
  margin: 5% auto;
}

.brand {
  color: #06b8f6;
  font-weight: bolder;
  font-size: x-large;
}

.logo {
  margin-right: 5%;
  max-width: 20%;
}

.sidebar {
  border-right: 1px solid black;
}
</style>