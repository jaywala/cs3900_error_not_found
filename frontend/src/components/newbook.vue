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
      property_type: String,
      address: String,
      address2: String,
      city: String,
      zip: Number,
      name: String,
      amenities: String,
      description: String,
      rules: String,
      nbathroom: Number,
      nbedroom: Number,
      nguest: Number,
  },
  methods: {

  }
}
</script>
