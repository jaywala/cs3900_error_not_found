<template >
  <div id="app" class="container content" style = "margin-top: 100px">
  <b-alert variant="success"
        dismissible
        :show="showDismissibleAlert"
        @dismissed="showDismissibleAlert=false">
    Successfully Updated!
  </b-alert>
  <md-field>
      <label>Given name</label>
      <md-input v-model="message.given_name"></md-input>
    </md-field>
    <md-field>
      <label>Family name</label>
      <md-input v-model="message.family_name"></md-input>
    </md-field>
    <md-field>
      <label>E-mail (Read-Only)</label>
      <md-input v-model="message.email" readonly></md-input>
    </md-field>
    <md-button class="md-dense md-raised md-primary" @click = "submit()">submit</md-button>
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
    // submit changing
    submit(){
      axios.post('http://localhost:8000/post/user/update/',{body:this.message})
      this.showDismissibleAlert = true;

    }
  },
  data () {
    return {
      showDismissibleAlert: false,
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
    axios.get(this.url,{params:{email:this.$auth.getUserProfile().email}})
    .then(response => {
      // JSON responses are automatically parsed.
      console.log(response.data)
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
