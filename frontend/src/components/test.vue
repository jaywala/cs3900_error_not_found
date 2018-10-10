<template>
  <div>
    <div class="text-center">

    </div>

    <Slider
    :pagination-visible="true"
    :pagination-clickable = "true"
      :async-data="message"
      direction="horizontal">
    <div v-for="img in message" :key="img.id">
        <img :src="img.pic" alt="">
    </div>
  </Slider>


  </div>
</template>
<script>
//<img src="" alt="" :src="img.pic" v-for="img in message">
import Vue from 'vue'
import axios from 'axios'
import router from '../router'
import auth from '../auth'
import Slider from 'vue-plain-slider'
export default {
  components: {
      Slider
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
      onSlideChangeStart (currentPage, el) {
      console.log('onSlideChangeStart', currentPage, el);
    },
    onSlideChangeEnd (currentPage, el) {
      console.log('onSlideChangeEnd', currentPage, el);
    }
  },

  data() {
    return {
      message: null,
      slickOptions: {
                slidesToShow: 3,
                // Any other options that can be got from plugin documentation
      },
    }
  },

  mounted () {
      axios.get("http://localhost:8000/get/advertisement/images/"+ "Colleen/example/1/")
      .then(response => {
           // JSON responses are automatically parsed.
           this.message = response.data
           console.log(this.message)
       })
       .catch(e => {
           this.errors.push(e)
       })
       console.log(this.message)

   }

/*
    mounted () {
       axios.post("http://localhost:8000/post/image/delete/", {body:this.message})
   }
*/
}

</script>
<style src="./icon.css"></style>
