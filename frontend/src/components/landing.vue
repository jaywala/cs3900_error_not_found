<template lang="html">
    <search></search>
</template>

<script>
import Vue from 'vue'
import router from '../router'
import axios from 'axios'

import search from './search.vue'

export default {
  components: {
    search,
  },
  data() {
    return {
      total: 10,
      current: Number,
      errors: String,
      ads: [
         {
           ad_id: 1,
           poster: "Colleen@example.com",
           list_of_reviews: "1,",
           list_of_events: "",
           list_of_images: "1,2,3,4,5,6,7,8,9,10,",
           accommodation_name: "An Oasis in the City",
           accommodation_description: "Very  Quay ",
           property_type: "Apartment",
           house_rules: "Be considerate. No showering after 2330h.",
           booking_rules: "no cancellation",
           amenities: "TV,Kitchen,Elevator,Buzzer/wireless intercom,Heating,Washer,Smoke detector,Fire extinguisher,Essentials,Hangers,Hair dryer,Iron,Bed linens,Extra pillows and blankets,Microwave,Refrigerator,Dishwasher,Dishes and silverware,Cooking basics,Stove,Single level home,Patio or balcony,Garden or backyard",
           base_price: 65,
           num_guests: 1,
           num_bedrooms: 1,
           num_bathrooms: 0,
           address: "Potts Point",
           city: "Potts Point, Australia",
           zip_code: "2011",
           latitude: -33.86916827,
           longitude: 151.2265622
         }
      ],
      parameters: "",
      reviews: [],
      ratings: [],
    }
  },
  mounted () {

      axios.get("http://localhost:8000/get/advertisement/" + this.parameters)
      .then(response => {
          // JSON responses are automatically parsed.
          this.ads = response.data
      })
      .catch(e => {
          this.errors.push(e)
      })
      /*for (var i = 0; i < ads.length; i++) {
        let ad = ads[i]
        axios.get("http://localhost:8000/get/advertisement/images/"+ad.ad_id)
      }*/
  }
}
</script>
<style src="./album.css"></style>
