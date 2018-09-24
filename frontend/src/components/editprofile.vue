<template >
  <div id="app">
  <h1 v-if="authenticated()">{{this.message}}</h1>
  <h2>hello</h2>
</div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import router from '../router'
import auth from '../auth'
export default {
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
    }
  },
  data () {
    return {
      message: null

    }
  },
  mounted () {
    axios.get("http://localhost:8000/get/"+this.$auth.getUserProfile().nickname+"/")
    .then(response => {
      // JSON responses are automatically parsed.
      this.message = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })


  }
}
</script>

<style lang="css">
</style>
