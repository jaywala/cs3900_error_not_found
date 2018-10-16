<template>
  <div>

    <md-table style = "margin: 70px">
      <md-table-row>
        <md-table-head>Name</md-table-head>
        <md-table-head>Email</md-table-head>
        <md-table-head>Request</md-table-head>
      </md-table-row>

      <md-table-row v-for="r in request">
        <md-table-cell>{{r.name}}</md-table-cell>
        <md-table-cell>{{r.email}}</md-table-cell>
        <md-table-cell>{{r.text}}</md-table-cell>
        <md-button class="md-dense md-raised md-primary" v-if="getProfile().email == r.email"@click = "deleter(r)">delete</md-button>
      </md-table-row>


    </md-table>
    <md-field>
      <label>request detail</label>
      <md-textarea v-model="message.detail"></md-textarea>
    </md-field>
    <md-button class="md-dense md-raised md-primary" @click = "submit()">public</md-button>
  </div>
</template>

<script>

import Vue from 'vue'
import router from '../router'
import axios from 'axios'

  export default {
    name: 'TableBasic',
    data: () => ({
      request:[
      ],

      message: {
        name: null,
        email: null,
        detail:null,
      },
    }),
    methods: {
      submit() {
        this.message.name = this.getProfile().nickname
        this.message.email = this.getProfile().email
        axios.post("http://localhost:8000/post/PropertyRequest/create/",{body: this.message})
        .then(response => {
          // JSON responses are automatically parsed.
          console.log(response.data)
          this.request = response.data
        })
        window.setTimeout(() => {
          this.message.detail = null
        }, 150)
      },
      getProfile(){
        return router.app.$auth.getUserProfile()
      },
      deleter(r){
        axios.post("http://localhost:8000/post/PropertyRequest/delete/",{body: r})
        .then(response => {
          // JSON responses are automatically parsed.
          console.log(response.data)
          this.request = response.data
        })
      }
    },
    mounted () {
    axios.get("http://localhost:8000/get/PropertyRequest/")
    .then(response => {
      // JSON responses are automatically parsed.
      console.log(response.data)
      this.request = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })
   },
 }
</script>
