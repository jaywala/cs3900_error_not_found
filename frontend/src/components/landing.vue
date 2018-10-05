<template lang="html">
    <main role="main">
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" rel="stylesheet">

        <!-- Custom styles for this template -->
      <section class="jumbotron text-center">
        <div class="container">
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
                  <p class="card-text">Property Type · {{ad.suburb}}</p>
                   <router-link :to="{ name: 'detailpage', params: { id:ad.ad_id, poster:ad.poster }}" > <h4 class="card-text">{{ad.accommodation_name}}</h4></router-link>
                  <p class="card-text">${{ad.base_price}} AUD per night</p>
                  <div class="d-flex justify-content-between align-items-center">
                    <small class="text-muted">&lt;Rating&gt; &lt;# of Reviews&gt;</small>
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
      ads: {
         ad:{
           id: 4,
           email:"hdhh@gmail.com"
         }
      },
      parameters: "",
      message: ""
    }
  },
  mounted () {

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
</script>
<style src="./album.css"></style>
