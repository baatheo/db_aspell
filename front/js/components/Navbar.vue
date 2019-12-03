<template>
  <nav class="navbar is-dark" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="https://github.com/baloo1379/db_aspell">
        <div class="logo"></div>
      </a>

      <a
        role="button"
        class="navbar-burger burger"
        v-bind:class="{'is-active' : isActive}"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarBasicExample"
        @click="toggleMenu"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu" v-bind:class="{'is-active': isActive}">
      <div class="navbar-end">
        <router-link class="navbar-item" to="/" exact>Home</router-link>
      </div>
      -
    </div>
  </nav>
</template>

<script>
    export default {
        name: "Navbar",
        data() {
            return {
                isActive: false
            };
        },
        methods: {
            toggleMenu() {
                this.isActive = !this.isActive;
            }
        }
    };
</script>

<style>
  .logo {
    width: 28px;
    height: 28px;
    background-image: url("https://www.gravatar.com/avatar/5ae4bdd28eb0082052d7cfa1fcd275af");
    background-size: cover;
  }
</style>
