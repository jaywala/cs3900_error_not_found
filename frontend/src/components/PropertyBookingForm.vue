<template>
  <div class="PropertyBookingForm">
    <h2>&lt;Booking Form&gt;</h2>
    Check in<datepicker></datepicker>
    Check out<datepicker></datepicker>
  </div>
</template>

<script>
import Datepicker from 'vuejs-datepicker';
 
export default {
  // ...
  components: {
    Datepicker
  }
  // ...
}
</script>

<style>

</style>