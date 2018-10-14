<template>
  <div class="newbook">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <meta name="description" content="">
      <meta name="author" content="">

      <title>Register your own Room!</title>

      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    </head>

    <body>
      <PropertyForm></PropertyForm>
    </body>

  </div>
</template>

<script>

import PropertyForm from './PropertyForm.vue'

export default {
  name: 'newbook',
  components: {
    PropertyForm,
  },
  props: {
      message:
      {property_type: String,
      address: String,
      address2: String,
      base_price: Number,
      city: String,
      zip: Number,
      name: String,
      amenities: String,
      description: String,
      rules: String,
      nbathroom: Number,
      nbedroom: Number,
      nguest: Number}
  },
  message:{
    ad_id: 1,
    poster: "Colleen@example.com",
    accommodation_name: "An Oasis in the City",
    accommodation_description: "Quay ",
    house_rules: "Be considerate. No showering after 2330h.",
    booking_rules: "",
    amenities: "TV,Kitchen,Elevator,Buzzer/wireless intercom,Heating,Washer,Smoke detector,Fire extinguisher,Essentials,Hangers,Hair dryer,Iron,Bed linens,Extra pillows and blankets,Microwave,Refrigerator,Dishwasher,Dishes and silverware,Cooking basics,Stove,Single level home,Patio or balcony,Garden or backyard",
    base_price: 65,
    num_guests: 1,
    num_bedrooms: 1,
    num_bathrooms: 0,
    suburb: "Potts Point",
    state: "NSW",
    country: "Australia",
    latitude: -33.86916827,
    longitude: 151.2265622,
    list_of_reviews: "",
    list_of_events: ""
  },
  methods: {

  }
}
</script>
