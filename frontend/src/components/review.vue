<template>
  <div>
    <h1 style = "margin-top: 100px;">all the bookings</h1>
    {{bookings}}
    <div v-for="(book,n) in bookings" class="col-md-4">
      <md-card md-with-hover>
      <md-ripple>
        <md-card-header>
          <div class="md-title">{{book.event.booking_status}}</div>
          <div class="md-subhead">{{book.ad.accommodation_name}}</div>
          <div class="md-subhead">from:{{book.event.start_day}} to:{{book.event.end_day}}</div>
        </md-card-header>

        <md-card-content>
          <div v-if="book.event.booking_status != 'finished'">
              <md-radio v-model="reviews[n].radio" value="1" hidden>1</md-radio>
              <md-textarea v-model="reviews[n].textarea" value = "dommm" hidden></md-textarea>
          </div>
          <div v-if = "book.event.booking_status == 'finished'">
            <md-radio v-model="reviews[n].radio" value="1">1</md-radio>
            <md-radio v-model="reviews[n].radio" value="2">2</md-radio>
            <md-radio v-model="reviews[n].radio" value="3">3</md-radio>
            <md-radio v-model="reviews[n].radio" value="4">4</md-radio>
            <md-radio v-model="reviews[n].radio" value="5">5</md-radio>
            <md-field>
          <label>Textarea</label>
          <md-textarea v-model="reviews[n].textarea"></md-textarea>
          </md-field>
          </div>
        </md-card-content>
        <md-card-actions>
          <router-link :to="{ name: 'detailpage', params: { poster_id:book.ad.poster_id, ad_id:book.ad.ad_id } }" ><md-button class="md-primary md-raised">View</md-button></router-link>
          <md-button class=" md-raised" type="button" name="button" @click = "cancelbooking(book.title)">cancel</md-button>
        </md-card-actions>
      </md-ripple>
    </md-card>
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
      bookings : [
          {
            status:"finished",
            title:"finished",
          },
          {
            status:"commited",
            title:"commited",
          }
      ],
      reviews:[],
    }
  },

  mounted () {

      axios.get('http://localhost:8000/get/bookersBooking/',{params:{booker:router.app.$auth.getUserProfile().email}})
       .then(response => {
           // JSON responses are automatically parsed.
           console.log(response.data)
           this.bookings = response.data
           for (var i = 0; i < response.data.length; i ++ ){
              var newdd = {textarea:null,radio:null}
              this.reviews.push(newdd)
            }
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
