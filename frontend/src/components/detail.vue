<template >
  <div id="app">
  <h1 v-if="authenticated()">{{token()}}</h1>
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
      message: {
    "user": 1,
    "accommodation_name": "shit",
    "accommodation_description": "s to walk to Circular  Quay ",
    "house_rules": "Be considerate.   No showering after 2330h.",
    "booking_rules": "",
    "base_price": 65.0,
    "num_guests": 1,
    "num_bedrooms": 1,
    "num_bathrooms": 0,
    "suburb": "NSW",
    "state": "NSW",
    "country": "Australia",
    "latitude": -33.86916827,
    "longitude": 151.2265622
},
      loading: true,
      errored: false
    }
  },
  mounted () {
    console.log(router.app.$auth.getUserProfile())
    axios.post("http://localhost:8000/api/public/",{body:this.message})



  }
}
</script>

<style lang="css">
</style>
