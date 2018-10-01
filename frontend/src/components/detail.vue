<template >
  <div id="app">
      <h2>{{this.url}}</h2>
  <h1 v-if="authenticated()">backend response message: {{this.errors}}</h1>

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
      message: {
          poster: "gladyschanmail@gmail.com",
          accommodation_name: "house",
          accommodation_description: "big house",
          house_rules: null,
          booking_rules: null,
          base_price: null,
          num_guests: null,
          num_bedrooms: null,
          num_bathrooms: null,
          suburb: null,
          state: null,
          country: null,
          latitude: null,
          longitude: null
     },
    url: "String",
    errors: String
               /*
               {
                    user_name: "gladys",
                    name: "chan",
                    email: "gladyschanmail@gmail.com",
                    profile_pic: null
               }
               */
    }
  },

  mounted () {
      this.url = "http://localhost:8000/get/advertisement/"+ this.$auth.getUserProfile().email.split('@')[0] + "/" + this.$auth.getUserProfile().email.split('@')[1].split('.')[0] +"/"
    axios.get("http://localhost:8000/get/advertisement/"+ this.$auth.getUserProfile().email.split('@')[0] + "/" + this.$auth.getUserProfile().email.split('@')[1].split('.')[0] +"/")
    .then(response => {
      // JSON responses are automatically parsed.
      this.errors = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })
  }

/*
  mounted () {
    axios.post("http://localhost:8000/post/advertisement/"+this.$auth.getUserProfile().email.split('@')[0] + "/" + this.$auth.getUserProfile().email.split('@')[1].split('.')[0]+"/update/", {body:this.message})
    .then(response => {
      // JSON responses are automatically parsed.
      this.message = response.data
    })
  }
*/

}

</script>

<style lang="css">
</style>
