<template>
<div class="PropertyBookingForm">
  <md-card>
    <md-card-header>
      <div class="md-title">&lt;Booking Form&gt;</div>
    </md-card-header>
    <md-card-content>
      <md-datepicker v-model="selectedDate">
        <label>Check In date</label>
      </md-datepicker>
      <md-datepicker v-model="selectedDate">
        <label>Check Out date</label>
      </md-datepicker>
      <md-field>
        <label for="nGuests">Number of Guests</label>
        <md-select name="nGuests" id="nGuests">
          <md-option value="1">1</md-option>
          <md-option value="2">2</md-option>
          <md-option value="3">3</md-option>
          <md-option value="4">4</md-option>
          <md-option value="5">5</md-option>
          <md-option value="6">6</md-option>
          <md-option value="7">7</md-option>
          <md-option value="8">8+</md-option>
        </md-select>
      </md-field>

      <md-card-actions>
        <md-button type="submit" class="md-primary" :disabled="sending">Book</md-button>
      </md-card-actions>
    </md-card-content>
  </md-card>
</div>
</template>

<script>

export default {
  name: 'LabeledDatepicker',
  data: () => ({
    selectedDate: null
  })
}
</script>

<style lang="scss" scoped>
.md-datepicker-dialog {
  height: 300px;
  top: 0px;
}
</style>