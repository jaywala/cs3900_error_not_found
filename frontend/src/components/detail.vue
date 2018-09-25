<template >
  <div id="app">
  <h1 v-if="authenticated()">backend response message: {{this.message}}</h1>
  <h2>error message: {{this.error}}</h2>
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
    },
    get(){
      return router.app.$auth.getUserProfile()
    }
  },
  data () {
    return {
      id: {user: 1},
      message: {
                id: 1,
                
               }

    }
  },

  mounted () {
    axios.get("http://localhost:8000/get/user/"+ this.$auth.getUserProfile().email.split('@')[0] + "/" + this.$auth.getUserProfile().email.split('@')[1].split('.')[0] +"/")
    .then(response => {
      // JSON responses are automatically parsed.
      this.message = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })
  }

/*
  mounted () {
    axios.post("http://localhost:8000/post/advertisement/"+this.$auth.getUserProfile().email.split('@')[0] + "/" + this.$auth.getUserProfile().email.split('@')[1].split('.')[0]+"/"+ this.id.user +"/update/", {body:this.info})
    .then(response => {
      // JSON responses are automatically parsed.
      this.info = response.data
    })
  }
*/

}

</script>

<style lang="css">
</style>
