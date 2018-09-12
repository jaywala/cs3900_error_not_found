<template >
  <div id="app">
  <h1>{{this.ad}}</h1>

</div>
</template>

<script>
import axios from 'axios'
import {APIService} from '../auth/APIService';
/*import Loading from './Loading';*/
const API_URL = 'http://localhost:8000';
const apiService = new APIService();

export default {
    data () {
        return {
            "user": 1,
            "accommodation_name": "An Oasis in the City",
            "accommodation_description": "Very central ",
            "house_rules": "Be considerate.   No showering after 2330h.",
            "booking_rules": "no running",
            "base_price": 65.0,
            "num_guests": 1,
            "num_bedrooms": 1,
            "num_bathrooms": 0,
            "suburb": "Potts Point",
            "state": "NSW",
            "country": "Australia",
            "latitude": -33.86916827,
            "longitude": 151.2265622
        };
    },
    methods: {
        getAdvertisements(){
            apiService.getAdvertisement().then((page) => {
            });
        },
        mounted() {
            axios
              .get('http://localhost:8000/advertisement/1/')
              .then(response => {
                this.info = response.data
              })
              .catch(error => {
                console.log(error)
                this.info.errored = 'get method has error'
              })
              .finally(() => this.loading = false)
        },
    }
}



/*
  mounted () {
    axios
      .get('http://localhost:8000/advertisement/1/')
      .then(response => {
        this.info = response.data
      })
      .catch(error => {
        console.log(error)
        this.info.errored = 'get method has error'
      })
      .finally(() => this.loading = false)

    axios
        .post('http://localhost:8000/advertisement/1/', this.info)
        .catch(error => {
            console.log(error)
            this.info.errored = 'post method has error'
        })
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
}*/
</script>

<style lang="css">
</style>
