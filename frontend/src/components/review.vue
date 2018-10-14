<template>
  <div>
    <h1>all the bookings</h1>
    <div v-for="book in bookings" class="col-md-4">
      <h3>{{book.title}}</h3>
      <h4>{{book.status}}</h4>
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
    </div>
    {{this.radio}}
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

      axios.get()
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
