<template>
  <div class="manage content container">
    <h1>Your Properties</h1>
    <div v-if="ads">

      <div v-for="advert in ads">
        <div class="card">
          <div class="card-body">
            <router-link :to="{ name: 'detailpage', params: { poster_id:advert.ad.poster_id, ad_id:advert.ad.ad_id } }" > <h4 class="card-text">{{advert.ad.accommodation_name}}</h4></router-link>
            <small>{{ advert.ad.address }}</small>
            <p>{{ advert.ad.accommodation_description | truncate(200, '...') }}</p>
            
            <router-link :to="{ name: 'detailpage', params: { poster_id:advert.ad.poster_id, ad_id:advert.ad.ad_id } }" ><md-button class="md-primary md-raised">View</md-button></router-link>
            <md-button class="md-secondary md-raised">Edit</md-button>
            <div style="display: inline">
              <md-dialog-confirm
                :md-active.sync="delete_dialog_active"
                md-title="Are you sure you want to delete this property listing?"
                md-content="This action cannot be undone."
                md-confirm-text="Yes"
                md-cancel-text="No"
                @md-confirm="deleteAd(advert.ad.ad_id)" />

              <md-button class="md-accent md-raised" @click="delete_dialog_active = true">Delete</md-button>
            </div>
            
          </div>

          <!-- Bookings -->
          <div v-for="event in advert.events">
            <div class="alert alert-success" role="alert">
              <h5 class="alert heading"><span class="badge badge-secondary">Booked</span> {{ event.booker }}</h5>
              <p>{{ event.start_day }} - {{ event.end_day }}</p>
              <hr>
              <p><strong>Notes: </strong>{{ event.notes }}</p>
            </div>
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
      errors: [],
      ads: [],
      ads_bookings: [],
      user: null,
      delete_dialog_active: false,
    }
  },
  computed: {},
  methods: {
    deleteAd: function(ad_id) {
      axios.post("http://localhost:8000/post/advertisement/delete/",
        {
          body: {
            poster: this.user.email,
            ad_id: ad_id
          }
        }
      )
      // Refresh page.
      location.reload();
    },

    fetchAdEvents: function(ad_id) {
      // Fetch bookings for each advertisement.
      alert('fetching...')
      axios.get("http://localhost:8000/get/event/user/",
        {
          params: {
            email: this.user.email,
            ad_id: ad_id,
          }
        })
        .then(response => {
            // JSON responses are automatically parsed.
            console.log(response.data)
            return response.data
        })
        .catch(e => {
            this.errors.push(e)
        })
    }
  },
  mounted() {
    this.user = router.app.$auth.getUserProfile();
    // console.log(this.user);

    axios.get("http://localhost:8000/get/everythingUser/",
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
