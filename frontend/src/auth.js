import auth0 from 'auth0-js'
import Vue from 'vue'

// use auth0 to handle authentication

//define the auth config
let webAuth = new auth0.WebAuth({
  domain: 'cs3900.au.auth0.com',
  clientID: 'CyF2yOxLafjmlJ75djXxCdeslXo2LU9N',
  // make sure port is 8080
  redirectUri: 'http://localhost:8080/callback',
  // we will use the api/v2/ to access the user information as payload
  audience: 'http://djangovuejs.digituz.com.br',
  responseType: 'token id_token',
  scope: 'openid email profile',
  apiUrl: 'http://localhost:8000/assignment'
})


//define main auth class
let auth = new Vue({
  computed: {
    //id_token used to handle authentication
    token: {
      get: function() {
        return localStorage.getItem('id_token')
      },
      set: function(id_token) {
        localStorage.setItem('id_token', id_token)
      }
    },
    //The Access Token is a credential that can be used by an application to access an API
    accessToken: {
      get: function() {
        return localStorage.getItem('access_token')
      },
      set: function(accessToken) {
        localStorage.setItem('access_token', accessToken)
      }
    },
    //store expire time (around 4 hrs)
    expiresAt: {
      get: function() {
        return localStorage.getItem('expires_at')
      },
      set: function(expiresIn) {
        let expiresAt = JSON.stringify(expiresIn * 1000 + new Date().getTime())
        localStorage.setItem('expires_at', expiresAt)
      }
    },
    //current user (who loggedin)
    user: {
      get: function() {
        return JSON.parse(localStorage.getItem('user'))
      },
      set: function(user) {
        localStorage.setItem('user', JSON.stringify(user))
      }
    }
  },

  methods: {
    login() {
      webAuth.authorize()
    },
    logout() {
      localStorage.removeItem('access_token')
      localStorage.removeItem('id_token')
      localStorage.removeItem('expires_at')
      webAuth.logout()
    },
    isAuthenticated() {
      return new Date().getTime() < this.expiresAt
    },
    handleAuthentication() {
      return new Promise((resolve, reject) => {
        webAuth.parseHash((err, authResult) => {
          if (authResult && authResult.accessToken && authResult.idToken) {
            this.expiresAt = authResult.expiresIn
            this.accessToken = authResult.accessToken
            this.token = authResult.idToken
            this.user = authResult.idTokenPayload
            resolve()
          } else if (err) {
            this.logout()
            reject(err)
          }
        })
      })
    },
    getAuthToken(){
      return localStorage.getItem('access_token');
    },
    getUserProfile () {
      const accessToken = localStorage.getItem('access_token')
      if (accessToken) return this.user
      else return null
    }
  }
})

export default {
  install: function(Vue) {
    Vue.prototype.$auth = auth
  }
}
