<template>
  <div>
    <div class="datepicker-trigger">
      <h2>Book unique homes and experiences.</h2>
      <h3>where</h3>
      <input type="text" placeholder="Any where" v-model="where">
      <h3>check-in n check-out</h3>
      <input
        type="text"
        id="datepicker-trigger"
        placeholder="Select dates"
        :value="formatDates(dateOne, dateTwo)"
      >

      <AirbnbStyleDatepicker
        :trigger-element-id="'datepicker-trigger'"
        :mode="'range'"
        :fullscreen-mobile="true"
        :date-one="dateOne"
        :date-two="dateTwo"
        @date-one-selected="val => { dateOne = val }"
        @date-two-selected="val => { dateTwo = val }"
      />
      <h3>guest</h3>

      <md-button class="md-icon-button md-raised" v-on:click="guests -= 1" >
        -
      </md-button>
      {{guests}}
      <md-button class="md-icon-button md-raised" v-on:click="guests += 1" >
        <md-icon>add</md-icon>
      </md-button>

    </div>
    <div class="">
      {{dateFormat}}
      {{dateOne}}
      {{dateTwo}}
    </div>
  </div>
</template>

<script>
import format from 'date-fns/format'
//import './../vue-airbnb-style-datepicker/dist/vue-airbnb-style-datepicker.min.css'
export default {
  data() {
    return {
      dateFormat: 'D MMM',
      dateOne: '',
      dateTwo: '',
      where: '',
      guests: 0
    }
  },
  methods: {
    formatDates(dateOne, dateTwo) {
      let formattedDates = ''
      if (dateOne) {
        formattedDates = format(dateOne, this.dateFormat)
      }
      if (dateTwo) {
        formattedDates += ' - ' + format(dateTwo, this.dateFormat)
      }
      return formattedDates
    }
  }
}
</script>
<style src="./icon.css"></style>
