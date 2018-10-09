<template>
  <div class="container">
    {{message.where}}
    <!--<input type="text" placeholder="Any where" v-model="message.where">-->
    <md-field style="width: 500px">
      <vue-google-autocomplete required
          classname="md-input form-control"
          placeholder="Address"
          name="address"
          id="map"
          v-model="message.where"
          country='au'
          v-on:placechanged="getAddressData"
        >
      </vue-google-autocomplete>
    </md-field>

    <!--<input
      type="text"
      id="datepicker-trigger"
      v-bind:placeholder="message.dateFormat"
      :value="formatDates(message.dateOne, message.dateTwo)"
    >-->
    <AirbnbStyleDatepicker
      :trigger-element-id="'datepicker-trigger'"
      :mode="'range'"
      :fullscreen-mobile="true"
      :date-one="message.dateOne"
      :date-two="message.dateTwo"
      :offset-y="10"
      @date-one-selected="val => { message.dateOne = val }"
      @date-two-selected="val => { message.dateTwo = val }"
    />
    <div id="search-filters">
      <md-dialog :md-active.sync="showGuestsDialog">
        <md-dialog-title>Number of Guests</md-dialog-title>
          
        <md-button style="display:inline-block;" class="md-icon-button md-raised" v-bind:disabled="message.guests <= 1? true:false" v-on:click="message.guests -= 1" >
          -
        </md-button>
        {{message.guests}}
        <md-button style="display:inline-block;" class="md-icon-button md-raised" v-on:click="message.guests += 1" >
          <md-icon>add</md-icon>
        </md-button>

        <md-dialog-actions>
          <md-button class="md-primary" @click="showGuestsDialog = false">Clear</md-button>
          <md-button class="md-primary" @click="showGuestsDialog = false">Apply</md-button>
        </md-dialog-actions>
      </md-dialog>

      <md-dialog :md-active.sync="showPriceDialog">
        <md-dialog-title>Price</md-dialog-title>

        <div class="md-layout-item md-layout md-gutter"> 
          <div class="md-layout-item">
            <md-field>
              <label>Min</label>
              <md-input v-model="message.minPrice"></md-input>
            </md-field>
          </div>
          
          <div class="md-layout-item">
            <md-field>
              <label>Max</label>
              <md-input v-model="message.maxPrice"></md-input>
            </md-field>
          </div>
        </div>

        <md-dialog-actions>
          <md-button class="md-primary" @click="showPriceDialog = false">Clear</md-button>
          <md-button class="md-primary" @click="showPriceDialog = false">Apply</md-button>
        </md-dialog-actions>        
      </md-dialog>

      <md-dialog :md-active.sync="showDistanceDialog">
        <md-dialog-title>Max Distance</md-dialog-title>

        <md-field>
          <label>Max Distance (Km)</label>
          <md-input v-model="message.distance"></md-input>
        </md-field>

        <md-dialog-actions>
          <md-button class="md-primary" @click="showDistanceDialog = false">Clear</md-button>
          <md-button class="md-primary" @click="showDistanceDialog = false">Apply</md-button>
        </md-dialog-actions>        
      </md-dialog>

      <input type="button" id="datepicker-trigger" class="md-button md-primary md-raised md-theme-default" value="Dates">
      <md-button class="md-primary md-raised" @click="showGuestsDialog = true">Guests</md-button>
      <md-button class="md-primary md-raised" @click="showPriceDialog = true">Price Range</md-button>
      <md-button class="md-primary md-raised" @click="showDistanceDialog = true">Distance</md-button>
      <div class="">
        {{message.dateFormat}}
        {{message.dateOne}}
        {{message.dateTwo}}
        {{message.where}}
      </div>
    </div>

  </div>
</template>

<script>

import router from '../router'
import axios from 'axios'
import VueGoogleAutocomplete from 'vue-google-autocomplete'
import format from 'date-fns/format'
//import './../vue-airbnb-style-datepicker/dist/vue-airbnb-style-datepicker.min.css'
export default {
  components: {
    VueGoogleAutocomplete,
  },
  data() {
    return {
      showGuestsDialog: false,
      showPriceDialog: false,
      showDistanceDialog: false,
      message:{
        "dateFormated": '',
        "dateOne": '',
        "dateTwo": '',
        "where": '',
        "guests": 1,
        "distance": '',
        "minPrice": '',
        "maxPrice": '',
      },
      ads: null,
    }
  },
  methods: {
    formatDates(dateOne, dateTwo) {
      let formattedDates = ''
      if (dateOne) {
        formattedDates = format(dateOne, this.message.dateFormat)
      }
      if (dateTwo) {
        formattedDates += ' - ' + format(dateTwo, this.message.dateFormat)
      }
      return formattedDates
    },

    /**
    * When the location found
    * @param {Object} addressData Data of the found location
    * @param {Object} placeResultData PlaceResult object
    * @param {String} id Input container ID
    */
    getAddressData: function (addressData, placeResultData, id) {
        this.message.where = placeResultData.formatted_address

        // console.log(placeResultData)
        // alert(document.getElementById('map').value)
    },

    searchAds() {
      console.log(this.$router.currentRoute.path)
      this.parameters = ""
      axios.get("http://localhost:8000/get/advertisement/" + this.parameters)
      .then(response => {
        // JSON responses are automatically parsed.
        this.ads = response.data
      })
      .catch(e => {
        this.errors.push(e)
      })
      console.log(this.ads)
    }
  }
}
</script>
<style src="./icon.css">
.search-filters {
  
}
</style>
