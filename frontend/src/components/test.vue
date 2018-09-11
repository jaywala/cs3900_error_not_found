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
      where: ''
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
