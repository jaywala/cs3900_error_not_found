<template>
  <div class="callback"></div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import router from '../router'
import auth from '../auth'
export default {
  name: 'callback',
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
      },
      token(){
          return router.app.$auth.getAuthToken()
      },
      get(){
          return router.app.$auth.getUserProfile()
      }
  },
  data() {
    return {
      message: null,
    }
  },
  mounted() {
    this.$auth.handleAuthentication().then((data) => {
      this.message = this.$auth.getUserProfile()
      axios.post("http://localhost:8000/post/userLoggedIn/", {body: this.message})
      this.$router.push({ name: 'home' })
      this.$router.go(this.$router.currentRoute)
    })
  }
}
</script>

<style>
.callback {
  width: 40px;
  height: 40px;
  background-color: #333;

  margin: 100px auto;
  -webkit-animation: sk-rotateplane 1.2s infinite ease-in-out;
  animation: sk-rotateplane 1.2s infinite ease-in-out;
}

@-webkit-keyframes sk-rotateplane {
  0% { -webkit-transform: perspective(120px) }
  50% { -webkit-transform: perspective(120px) rotateY(180deg) }
  100% { -webkit-transform: perspective(120px) rotateY(180deg)  rotateX(180deg) }
}

@keyframes sk-rotateplane {
  0% {
    transform: perspective(120px) rotateX(0deg) rotateY(0deg);
    -webkit-transform: perspective(120px) rotateX(0deg) rotateY(0deg)
  } 50% {
    transform: perspective(120px) rotateX(-180.1deg) rotateY(0deg);
    -webkit-transform: perspective(120px) rotateX(-180.1deg) rotateY(0deg)
  } 100% {
    transform: perspective(120px) rotateX(-180deg) rotateY(-179.9deg);
    -webkit-transform: perspective(120px) rotateX(-180deg) rotateY(-179.9deg);
  }
}
</style>
