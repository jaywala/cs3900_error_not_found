<template >
  <div id="app">
  <h1>{{this.errored}}</h1>
  {{this.info.user}}


    <!-- EXAMPLE AXIOS USE
    <section v-if="errored">
      <p>We're sorry, we're not able to retrieve this information at the moment, please try back later</p>
    </section>

    <section v-else>
      <div v-if="loading">Loading...</div>

      <div
        v-else
        v-for="currency in info"
        class="currency"
      >
        {{ currency.description }}:
        <span class="lighten">
          <span v-html="currency.symbol"></span>{{ currency.rate_float | currencydecimal }}
        </span>
      </div>

    </section>
    -->

    <main role="main">
      <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" rel="stylesheet">

      <!-- Custom styles for this template -->
      <div class="_1e3y8tsi" style="background-image: url(https://a0.muscache.com/im/pictures/94837647-13df-4845-b85b-292651826562.jpg?aki_policy=xx_large);">
        
      </div>


        <div class="container" style="padding-top:25px">
          <div class="row">

            <div class="col-8">
              <div style="border-bottom: 1px solid #eaecef;">
                <h6>Property Type</h6>
                <h1>Property Title</h1>
                <h6><a href="">Suburb</a></h6>
                <p>Property Description..Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.</p>
              </div>
            </div>

            <div class="col-4">
              <div class="card">
                <div class="card-body">
                  <div style="border-bottom: 1px solid #eaecef;">
                    <p class="card-text">
                      2 of 2
                    </p>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
          
    </main>
  </div>
</template>

<script>
import axios from 'axios'
import AuthService from '../auth/AuthService';

export default {
  data () {
    return {
        /*token:*/
      info: {'username': 'admin', 'password': 'admin'},
      my_data:
      {
          "user": 1,
          "accommodation_name": "changed",
          "accommodation_description": "Very central",
          "house_rules": "Be considerate.   No showering after 2330h.",
          "booking_rules": "no running",
          "base_price": 65.0,
          "num_guests": 1,
          "num_bedrooms": 1,
          "num_bathrooms": 0,
          "suburb": "NSW",
          "state": "NSW",
          "country": "Australia",
          "latitude": -33.86916827,
          "longitude": 151.2265622
    },
    errored: false

    }
  },

  mounted () {
    axios
      .get('http://127.0.0.1:8000/advertisement/1/', { headers: { Authorization: `Bearer ${AuthService.getAuthToken()}` }})
      .then(response => {
        alert(response)
        this.info = response.data
      })
      .catch(error => {
        alert(error)
        console.log(error)
        this.info.errored = 'get method has error'
      })
      .finally(() => this.loading = false)
    /*
    axios
        .post('http://localhost:8000/advertisement/1/', this.info)
        .catch(error => {
            console.log(error)
            this.info.errored = 'post method has error'
        })*/
    axios
        .post('http://localhost:8000/login/', this.info)
        .catch(error => {
            console.log(error)
            this.errored = 'post method has error'
        })
    axios
        .post('http://localhost:8000/advertisement/1/', this.my_data)
        .catch(error => {
            console.log(error)
            this.errored = 'post method has error'
        })


  }
}
</script>

<style lang="css">
._1e3y8tsi {
  background-size: cover !important;
  width: 100% !important;
  height: 500px !important;
  background-position: center center !important;
}
</style>
