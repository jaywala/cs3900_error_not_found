<template >
  <div id="app">
  <h1>{{this.errored}}</h1>
  {{this.info.user}}
</div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      info: {
        user: 1,
        accommodation_name: "changed",
        accommodation_description: "Very central to the city which can be reached by an easy walk or by bus, with transport at the door, if required, and all amenities within easy reach. Potts Pt. is a vibrant and popular inner-city suburb & the area was described as 'Australia's Bohemian Heart' in the article by Raymond Bonner in the New York Times . Ultra-convenient & within walking distance of the central business district & all tourist sites such as: the Botanic Gardens, Opera House,",
        house_rules: "Be considerate. No showering after 2330h.",
        booking_rules: "",
        base_price: 65,
        num_guests: 1,
        num_bedrooms: 1,
        num_bathrooms: 0,
        suburb: "NSW",
        state: "NSW",
        country: "Australia",
        latitude: -33.86916827,
        longitude: 151.2265622,
        loading: true,
        errored: false
      }
    }
  },

  mounted () {
    /*axios
      .get('http://localhost:8000/advertisement/1/')
      .then(response => {
        this.info = response.data
      })
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(() => this.loading = false)*/
      axios.post('http://localhost:8000/advertisement/1/', this.info)



  }
}
</script>

<style lang="css">
</style>
