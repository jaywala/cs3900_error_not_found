<template >
  <div id="app">
    <!--<small v-if="authenticated()">backend response message: {{this.message}}</small>-->

    <div class="container" style="">
      <div class="row">

      </div>
      <div class="row">
        <div class="col-8">
          <small>&lt;{{this.message.property_type}}&gt;</small>

          <div class="row">
            <div class="col-9">
              <h1>{{this.message.accommodation_name}}</h1>
              <small>{{this.message.suburb}}</small>
              <div style="">
                <div style="margin-right: 16px;">{{this.message.num_guests}}guests</div>
                <div style="margin-right: 16px;">{{this.message.num_bedrooms}} bed</div>
                <div style="margin-right: 16px;">{{this.message.num_bathrooms}} bath</div>
              </div>
              <br>
              <p>{{this.message.accommodation_description}}</p>
              <p>{{this.message.amenities}}</p>

            </div>

            <div v-for="review in reviews">
              <li>{{review.rating}}</li>
            </div>

            <div class="col-3">
              <p>Profile image</p>
              <small>host name</small>
            </div>
          </div>
        </div>
        <div class="col-4">
          <PropertyBookingForm></PropertyBookingForm>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import router from '../router'
import auth from '../auth'

import PropertyBookingForm from './PropertyBookingForm.vue'

export default {
    components: {
        PropertyBookingForm,
    },
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
              poster: "Colleen@example.com",
              list_of_reviews: "1,",
              list_of_events: "",
              list_of_images: "1,2,3,4,5,6,7,8,9,10,",
              accommodation_name: "An Oasis in the City",
              accommodation_description: "Very  Quay ",
              property_type: "Apartment",
              house_rules: "Be considerate. No showering after 2330h.",
              booking_rules: "no cancellation",
              amenities: "TV,Kitchen,Elevator,Buzzer/wireless intercom,Heating,Washer,Smoke detector,Fire extinguisher,Essentials,Hangers,Hair dryer,Iron,Bed linens,Extra pillows and blankets,Microwave,Refrigerator,Dishwasher,Dishes and silverware,Cooking basics,Stove,Single level home,Patio or balcony,Garden or backyard",
              base_price: 65,
              num_guests: 1,
              num_bedrooms: 1,
              num_bathrooms: 0,
              address: "Potts Point",
              city: "Potts Point, Australia",
              zip_code: "2011",
              latitude: -33.86916827,
              longitude: 151.2265622
            },
            reviews: "hello",
        }
    },

    mounted () {
        axios.get("http://localhost:8000/get/advertisement"+ this.$router.currentRoute.path+'/')
        .then(response => {
            // JSON responses are automatically parsed.
            this.message = response.data
        })
        .catch(e => {
            this.errors.push(e)
        })
        axios.get("http://localhost:8000/get/review"+ this.$router.currentRoute.path+'/')
        .then(response => {
            // JSON responses are automatically parsed.
            this.reviews = response.data
        })
    }

}

</script>

<style lang="css">
</style>
