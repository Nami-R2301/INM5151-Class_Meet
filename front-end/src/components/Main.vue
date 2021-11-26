<template>
  <div class="container-fluid">
    <div class="row align-content-center text-center" style="background-color: #f2f5f8">
      <div class="col-12">
        <a class="navbar-brand" href="#"
           title="Cliquez ici pour rafraichir la page principale">
          <img class="logo" alt="logo Class Meet" src="../assets/logo.png">
          <img class="class_Meet" alt="Class Meet" src="../assets/Class_Meet.png"></a>
      </div>
    </div>
    <div class="row flex-nowrap section">
      <div class="col-6" style="margin-top: 2%">
        <img class="image-description-left" style="max-width: 80%" src="../assets/question-mark.jpg" title="question-mark"
             alt="Une image avec un point d'interrogation sur un tableau de craie.">
      </div>
      <div class="col-6">
        <h2 class="titre-section">Qu'est ce que c'est ?</h2>
        <p class="description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras efficitur libero tortor, at
          faucibus dolor ullamcorper vitae. Mauris turpis turpis, mollis eu purus quis, tristique iaculis ligula.
          Vestibulum tempor diam eget purus malesuada, non varius elit pretium. Morbi ornare convallis fringilla.
          Vivamus a finibus dui, non faucibus sem. Pellentesque vel eros non risus tristique rutrum a non nisi. Class
          aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.</p>
      </div>
    </div>
    <div class="solid text-center"><hr></div>
    <div class="row flex-nowrap section">
      <div class="col-4" style="margin-top: 2%">
         <h2 class="titre-section">Qu'est ce que c'est ?</h2>
        <p class="description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras efficitur libero tortor, at
          faucibus dolor ullamcorper vitae. Mauris turpis turpis, mollis eu purus quis, tristique iaculis ligula.
          Vestibulum tempor diam eget purus malesuada, non varius elit pretium. Morbi ornare convallis fringilla.
          Vivamus a finibus dui, non faucibus sem. Pellentesque vel eros non risus tristique rutrum a non nisi. Class
          aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.</p>
      </div>
      <div class="col-8">
        <img class="img-fluid" src="../assets/question-mark.jpg" title="question-mark"
             alt="Une image avec un point d'interrogation sur un tableau de craie.">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Main"
}
</script>

<style scoped>

img:hover {
    opacity: 0.45;
}

.image-intro {
    position: relative;
    min-width: 10%;
    width: 50%;
    max-width: 80%;
    max-height: 42.7%;
    margin-bottom: 25px;
}

h1, h2, h3, h4 {
    position: relative;
    width: 100%;
    margin: 8% 0 5% 0;
    text-align: center;
    font-size: 140%;
    font-weight: bold;
    font-family: "Candara Light", Cambria, serif;
}

h2 {
    margin: 8% 0 0 20%;
    text-align: left;
}

h3 {
    margin: 8% 0 5% 20%;
    text-align: left;
}

.description {
    position: relative;
    max-width: 60%;
    margin-left: 20%;
    text-align: left;
    font-size: 115%;
    font-weight: lighter;
    line-height: 150%;
}

.image-description-right {
    float: right;
    position: relative;
    width: 50%;
    height: 40%;
    margin: 0 0 5% 5%;
    overflow: auto;
}

.image-description-middle {
    float: left;
    position: relative;
    width: 50%;
    height: auto;
    margin: 5% 0 4% 8%;
}

.image-description-left {
    float: left;
    position: relative;
    width: 80%;
    height: auto;
    margin: 5% 0 5% 8%;
    overflow: auto;
}


.solid {
  display: flex;
  margin: 0 30% 0 30%;
  text-align: center;
  align-items: center;
  justify-content: center;
  border-top: 3px solid #bbb;
}

.logo {
  margin: 2.5% 0;
  max-width: 35%;
}

.class_Meet {
  max-width: 45%;
  margin: 2% 2%;
}

.section {
  display: grid;
  margin: 5%;
}

.titre-section {
  margin: 2% 2%;
  text-align: center;
  justify-content: center;
  color: black;
  font-family: "Prompt", Helvetica, Arial, serif;
  font-size: 300%;
  font-weight: bolder;
}

.description {
  margin: 2% 2%;
  text-align: left;
  color: black;
  font-family: Sen, Helvetica, Arial, serif;
  font-size: large;
  font-weight: bolder;
}

</style>