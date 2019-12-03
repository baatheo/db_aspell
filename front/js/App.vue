<template>
  <div>
    <Navbar/>
    <main class="section">
      <router-view></router-view>
    </main>
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
  main.section {
    min-height: calc(100vh - 220px);
  }
</style>
