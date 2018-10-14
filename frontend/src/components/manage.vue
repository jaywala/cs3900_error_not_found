<template>
  <div class="manage content container">
    <h1>Your Properties</h1>
    <div v-if="ads">

      <div v-for="ad in ads">
        <div class="card">
          <div class="card-body">
            <router-link :to="{ name: 'detailpage', params: { id:ad.ad_id, first:ad.poster.split('@')[0], last:ad.poster.split('@')[1].split('.')[0]}}" > <h4 class="card-text">{{ad.accommodation_name}}</h4></router-link>
            <small>{{ ad.address }}</small>
            <p>{{ ad.accommodation_description | truncate(200, '...') }}</p>

            <md-button class="md-primary md-raised" onclick=location.href="{ name: 'detailpage', params: { id:ad.ad_id, first:ad.poster.split('@')[0], last:ad.poster.split('@')[1].split('.')[0]}}">View</md-button>
            <md-button class="md-secondary md-raised">Edit</md-button>
            <md-button class="md-accent md-raised">Delete</md-button>
          </div>
        </div>
      </div> <!-- End of ad -->

    </div>
    <div v-else>
      <div class="card">
        <div class="card-body">
          <h3>List your first property Today!</h3>
        </div>
      </div>
    </div>

    <h1>Your Bookings</h1>
    <div class="card">
      <div class="card-body">
        This is some text within a card body.
      </div>
    </div>

  </div>
</template>


<script>
import Vue from 'vue'
import router from '../router'
import axios from 'axios'

export default {
  name: 'manage',
  components: {},
  data() {
    return {
      ads: [],
      user: null,
    }
  },
  computed: {},
  methods: {

  },
  mounted() {
    this.user = router.app.$auth.getUserProfile();
    // console.log(this.user);



    axios.get("http://localhost:8000/get/advertisement/user/",
          {
        params: {
          email: this.user.email
        }
      })
      .then(response => {
          // JSON responses are automatically parsed.
          this.ads = response.data
          console.log(this.ads)
      })
      .catch(e => {
          this.errors.push(e)
      })
  }
}
</script>
