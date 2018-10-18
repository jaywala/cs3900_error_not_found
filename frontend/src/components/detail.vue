<template >
  <div id="app">
    <!--<small v-if="authenticated()">backend response message: {{this.message}}</small>-->

    <div class="container content" style="">
      <div class="row">

      </div>
      <div class="row">
        <div class="col-8">
          <small>{{this.message[0].property_type}}</small>

          <div class="row">
            <div class="col-12">
              <h1>{{this.message[0].accommodation_name}}</h1>
              <small>{{this.message[0].city}}</small>
              <div style="">
                <div class="row">
                  <div style="margin-right: 16px;">{{this.message[0].num_guests}} <i class="fas fa-users"></i></div>
                  <div style="margin-right: 16px;">{{this.message[0].num_bedrooms}} <i class="fas fa-bed"></i></div>
                  <div style="margin-right: 16px;">{{this.message[0].num_bathrooms}} <i class="fas fa-bath"></i></div>
                </div>
              </div>

              <div class="row">
              <Slider
                style="width:100%;max-height:40%"
                :pagination-visible="true"
                :pagination-clickable = "true"
                  :async-data="message[1]"
                  direction="horizontal">
                <div v-for="img in message[1]" :key="img.id">
                    <img :src="img.pic" alt="">
                </div>
              </Slider>
              </div>
              <div class="row" style="padding-top:50px;">
                <h5>Description</h5>
              </div>
              <div class="row">
                <p>{{this.message[0].accommodation_description}}</p>
              </div>
              <hr>
              <div class="row">
                <h5>Amenities</h5>
              </div>
              <div class="row">
                <p>{{this.message[0].amenities}}</p>
              </div>
              <hr>

              <h5>Ratings</h5>
              <small>{{this.avg_rating}}</small>
              <div v-for="n in avg_rating" style="display: inline">
                <i class="fas fa-star"></i>
              </div>
              <div v-for="n in inverse_rating" style="display: inline; margin: -4px;">
                <i class="far fa-star"></i>
              </div>
              <p>
                <div v-for="review in message[3]">
                  <strong>{{ review.reviewer }}</strong>
                  <br>
                  {{ review.message }}
                  <hr>
                </div>
              </p>

            </div>

            <div class="col-3">
              <p>Profile image</p>
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
import Slider from 'vue-plain-slider'

import PropertyBookingForm from './PropertyBookingForm.vue'

export default {
    components: {
        PropertyBookingForm,
        Slider,
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
        },

    },
    data () {
        return {
            errors: [],
            message: {
              ad_id: 1,
              poster: null,
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
            avg_rating: null,
            inverse_rating: null,
        }
    },

    mounted () {

        this.user = this.message.poster;
        //get the advertisement from backend
        axios.get("http://localhost:8000/get/advertisement/single/",
                   {params: this.$router.currentRoute.params}
                 )
        //assign response data to front end data
        .then(response => {
            // JSON responses are automatically parsed.
            console.log(response.data)
            this.message = response.data

          var ratings = this.message[3]

          // Calculate overall rating average.
          var total = 0;
          var i;
          for (i=0; i<ratings.length; i++) {
            total += ratings[i].rating
          }
          //calculate average rating
          if (ratings.length != 0) {
            this.avg_rating = Math.round(total / ratings.length);
            this.inverse_rating = 5 - this.avg_rating
          }

        })
        .catch(e => {
            this.errors.push(e)
            //alert(e)
        })
        /*
        axios.get("http://localhost:8000/get/review"+ this.$router.currentRoute.path+'/')
        .then(response => {
            // JSON responses are automatically parsed.
            this.reviews = response.data
        })*/

    }

}

</script>

<style lang="css">
</style>
