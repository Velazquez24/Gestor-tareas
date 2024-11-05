<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <Mycomponent/>
</template>

<script>
import Mycomponent from './components/mycomponent.vue';

export default {
  name: 'App',
  components: {
  Mycomponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
