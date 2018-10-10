<template>
  <div class="container content" >
    <!--{{message.where}}-->
    <!--<input type="text" placeholder="Any where" v-model="message.where">-->
    <div id="search-filters" style="">
      <md-field style="width: 100%">
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

      <div v-if="this.message['dateOne'] && this.message['dateTwo']" style="display: inline">
        <input type="button" id="datepicker-trigger" class="md-button md-primary md-raised md-theme-default" :value="datesRange">
      </div>
      <div v-else style="display: inline">  
        <input type="button" id="datepicker-trigger" class="md-button md-secondary md-raised md-theme-default" value="Dates">
      </div>

      <md-button class="md-primary md-raised" @click="showGuestsDialog = true">{{ message.guests }} Guest(s)</md-button>
      
      <div v-if="this.message['minPrice'] || this.message['maxPrice']" style="display: inline">
        <md-button class="md-primary md-raised" @click="showPriceDialog = true">Price Range</md-button>
      </div>
      <div v-else style="display: inline">
        <md-button class="md-secondary md-raised" @click="showPriceDialog = true">Price Range</md-button>
      </div>

      <div v-if="this.message['distance']" style="display: inline">
        <md-button class="md-primary md-raised" @click="showDistanceDialog = true">Distance</md-button>
      </div>
      <div v-else style="display: inline">
        <md-button class="md-secondary md-raised" @click="showDistanceDialog = true">Distance</md-button>
      </div>
      
      <div class="" hidden>
        {{message.dateFormat}}
        {{message.dateOne}}
        {{message.dateTwo}}
        {{message.where}}
      </div>
      <md-button class="md-primary md-raised" style="width: 100%" v-on:click="searchAds()">Search</md-button>

    </div>

    <div id="search-result">

      <!-- Results -->
      <div class="row">
        <!-- Map -->
        <div class="col-md-0">
          <div id="map" class="map"></div>
        </div>
        
        <!-- Tiles -->
        <div class="col-md-12">
          <md-content class="md-scrollbar">
            <div id="ads" v-if="this.ads">
              <h2>{{ this.ads.length }} Search Results</h2>

              <div class="album py-5 bg-light"> <!-- Listings -->
                <div class="row">
                  <div v-for="ad in this.ads" class="col-md-4">
                    <div class="card mb-4 box-shadow">
                        <img class="card-img-top" src="https://images-na.ssl-images-amazon.com/images/I/51MZEBXRYML._SL500_AC_SS350_.jpg" alt="Card image cap">
                      <div class="card-body">
                        <p class="card-text">Property Type · {{ad.property_type}}</p>
                        <router-link :to="{ name: 'detailpage', params: { id:ad.ad_id, first:ad.poster.split('@')[0], last:ad.poster.split('@')[1].split('.')[0]}}" > <h4 class="card-text">{{ad.accommodation_name}}</h4></router-link>
                        <p class="card-text">${{ad.base_price}} AUD per night</p>
                        <div class="d-flex justify-content-between align-items-center">
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div> <!-- End of Listings -->

            </div>
          </md-content>
        </div>

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
      
      map: null,
      tileLayer: null,
      layers: [],
    }
  },
  computed: {
    datesRange () {
      return this.message['dateOne'] + "  -  " + this.message['dateTwo'];
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
      this.parameters = {};
      if (this.message['dateOne']) {
        this.parameters['dateOne'] = this.message['dateOne'];
      } else {
        this.parameters['dateOne'] = 'null';
      }
      if (this.message['dateTwo']) {
        this.parameters['dateTwo'] = this.message['dateTwo'];
      } else {
        this.parameters['dateTwo'] = 'null';
      }
      if (this.parameters['where']) {
        this.parameters['where'] = this.message['where'];
      } else {
        this.parameters['where'] = 'null';
      }
      this.parameters['guests'] = this.message['guests'];
      if (this.message['minPrice']) {
        this.parameters['minPrice'] = this.message['minPrice'];
      } else {
        this.parameters['minPrice'] = 'null';
      }
      if (this.message['maxPrice']) {
        this.parameters['maxPrice'] = this.message['maxPrice'];
      } else {
        this.parameters['maxPrice'] = 'null';
      }
      if (this.message['distance']) {
        this.parameters['distance'] = this.message['distance'];
      } else {
        this.parameters['distance'] = 'null';
      }

      let queryString = "{0}/{1}/{2}/{3}/{4}/{5}/{6}/".format(this.parameters['dateOne'], this.parameters['dateTwo'], this.parameters['where'], this.parameters['guests'], this.parameters['minPrice'], this.parameters['maxPrice'], this.parameters['distance'])
      // axios.get("http://127.0.0.1:8000/get/null/null/null/null/null/null/null/")
      axios.get("http://127.0.0.1:8000/get/"+queryString)
      .then(response => {
        // JSON responses are automatically parsed.
        this.ads = response.data
        
      })
      .catch(e => {
        
        this.errors.push(e)
      })
      console.log("lol: "+this.ads)
    },
    initMap() {
      this.map = L.map('map').setView([38.63, -90.23], 12);
      this.tileLayer = L.tileLayer(
        'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png',
        {
          maxZoom: 18,
          attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>',
        }
      );
      this.tileLayer.addTo(this.map);
    },
    initLayers() {},
  },
  mounted() {
    this.searchAds();
    this.initMap();
    this.initLayers();
  },
}
</script>
<style src="./icon.css">
.search-filters {
  
}

.map { height: 600px; }
</style>
