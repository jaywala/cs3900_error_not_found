<template >
  <div id="app">
  <h1 v-if="authenticated()">backend response message: {{this.message}}</h1>

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
    data () {
        return {
            message:
            /*{
                ad_id : 1,
                poster : "gladyschanmail@gmail.com",
                accommodation_name : "circus",
                accommodation_description : "very high in a tree",
                house_rules : "don't jump out the window",
                booking_rules : "tralalala",
                amenities : "TV,Kitchen,Elevator, Garden or backyard",
                base_price : 65,
                num_guests : 1,
                num_bedrooms : 1,
                num_bathrooms : 0,
                suburb : "Potts Point",
                state : "NSW",
                country : "Australia",
                latitude : -33.86916827,
                longitude : 151.2265622,
                list_of_reviews : "",
                list_of_events : "",
            },*/
            /*
            {
                id : 1,
                user_name : "Gladys",
                name : "Bip Boop",
                email : "gladyschanmail@gmail.com",
                profile_pic : null,
                list_of_ads : "",
            },
            */
            {
                "id": 1,
                "rev_id": 1,
                "rating": 10,
                "message": "hi there good",
                "ad_owner": "gladyschanmail@gmail.com",
                "ad_id": 1
            }

        }
    },

    mounted () {
        axios.get("http://localhost:8000/get/review/"+ this.$auth.getUserProfile().email.split('@')[0] + "/" + this.$auth.getUserProfile().email.split('@')[1].split('.')[0] +"/1/")
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
        axios.post("http://localhost:8000/post/advertisement/create/", {body:this.message})
    }
*/

}

</script>

<style lang="css">
</style>
