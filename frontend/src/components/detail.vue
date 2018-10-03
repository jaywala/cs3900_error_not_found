<template >
  <div id="app">


    <div class="container" style="">
      <div class="row">

      </div>
      <div class="row">
        <div class="col-8">
          <small>&lt;Property Type&gt;</small>

          <div class="row">
            <div class="col-9">
              <h1>&lt;{{this.message.accommodation_name}}&gt;</h1>
              <small>&lt;{{this.message.suburb}}&gt;</small>
              <div style="">
                <div style="margin-right: 16px;">{{this.message.num_guests}}guests</div>
                <div style="margin-right: 16px;">{{this.message.num_bedrooms}} bed</div>
                <div style="margin-right: 16px;">{{this.message.num_bathrooms}} bath</div>
              </div>
              <br>
              <p>&lt;{{this.message.accommodation_description}}&gt;</p>
              <p>&lt;{{this.message.amenities}}&gt;</p>

            </div>
            <div class="col-3">
              <p>&lt;Profile image&gt;</p>
              <small>&lt;host name&gt;</small>
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
            message: null
        }
    },

    mounted () {
        axios.get("http://localhost:8000/get/advertisement"+ this.$router.currentRoute.path.split('@')[0] + "/" + this.$router.currentRoute.path.split('@')[1].split('.')[0] +"/" + this.$router.currentRoute.path.split('@')[1].split('/')[1]+"/")
        .then(response => {
            // JSON responses are automatically parsed.
            this.message = response.data
        })
        .catch(e => {
            this.errors.push(e)
        })
        console.log(this.message)
    }

}

</script>

<style lang="css">
</style>
