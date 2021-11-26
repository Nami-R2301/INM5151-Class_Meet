<template>
  <div class="container-fluid">
    <div class="row align-content-center text-center" style="background-color: #f2f5f8;">
      <div class="col-12">
        <a class="navbar-brand" href="#"
           title="Cliquez ici pour rafraichir la page principale">
          <img class="logo col-2" alt="logo Class Meet" src="../assets/logo.png">
          <img class="class_Meet col-2" alt="Class Meet" src="../assets/Class_Meet.png"></a>
      </div>
    </div>
    <div class="row flex-nowrap my-5 section" style="margin-top: 2%">
      <div class="offset-1 col-5">
        <img class="image-description-left" src="../assets/questions.png" title="question-mark"
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
    <div class="solid text-center">
      <hr>
    </div>
    <div class="row flex-nowrap my-5 section">
      <div class="offset-1 col-6">
        <h2 class="titre-section">Faite appel à vos camarades</h2>
        <p class="description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras efficitur libero tortor, at
          faucibus dolor ullamcorper vitae. Mauris turpis turpis, mollis eu purus quis, tristique iaculis ligula.
          Vestibulum tempor diam eget purus malesuada, non varius elit pretium. Morbi ornare convallis fringilla.
          Vivamus a finibus dui, non faucibus sem.</p>
      </div>
      <div class="col-5">
        <img class="image-description-right img-fluid" src="../assets/students.png" title="question-mark"
             alt="Une image avec un point d'interrogation sur un tableau de craie.">
      </div>
    </div>
    <div class="solid text-center">
      <hr>
    </div>
    <div class="row flex-nowrap my-5 section">
      <div class="offset-1 col-5">
        <img class="offset-2" style="max-width: 40%;" src="../assets/parcours.png" title="question-mark"
             alt="Une image avec un point d'interrogation sur un tableau de craie.">
      </div>
      <div class="col-6">
        <h2 class="titre-section">Accéder à votre parcours</h2>
        <p class="description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras efficitur libero tortor, at
          faucibus dolor ullamcorper vitae. Mauris turpis turpis, mollis eu purus quis, tristique iaculis ligula.
          Vestibulum tempor diam eget purus malesuada, non varius elit pretium. Morbi ornare convallis fringilla.
          Vivamus a finibus dui, non faucibus sem. Pellentesque vel eros non risus tristique rutrum a non nisi. Class
          aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.</p>
      </div>
    </div>
    <div class="solid text-center">
      <hr>
    </div>
    <div class="row flex-nowrap my-5 section" style="margin-top: 2%">
      <div class="offset-1 col-6">
        <h2 class="titre-section">Rejoigner des salles étudiantes pour vous entraîdez</h2>
        <p class="description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras efficitur libero tortor, at
          faucibus dolor ullamcorper vitae. Mauris turpis turpis, mollis eu purus quis, tristique iaculis ligula.
          Vestibulum tempor diam eget purus malesuada, non varius elit pretium. Morbi ornare convallis fringilla.
          Vivamus a finibus dui, non faucibus sem. Pellentesque vel eros non risus tristique rutrum a non nisi. Class
          aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.</p>
      </div>
      <div class="col-5">
        <img class="image-description-right offset-2" style="max-width: 50%;" src="../assets/voice-chat.png"
             title="question-mark"
             alt="Une image avec un point d'interrogation sur un tableau de craie.">
      </div>
    </div>
    <div class="solid text-center">
      <hr>
    </div>
    <div class="row flex-nowrap my-5 section">
      <div class="offset-1 col-5">
        <img class="offset-2" style="max-width: 40%;" src="../assets/contacts.png" title="question-mark"
             alt="Une image avec un point d'interrogation sur un tableau de craie.">
      </div>
      <div class="col-6">
        <h2 class="titre-section">Suivez le cheminement de vos camarades et contacts</h2>
        <p class="description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras efficitur libero tortor, at
          faucibus dolor ullamcorper vitae. Mauris turpis turpis, mollis eu purus quis, tristique iaculis ligula.
          Vestibulum tempor diam eget purus malesuada, non varius elit pretium. Morbi ornare convallis fringilla.
          Vivamus a finibus dui, non faucibus sem. Pellentesque vel eros non risus tristique rutrum a non nisi. Class
          aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.</p>
      </div>
    </div>
    <div class="solid text-center">
      <hr>
    </div>
    <div class="container-fluid text-center justify-content-center align-content-center"
         style="background-color: #f2f5f8; margin-bottom: -15%; padding: 0">
      <div class="row flex-nowrap my-5 section">
        <div class="col-12">
          <h2 class="titre-section" style="margin: 0 auto; text-align: center;">Vous êtes partant?</h2>
        </div>
      </div>
      <div class="row">
        <a href="/login" title="Connectez-vous" role="button" class="btn btn-primary">Connectez-vous</a>
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


.container-fluid {
  margin-bottom: 5%;
}

a[role=button] {
  margin: 0 auto 5% auto;
  max-width: 15%;
  color: #06b8f6;
  border: none;
  font-size: 125%;
  background-color: #ffffff;
  text-align: center;
}

img:hover {
  opacity: 0.45;
}

h1, h2, h3, h4 {
  width: 100%;
  text-align: center;
  font-size: 140%;
  font-weight: bold;
  font-family: "Candara Light", Cambria, serif;
}

h2 {
  text-align: left;
}

h3 {
  margin: 8% 0 5% 20%;
  text-align: left;
}

.description {
  margin-right: 15%;
  text-justify: auto;
  font-size: 115%;
  font-weight: lighter;
  line-height: 150%;
}

.image-description-right {
  height: auto;
  max-width: 80%;
  overflow: hidden;
}

.image-description-left {
  float: left;
  position: relative;
  max-width: 80%;
  height: auto;
  overflow: auto;
}


.solid {
  display: flex;
  margin: 5% 30% 5% 30%;
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
}

.titre-section {
  text-align: left;
  margin-bottom: 5%;
  margin-left: -5%;
  justify-content: center;
  color: black;
  font-family: "Prompt", Helvetica, Arial, serif;
  font-size: 300%;
  font-weight: bolder;
}


</style>