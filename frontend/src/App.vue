<template>
    <div id = "app">
        <!-- Bootstrap core CSS -->
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" rel="stylesheet">

        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.4.1/css/all.css" integrity="sha384-5sAR7xN1Nv6T6+dT2mhtzEpVJvfS3NScPQTrOxhwjIuvcA67KV2R5Jz6kr4abQsz" crossorigin="anonymous">

        <!-- Custom styles for this template -->
        <link href="./components/album.css" rel="stylesheet">

        <header hidden>
          <div class="collapse bg-dark" id="navbarHeader">
            <div class="container">
              <div class="row">
                <div class="col-sm-8 col-md-7 py-4">
                  <h4 class="text-white">About</h4>
                  <p class="text-muted">Add some information about the album below, the author, or any other background context. Make it a few sentences long so folks can pick up some informative tidbits. Then, link them off to some social networking sites or contact information.</p>
                </div>
                <div class="col-sm-4 offset-md-1 py-4">
                  <h4 class="text-white">Contact</h4>
                  <ul class="list-unstyled">
                    <li><a href="#" class="text-white">Follow on Twitter</a></li>
                    <li><a href="#" class="text-white">Like on Facebook</a></li>
                    <li><a href="#" class="text-white">Email me</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="navbar navbar-dark navbar-static-top bg-dark box-shadow" style="position: fixed; width: 100%;">
            <div class="container d-flex justify-content-between" >
              <a href="/" class="navbar-brand d-flex align-items-center">
                <i class="fas fa-home fa-2x fa-flip-vertical"></i>
                <strong>&nbsp;NotAirbnb</strong>
              </a>

              <div class="navbar-right">
                
                <a class="align-items-center">
                  <i class="fas fa-search fa-2x"></i>
                </a>
                <b-dropdown id="ddown1" variant="link" no-caret>
                  <template slot="button-content">
                    <i class="fas fa-chevron-circle-down fa-2x"></i><span class="sr-only">Search</span>
                  </template>
                
                  <router-link to="/search" v-if="authenticated()" tag="b-dropdown-item">Search</router-link>
                  <router-link to="/manage/" v-if="authenticated()" tag="b-dropdown-item">Manage properties</router-link>
                  <router-link to="/newbook" v-if="authenticated()" tag = "b-dropdown-item">Add property</router-link>
                  <router-link to="/review" v-if="authenticated()" tag = "b-dropdown-item">review bookings</router-link>
                  <router-link to="/editprofile" v-if="authenticated()" tag = "b-dropdown-item">edit profile</router-link>

                  <b-dropdown-divider></b-dropdown-divider>

                  <b-dropdown-item class="btn btn-primary btn-margin" v-if="!authenticated()" @click="login()">
                    Log In
                  </b-dropdown-item>
                  <b-dropdown-item class="btn btn-primary btn-margin" v-if="authenticated()" @click="logout()">
                    Log Out
                  </b-dropdown-item>
                </b-dropdown>
              </div>
              
            </div>
          </div>
        </header>


        <b-navbar class="navbar-static-top" toggleable="md" type="dark" variant="info" style="position: fixed; width: 100%;">

          <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

              <a href="/" class="navbar-brand d-flex align-items-center">
                <i class="fas fa-home fa-2x fa-flip-vertical" style="color:#7B414C"></i>
                <strong style="color:#7B414C">&nbsp;NotAirbnb</strong>
              </a>

          <b-collapse is-nav id="nav_collapse">

            <b-navbar-nav>
              <b-nav-item href="/" style="color:antiquewhite">Link</b-nav-item>
              <b-nav-item href="#" style="color:antiquewhite" disabled>Disabled</b-nav-item>
            </b-navbar-nav>

            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">

              <b-nav-item href="/search/"><i class="fas fa-search fa-1x" style="color:antiquewhite"></i></b-nav-item>

              <b-nav-item href="/trips/">Trips</b-nav-item>
              <b-nav-item href="/help/">Help</b-nav-item>

              <b-nav-item-dropdown right no-caret>
                <!-- Using button-content slot -->
                <template slot="button-content">
                  <div v-if="authenticated()">
                    <em>{{ user.email }}</em>
                  </div>
                  <div v-else>
                    <em>User</em>
                  </div>
                </template>

                  <router-link to="/manage/" v-if="authenticated()" tag="b-dropdown-item">Manage properties</router-link>
                  <router-link to="/newbook" v-if="authenticated()" tag = "b-dropdown-item">Add property</router-link>
                  <router-link to="/editprofile" v-if="authenticated()" tag = "b-dropdown-item">edit profile</router-link>

                  <b-dropdown-divider></b-dropdown-divider>
                  <b-dropdown-item class="btn btn-primary btn-margin" v-if="!authenticated()" @click="login()">
                    Log In
                  </b-dropdown-item>
                  <b-dropdown-item class="btn btn-primary btn-margin" v-if="authenticated()" @click="logout()">
                    Log Out
                  </b-dropdown-item>
              </b-nav-item-dropdown>
            </b-navbar-nav>

          </b-collapse>
        </b-navbar>
      <router-view></router-view>
      <br>
        <div class="container">
          <p class="float-right">
            <a href="#">Back to top</a>
          </p>
          
          <p>Developed by Gladys Chan, Zihan Qiu, Jay Motwani and Joseph Hilsberg as part of <a href="http://legacy.handbook.unsw.edu.au/undergraduate/courses/2018/COMP3900.html">COMP3900</a></p>
        </div>
      </header>
    <br>
  </div>
  
</template>

<script>
import Vue from 'vue'
import router from '@/router'

// First, checks if it isn't implemented yet.
if (!String.prototype.format) {
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) { 
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}

export default {
  name: 'App',
  data() {
    return {
      user: null,
    }
  },
  methods: {
    // this method calls the AuthService login() method
    login () {
      router.app.$auth.login()
      //this.$router.push('helloworld')
    },
    authenticated(){
      return router.app.$auth.isAuthenticated()
    },
    logout(){
      router.app.$auth.logout()
    }
  },
  mounted() {
    this.user = router.app.$auth.getUserProfile();
    console.log(this.user);
  }
}
</script>

<style>
.navbar-static-top {
  position: fixed;
  top: 0px;
  z-index: 10000;
}

.content {
  padding-top: 80px;
}

</style>