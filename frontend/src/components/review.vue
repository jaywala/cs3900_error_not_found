<template>
  <div>

    <div  style = "margin-top: 100px;" class="container" v-if="bookings.length < 1">
      <h1>    haven't booked anything</h1>
    </div>
    <div class="" v-else >
      <h1 style = "margin-top: 100px;">all the bookings</h1>
      <div class="" v-for="book in bookings">
          {{book.ad.ad_id}}
      </div>
      {{this.reviews}}
    <div v-for="(book,n) in bookings" class="col-md-10">
      <md-card md-with-hover  style = "margin-top : 20px">
      <md-ripple>
        <md-card-header>
          <div class="md-title"><span class="badge badge-secondary">{{book.event.booking_status}}</span>    {{book.ad.accommodation_name}}</div>
          <div class="md-subhead">from:{{book.event.start_day}} to:{{book.event.end_day}}</div>
        </md-card-header>

        <md-card-content>
          <div class="" v-if="book.event.booking_status == 'booked'">
              you have the change to cancel the booking one day before you arrive
          </div>
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
          <div class="">
              <md-button class="md-raised" @click = "submit(n) v-if = "book.event.booking_status == 'finished'" ">Submit</md-button>
          </div>
        </md-card-content>
        <md-card-actions>
          <router-link :to="{ name: 'detailpage', params: { poster_id:book.ad.poster_id, ad_id:book.ad.ad_id } }" ><md-button class="md-primary md-raised">View</md-button></router-link>
          <md-button v-if="book.event.booking_status == 'booked'" class=" md-raised" type="button" name="button" @click = "cancelbooking(n)">cancel</md-button>
        </md-card-actions>
      </md-ripple>
    </md-card>
    </div>
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
        }, 
        //submit a review
        submit(n){
            axios.post('http://localhost:8000/post/review/create/',{body:this.reviews[n],user:this.$auth.getUserProfile(),event:this.bookings[n]})
        },
        //cancel a booking
        cancelbooking(n){
            axios.post('http://localhost:8000/post/event/delete/',{body:this.bookings[n],user:this.$auth.getUserProfile()})
            .then(response => {
                // JSON responses are automatically parsed.
                console.log(response.data)
                this.bookings = response.data
                for (var i = 0; i < response.data.length; i ++ ){
                   var newdd = {textarea:null,rating:null}
                   this.reviews.push(newdd)
                 }
            })
            .catch(e => {
                this.errors.push(e)
            })
        },
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
           this.bookings = response.data
           for (var i = 0; i < response.data.length; i ++ ){
              var newdd = {textarea:null,rating:null}
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
