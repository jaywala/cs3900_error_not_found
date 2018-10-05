<template>


<div class="PropertyBookingForm" style="">
  <md-card>
    <md-card-header>
      <strong><div class="md-title">${{ this.message.base_price }}</div></strong>per night
    </md-card-header>
    <md-card-content>
      <md-datepicker v-model="selectedDate">
        <label>Check In date</label>
      </md-datepicker>
      <md-datepicker v-model="selectedDate">
        <label>Check Out date</label>
      </md-datepicker>
      <md-field style="width:180px">
        <label for="nGuests">Number of Guests</label>
        <md-select name="nGuests" id="nGuests">
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
        <md-button type="submit" class="md-primary" :disabled="sending">Book</md-button>
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
  data: () => ({
    selectedDate: null,
    message: null
  }),

  mounted () {
  axios.get("http://localhost:8000/get/advertisement"+ this.$router.currentRoute.path.split('@')[0] + "/" + this.$router.currentRoute.path.split('@')[1].split('.')[0] +"/1/")
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

<style lang="scss" scoped>
.md-datepicker-dialog {
  height: 300px;
  top: 0px;
}

body {
  background-color: black;
}
</style>