<template>
  <div>
    <h1 style = "margin-top: 100px;">all the bookings</h1>
    {{bookings}}
    <div v-for="book in bookings" class="col-md-4">
      <md-card md-with-hover>
      <md-ripple>
        <md-card-header>
          <div class="md-title">{{book.booking_status}}</div>
          <div class="md-subhead">from:{{book.start_day}} to:{{book.end_day}}</div>
        </md-card-header>

        <md-card-content>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio. Dolores, sed accusantium quasi non.
        </md-card-content>
        <div class="" v-if="book.status == 'booked'">
          <button type="button" name="button" @click = "cancelbooking(book.title)">cancel</button>
        </div>
        <div v-if = "book.status == 'finished'">
          <md-radio v-model="radio" value="1">1</md-radio>
          <md-radio v-model="radio" value="2">2</md-radio>
          <md-radio v-model="radio" value="3">3</md-radio>
          <md-radio v-model="radio" value="4">4</md-radio>
          <md-radio v-model="radio" value="5">5</md-radio>
          <md-field>
        <label>Textarea</label>
        <md-textarea v-model="textarea"></md-textarea>
        </md-field>
        </div>
        <md-card-actions>
          <md-button>Action</md-button>
          <md-button>Action</md-button>
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
      radio: Number
    }
  },

  mounted () {

      axios.get('http://localhost:8000/get/bookersBooking/',{params:{booker:router.app.$auth.getUserProfile().email}})
       .then(response => {
           // JSON responses are automatically parsed.
           console.log(response.data)
           this.bookings = response.data
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
