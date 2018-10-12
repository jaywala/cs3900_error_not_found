<template>
  <div class="PropertyForm container content">
    <form novalidate class="md-layout" @submit.prevent="validateUser">
      <md-card class="md-layout-item md-size-100 md-small-size-200">
        <md-card-header>
          <div class="md-display-1">List your property</div>
        </md-card-header>

        <md-card-content>
          <div class="md-title">Property Information</div>
          <div class="md-caption">Property & Location information.</div>

          <div>
            <md-radio v-model="form.propertyType" value="apartment">Apartment </md-radio>
            <md-radio v-model="form.propertyType" value="house">House</md-radio>
          </div>

          <md-field :class="getValidationClass('address')">
            <vue-google-autocomplete required
                classname="md-input form-control"
                placeholder="Address"
                name="address"
                id="map"
                v-model="form.address"
                country='au'
                :disabled="sending"
                v-on:placechanged="getAddressData"
              >
            </vue-google-autocomplete>
            <span class="md-error" v-if="!$v.form.address.required">The address is required</span>
          </md-field>


          <div class="md-layout md-gutter">
            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('city')">
                <label for="city">City</label>
                <md-input required name="city" id="city" autocomplete="city" v-model="form.city" :disabled="sending" />
                <span class="md-error" v-if="!$v.form.city.required">The city is required</span>
              </md-field>
            </div>

            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('zipCode')">
                <label for="zip-code">ZIP Code</label>
                <md-input required type="number" name="zip-code" id="zip-code" autocomplete="zip-code" v-model="form.zipCode" :disabled="sending" />
                <span class="md-error" v-if="!$v.form.zipCode.required">The zip code is required</span>
                <span class="md-error" v-else-if="!$v.form.zipCode.minlength">Invalid ZIP Code</span>
                <span class="md-error" v-else-if="!$v.form.zipCode.maxlength">Invalid ZIP Code</span>
              </md-field>
            </div>
          </div>

          <div class="md-title">Overview</div>
          <div class="md-caption">A title and summary displayed on your public listing page.</div>

          <md-field :class="getValidationClass('title')">
            <label for="title">Write a title</label>
            <md-input required name="title" id="title" autocomplete="title" v-model="form.title" :disabled="sending" />
            <span class="md-error" v-if="!$v.form.title.required">A title is required</span>
          </md-field>

          <md-field :class="getValidationClass('summary')">
            <label for="summary">Write a summary in 250 characters or less</label>
            <md-textarea required name="summary" id="summary" autocomplete="summary" v-model="form.summary" :disabled="sending" />
            <span class="md-error" v-if="!$v.form.summary.required">A summary is required</span>
          </md-field>

          <div class="md-layout md-gutter">
            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('nGuests')">
                <label for="nGuests">Number of Guests</label>
                <md-select name="nGuests" id="nGuests" v-model="form.nGuests" md-dense :disabled="sending">
                  <md-option value="1">1</md-option>
                  <md-option value="2">2</md-option>
                  <md-option value="3">3</md-option>
                  <md-option value="4">4</md-option>
                  <md-option value="5">5</md-option>
                  <md-option value="6">6</md-option>
                  <md-option value="7">7</md-option>
                  <md-option value="8">8+</md-option>
                </md-select>
                <span class="md-error">You must specify the maximum number of guests</span>
              </md-field>
            </div>

            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('nBedrooms')">
                <label for="nBedrooms">Number of Bedrooms</label>
                <md-select name="nBedrooms" id="nBedrooms" v-model="form.nBedrooms" md-dense :disabled="sending">
                  <md-option value="1">1</md-option>
                  <md-option value="2">2</md-option>
                  <md-option value="3">3</md-option>
                  <md-option value="4">4</md-option>
                  <md-option value="5">5</md-option>
                  <md-option value="6">6+</md-option>
                </md-select>
                <span class="md-error">You must specify the number of bedrooms</span>
              </md-field>
            </div>

            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('nBathrooms')">
                <label for="nBathrooms">Number of Bathrooms</label>
                <md-select name="nBathrooms" id="nBathrooms" v-model="form.nBathrooms" md-dense :disabled="sending">
                  <md-option value="1">1</md-option>
                  <md-option value="2">2</md-option>
                  <md-option value="3">3</md-option>
                  <md-option value="4">4</md-option>
                  <md-option value="5">5+</md-option>
                </md-select>
                <span class="md-error">You must specify the number of bathrooms</span>
              </md-field>
            </div>
          </div>

          <md-field :class="getValidationClass('amenities')">
            <label for="amenities">Write a list of major amenities provided</label>
            <md-textarea required name="amenities" id="amenities" autocomplete="amenities" v-model="form.amenities" :disabled="sending" />
            <span class="md-error" v-if="!$v.form.amenities.required">A list of available amenities must be provided</span>
          </md-field>
        </md-card-content>

        <md-progress-bar md-mode="indeterminate" v-if="sending" />

        <md-card-actions>
          <md-button type="submit" @click = "submit" class="md-primary" :disabled="sending">Register property</md-button>
        </md-card-actions>
      </md-card>

      <md-snackbar :md-active.sync="userSaved">Property listing was saved with success!</md-snackbar>
    </form>


    <file-base64 :multiple="true" :done="getFiles"></file-base64>

    <div class="text-center">
      <img src="" width="50%" alt="" :src="img.base64" v-for="img in files">
    </div>



    <div v-if="files.length != 0">
      <h3 class="text-center mt-25">Callback Object</h3>
      <div class="pre-container" align="left">
        <pre>{{ files }}</pre>
      </div>
    </div>
  </div>
