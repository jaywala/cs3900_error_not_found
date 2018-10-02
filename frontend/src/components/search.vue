<template>
  <div>
    <div class="datepicker-trigger">
      <h2>Book unique homes and experiences.</h2>
      <h3>where</h3>
      <input type="text" placeholder="Any where" v-model="message.where">
      <h3>check-in n check-out</h3>
      <input
        type="text"
        id="datepicker-trigger"
        v-bind:placeholder="message.dateFormat"
        :value="formatDates(message.dateOne, message.dateTwo)"
      >

      <AirbnbStyleDatepicker
        :trigger-element-id="'datepicker-trigger'"
        :mode="'range'"
        :fullscreen-mobile="true"
        :date-one="message.dateOne"
        :date-two="message.dateTwo"
        @date-one-selected="val => { message.dateOne = val }"
        @date-two-selected="val => { message.dateTwo = val }"
      />
      <h3>guest</h3>

      <md-button class="md-icon-button md-raised" v-bind:disabled="message.guests <= 0? true:false" v-on:click="message.guests -= 1" >
        -
      </md-button>
      {{message.guests}}
      <md-button class="md-icon-button md-raised" v-on:click="message.guests += 1" >
        <md-icon>add</md-icon>
      </md-button>

    </div>
    <div class="">
      {{message.dateFormat}}
      {{message.dateOne}}
      {{message.dateTwo}}
      {{message.where}}
    </div>
  </div>
</template>

<script>
import format from 'date-fns/format'
//import './../vue-airbnb-style-datepicker/dist/vue-airbnb-style-datepicker.min.css'
export default {
  data() {
    return {
      message:{
        "dateFormat": 'DD MMM',
        "dateOne": '',
        "dateTwo": '',
        "where": '',
        "guests": 0
      }
    }
  },
  methods: {
    formatDates(dateOne, dateTwo) {
      let formattedDates = ''
      if (dateOne) {
        formattedDates = format(message.dateOne, message.dateFormat)
      }
      if (dateTwo) {
        formattedDates += ' - ' + format(message.dateTwo, message.dateFormat)
      }
      return formattedDates
    }
  }
}
</script>
<style src="./icon.css"></style>
