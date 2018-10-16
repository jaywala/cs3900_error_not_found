<template >
  <div id="app" class="container content">
  <h1 v-if="authenticated()">{{this.message}}</h1>
  <md-field>
      <label>Initial Value</label>
      <md-input v-model="this.message.given_name"></md-input>
    </md-field>
    <md-field>
      <label>Initial Value</label>
      <md-input v-model="this.message.family_name"></md-input>
    </md-field>
    <md-field>
      <label>Initial Value (Read Only)</label>
      <md-input v-model="this.message.email" readonly></md-input>
    </md-field>
    <md-button class="md-dense md-raised md-primary" @click = "submit()">submit</md-button>
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
    },
    submit(){
      axios.post('http://localhost:8000/post/user/update/',{body:this.message})
    }
  },
  data () {
    return {
      message: {
        "given_name": "George",
        "family_name": "Q",
        "nickname": "georgeq.tsingdao",
        "name": "George Q",
        "picture": "https://lh3.googleusercontent.com/-GzqPoUtimaw/AAAAAAAAAAI/AAAAAAAAAAA/AAN31DUbjbINQTD0Hdh1Pu3wEnZwrujeBQ/mo/photo.jpg",
        "email":"fuck@fuck.com",
       },
      url : null
    }
  },
  mounted () {
    this.url = "http://localhost:8000/get/user/"
    axios.get(this.url,{email:this.$auth.getUserProfile().email})
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
