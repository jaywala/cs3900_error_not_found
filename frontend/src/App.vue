<template>
  <div>
    <button
      class="btn btn-primary btn-margin"
      v-if="!authenticated"
      @click="login()">
      Log In
    </button>



    <button
      class="btn btn-primary btn-margin"
      v-if="authenticated"
      @click="logout()">
      Log Out
    </button>


    <router-link to="/newbook" v-if = "authenticated">add room</router-link>
    <router-view></router-view>

    <br>
  </div>
</template>
<script>
import AuthService from './auth/AuthService'
import axios from 'axios'
import HelloWorld from './components/HelloWorld.vue'
import newbook from '@/components/newbook.vue'
const API_URL = 'http://localhost:8000'
const auth = new AuthService()

export default {
  name: 'app',
  data () {
    this.handleAuthentication()
    this.authenticated = false

    auth.authNotifier.on('authChange', authState => {
      this.authenticated = authState.authenticated
    })
    return {
      authenticated: false,
      message: ''
    }
  },
  components: {HelloWorld},
  methods: {
    // this method calls the AuthService login() method
    login () {
      auth.login()
      //this.$router.push('helloworld')
    },
    handleAuthentication () {
      auth.handleAuthentication()
    },
    logout () {
      auth.logout()
    }
  }
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
