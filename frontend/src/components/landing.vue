<template lang="html">
    <main role="main">
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" rel="stylesheet">

        <!-- Custom styles for this template -->
      <section class="jumbotron text-center">
        <div class="container content">
          <p>
            <h1 style="color:aliceblue;">Sydney</h1>
            <p style="color:aliceblue;">Relentlessly enterprising and culturally diverse, all eyes are on Sydney when this influential city takes the stage.</p>
            <br><br><br><br>
          </p>
        </div>
      </section>

      <!-- Listings -->
      <div class="album py-5 bg-light">
        <div class="container">
          <div class="row">
            <!-- Each Listing -->
            <div v-for="ad in ads" class="col-md-4">
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
        </div>
      </div>

    </main>
</template>

<script>
import Vue from 'vue'
import router from '../router'
import axios from 'axios'
export default {
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
