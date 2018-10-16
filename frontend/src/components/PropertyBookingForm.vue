<template>


<div class="PropertyBookingForm" style="">
  <b-alert variant="success"
    dismissible
    :show="showSuccess"
    @dismissed="showSuccess=false">
    Your booking has been accepted!
  </b-alert>
  <b-alert variant="danger"
    dismissible
    :show="showError"
    @dismissed="showError=false">
    Your booking could not be accepted!
  </b-alert>
  <md-card>
    <md-card-header>
      <strong><div class="md-title">${{ this.message[0].base_price }}</div></strong>per night
    </md-card-header>
    <md-card-content >
      <md-datepicker v-model="bookdetail.start_day" >
        <label>Check In date</label>
      </md-datepicker>
      <md-datepicker v-model="bookdetail.end_day">
        <label>Check Out date</label>
      </md-datepicker>
      <md-field style="width:180px">
        <label for="nGuests">Number of Guests</label>
        <md-select v-model = "bookdetail.guest"name="nGuests" id="nGuests">
          <md-option value="1">1</md-option>
          <md-option value="2">2</md-option>
          <md-option value="3">3</md-option>
          <md-option value="4">4</md-option>
          <md-option value="5">5</md-option>
          <md-option value="6">6</md-option>
          <md-option value="7">7</md-option>
          <md-option value="8">8+</md-option>
        </md-select>
      </md-field>
      <md-card-actions>
        <md-button type="submit" class="md-primary md-raised" style="width:100%" @click = "makebook()">Book</md-button>
      </md-card-actions>
    </md-card-content>
  </md-card>
</div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import router from '../router'
import auth from '../auth'

export default {
  name: 'LabeledDatepicker',
  methods: {
    makebook(){
      axios.post("http://localhost:8000/post/event/create/",{body:this.$router.currentRoute.params,user:router.app.$auth.getUserProfile(),detail:this.bookdetail})
      .then( 
        (response) => { this.showSuccess = true; },
        (error) => { this.showError = true; }
      );
    }
  },
  data: () => ({
    showSuccess: false,
    showError: false,
    bookdetail : {
      start_day : null,
      end_day : null,
      guest : null,
    },

    message: null
  }),

  mounted () {

  this.user = this.bookdetail.ad_owner;
  console.log(this.$router.currentRoute)
  axios.get("http://localhost:8000/get/advertisement/single/", {params: this.$router.currentRoute.params})
  .then(response => {
    // JSON responses are automatically parsed.
    this.message = response.data
  })
  .catch(e => {
    this.errors.push(e)
  })
  //console.log(this.message)
}
}
</script>

<style lang="scss" scoped>
.md-datepicker-dialog {
  height: 300px;
  top: 0px;
}

body {
  background-color: black;
}
</style>