</template>

<script>
  import VueGoogleAutocomplete from 'vue-google-autocomplete'
  import fileBase64 from 'vue-file-base64';
  import { validationMixin } from 'vuelidate'
  import {
    required,
    minLength,
    maxLength
  } from 'vuelidate/lib/validators'
  import axios from 'axios'
  import Vue from 'vue'
  import router from '../router'
  import auth from '../auth'
  export default {
    components: { fileBase64, VueGoogleAutocomplete },
    mounted () {
    },
    name: 'FormValidation',
    mixins: [validationMixin],
    data: () => ({
      files: [],
      form: {
        poster: null,
        propertyType: 'apartment',
        address: null,
        city: null,
        zipCode: null,
        title: null,
        summary: null,
        nGuests: null,
        nBedrooms: null,
        nBathrooms: null,
        age: null,
        amenities: null,
      },

      userSaved: false,
      sending: false,
      address: ''
    }),
    validations: {
      form: {
        address: {
          required
        },
        city: {
          required
        },
        zipCode: {
          required,
          minLength: minLength(4),
          maxLength: maxLength(4)
        },
        title: {
          required,
          maxLength: maxLength(35)
        },
        summary: {
          required,
          maxLength: maxLength(250)
        },
        age: {
          required,
          maxLength: maxLength(3)
        },
        nGuests: {
          required
        },
        nBedrooms: {
          required
        },
        nBathrooms: {
          required
        },
        amenities: {
          required
        }
      }
    },
    methods: {
      submit(){
        this.form.poster = router.app.$auth.getUserProfile().email
        axios.post('http://localhost:8000/post/advertisement/create/',{body:this.form,images:this.files})

      },
      getFiles(files){
        this.files = files
      },
      getValidationClass (fieldName) {
        const field = this.$v.form[fieldName]

        if (field) {
          return {
            'md-invalid': field.$invalid && field.$dirty
          }
        }
      },
      clearForm () {
        this.$v.$reset()
        this.form.address == null
        this.form.propertyType = 'apartment'
        this.form.city = null
        this.form.zipCode = null
        this.form.title = null
        this.form.summary = null
        this.form.age = null
        this.form.nGuests = null
        this.form.nBedrooms = null
        this.form.nBathrooms = null
        this.form.amenities = null
      },
      saveUser () {
        this.sending = true

        // Instead of this timeout, here you can call your API
        window.setTimeout(() => {
          this.userSaved = true
          this.sending = false
          this.clearForm()
        }, 1500)
      },
      validateUser () {
        this.$v.$touch()

        if (!this.$v.$invalid) {
          this.saveUser()
        }
      },

      /**
      * When the location found
      * @param {Object} addressData Data of the found location
      * @param {Object} placeResultData PlaceResult object
      * @param {String} id Input container ID
      */
      getAddressData: function (addressData, placeResultData, id) {
          this.form.address = placeResultData.formatted_address
          this.form.city = placeResultData.address_components[2]['long_name']
          this.form.zipCode = placeResultData.address_components[6]['long_name']

          // console.log(placeResultData)
          // alert(document.getElementById('map').value)
      }
    }
  }
</script>

<style lang="scss" scoped>
  .md-progress-bar {
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
  }

  small {
    display: block;
  }
</style>
