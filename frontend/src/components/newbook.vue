<template>
  <div class="newbook">
    <PropertyForm></PropertyForm>
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
