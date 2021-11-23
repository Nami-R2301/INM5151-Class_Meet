<template>
  <footer>
    <ul>
      <li><a><img class="class_Meet" alt="Class Meet" src="../assets/Class_Meet.png"></a></li>
      <li class="copyright">&copy; Copyright 2020 Nami's Fix&trade; All Rights Reserved</li>
      <li class="signal"><a>Signaler un problème</a></li>
    </ul>
  </footer>
</template>

<script>
export default {
  name: "Footer"
}
</script>

<style>

footer {
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 0;
  overflow: hidden;
  background-color: aliceblue;
  font-family: Sen, "Times New Roman", serif;
  font-size: 100%;
}

footer li {
  display: block;
  float: left;
  margin: 1% 2% 1% 0;
  list-style-type: none;
  text-align: left;
  color: black;
  font-weight: bolder;
}

.copyright {
  position: center;
  max-width: 40%;
}

.signal {
  max-width: 33%;
  float: right;
  text-align: right;
}

footer a {
  text-decoration: none;
}
</style>