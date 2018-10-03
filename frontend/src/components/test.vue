<template>
  <div>
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

  data() {
    return {
      message :
          {
              "ad_id": 1,
              "poster": "Joe@example.com",
              "accommodation_name": "Wow factor Harbour & Fire works",
              "accommodation_description": "Lifestyle",
              "house_rules": "No pets  No smoking indoors (balcony) No stiletto shoes indoors.",
              "booking_rules": "",
              "amenities": ",Elevator,Buzzer/wireless intercom,Heating,Family/kid",
              "base_price": 275.0,
              "num_guests": 1,
              "num_bedrooms": 1,
              "num_bathrooms": 0,
              "suburb": "Darlinghurst",
              "state": "NSW",
              "country": "Australia",
              "latitude": -33.87734192,
              "longitude": 151.2209494,
              "list_of_reviews": "",
              "list_of_events": ""
          }
    }
  },

  mounted () {

      axios.get("http://localhost:8000/get/advertisement/"+ this.$auth.getUserProfile().email.split('@')[0] + "/" + this.$auth.getUserProfile().email.split('@')[1].split('.')[0])
       .then(response => {
           // JSON responses are automatically parsed.
           this.message = response.data
       })
       .catch(e => {
           this.errors.push(e)
       })
       console.log(this.message)
   }
/*
    mounted () {
       axios.post("http://localhost:8000/post/review/create/", {body:this.message})
   }
*/
}

</script>
<style src="./icon.css"></style>
