<template>
  <div>
    <Navbar/>
    <div class="section">
      <router-view></router-view>
    </div>
    <Footer/>
  </div>
</template>

<script>
    import Footer from "./components/Footer";
    import Navbar from "./components/Navbar";

    export default {
        name: "Home",
        components: {Navbar, Footer}
    };
</script>

<style>
</style>
