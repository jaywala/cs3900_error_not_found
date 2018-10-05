<template>
  <div>
    <div class="text-center">
      <img src="" alt="" :src="img.pic" v-for="img in message">

      <h1>backend: {{this.message}} </h1>
    </div>
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
      message: /*null*/
                /*
                {"id": 100,
                "email": "gladyschanmail@gmail.com",
                "given_name": "Boop",
                "name": "Gladys Chan",
                "picture": "https://lh5.googleusercontent.com/-tUOv4633lvo/AAAAAAAAAAI/AAAAAAAAAAA/AAN31DXj19KOrdLyLEG7I4P5yrKElyWY0A/mo/photo.jpg",
                "list_of_ads": null,
                "list_of_rentals": null,
                "list_of_posted_reviews": null}
                */
                /*
                {"ad_id": 1,
                "poster": "gladyschanmail@gmail.com",
                "list_of_reviews": "",
                "list_of_events": "",
                "list_of_images": "",
                "title": "igloo",
                "summary": "Very central to Circular  Quay ",
                "propertyType": "Apartment",
                "house_rules": "Be considerate. No showering after 2330h.",
                "booking_rules": "no cancellation",
                "amenities": "chair,TV,Kitchen,Elevator,Buzzer/wireless intercom",
                "base_price": 65.0,
                "nGuests": 1,
                "nBedrooms": 1,
                "nBathrooms": 0.0,
                "address": "Potts Point",
                "city": "Potts Point, Australia",
                "zipCode": "2011",
                "latitude": -33.86916827,
                "longitude": 151.2265622}*/
                /*
                {"id": 1,
                "rev_id": 1,
                "ad_owner": "gladyschanmail@gmail.com",
                "ad_id": 1,
                "rating": 5,
                "message": null}
                */
                {"id": 1,
                "event_id": 1,
                "ad_owner": "gladyschanmail@gmail.com",
                "ad_id": 1,
                "start_day": "2018-10-06",
                "start_day_start_time": "01:15:47",
                "end_day": "2018-10-06",
                "end_day_end_time": "02:15:50",
                "booking_status": "booked",
                "notes": ""}
    }
  },
/*
  mounted () {

      axios.get("http://localhost:8000/get/event/"+ "gladyschanmail/gmail/1/")
      .then(response => {
           // JSON responses are automatically parsed.
           this.message = response.data
       })
       .catch(e => {
           this.errors.push(e)
       })
       console.log(this.message)
   }
*/

    mounted () {
       axios.post("http://localhost:8000/post/event/delete/", {body:this.message})
   }

}

</script>
<style src="./icon.css"></style>
