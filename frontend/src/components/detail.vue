<template >
  <div id="app">
  <h1 v-if="authenticated()">{{this.message}}</h1>
  <h2>hello</h2>
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
    }
  },
  data () {
    return {
      message:
            {
                user: 3,
                accommodation_name: "Manly Harbour House",
                accommodation_description: "Beautifully renovatedThe front lounge enjoys P&O",
                house_rules: "Standard Terms and Conditions  owners in adv",
                booking_rules: "no running",
                base_price: 471,
                num_guests: 6,
                num_bedrooms: 3,
                num_bathrooms: 3,
                suburb: "Balgowlah",
                state: "NSW",
                country: "Australia",
                latitude: -33.80092903,
                longitude: 151.2617222
            }

    }
  },

  mounted () {
    axios.get("http://localhost:8000/get/user/"+ this.$auth.getUserProfile().email.split('@')[0] + "/" + this.$auth.getUserProfile().email.split('@')[1].split('.')[0] +"/")
    .then(response => {
      // JSON responses are automatically parsed.
      this.message = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })
  }

  /*
  mounted () {
    axios.post("http://localhost:8000/api/get/user/"+this.$auth.getUserProfile().email+"/"+this.message.user+"/", {body:this.message})
  }
  */
}

</script>

<style lang="css">
</style>
