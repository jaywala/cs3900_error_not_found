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
      message:
                {"id": 100,
                "email": "gladyschanmail@gmail.com",
                "given_name": "Boop",
                "name": "Gladys Chan",
                "picture": "https://lh5.googleusercontent.com/-tUOv4633lvo/AAAAAAAAAAI/AAAAAAAAAAA/AAN31DXj19KOrdLyLEG7I4P5yrKElyWY0A/mo/photo.jpg",
                "list_of_ads": null,
                "list_of_rentals": null,
                "list_of_posted_reviews": null}
    }
  },
/*
  mounted () {

      axios.get("http://localhost:8000/get/user/"+ "gladyschanmail/gmail/")
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
       axios.post("http://localhost:8000/post/user/update/", {body:this.message})
   }

}

</script>
<style src="./icon.css"></style>
