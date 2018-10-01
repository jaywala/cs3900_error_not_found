<template >
  <div id="app">
      <h2>{{this.url}}</h2>
  <h1 v-if="authenticated()">backend response message: {{this.message}}</h1>

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
          ad_id: 1,
          poster: "gladyschanmail@gmail.com",
          accommodation_name: "mouse and phone",
          accommodation_description: "cold",
          house_rules: "no fires",
          booking_rules: null,
          amenities: null,
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
/*
  mounted () {
      this.url = "http://localhost:8000/get/advertisement/"+ this.$auth.getUserProfile().email.split('@')[0] + "/" + this.$auth.getUserProfile().email.split('@')[1].split('.')[0] +"/"
    axios.get("http://localhost:8000/get/advertisement/"+ this.$auth.getUserProfile().email.split('@')[0] + "/" + this.$auth.getUserProfile().email.split('@')[1].split('.')[0] +"/")
    .then(response => {
      // JSON responses are automatically parsed.
      this.message = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })
  }
*/

  mounted () {
    this.url = "http://localhost:8000/post/advertisement/"+ this.$auth.getUserProfile().email.split('@')[0] + "/" + this.$auth.getUserProfile().email.split('@')[1].split('.')[0] +"/create/"
    axios.post("http://localhost:8000/post/advertisement/"+this.$auth.getUserProfile().email.split('@')[0] + "/" + this.$auth.getUserProfile().email.split('@')[1].split('.')[0] + "/create/", {body:this.message})
  }


}

</script>

<style lang="css">
</style>
