<template>
  <div>

    <md-table style = "margin: 70px">
      <md-table-row>
        <md-table-head>Name</md-table-head>
        <md-table-head>Email</md-table-head>
        <md-table-head>Request</md-table-head>
      </md-table-row>

      <md-table-row v-for="r in request">
        <md-table-cell>{{r.rname}}</md-table-cell>
        <md-table-cell>{{r.email}}</md-table-cell>
        <md-table-cell>{{r.detail}}</md-table-cell>
      </md-table-row>
    </md-table>

      <label>request detail</label>
      <md-input v-model="message.detail"></md-input>
    </md-field>
    <md-button class="md-dense md-raised md-primary" @click = "submit()">public</md-button>
  </div>
</template>

<script>
  export default {
    name: 'TableBasic',
    data: () => ({
      request:[
        {
          rname: "George",
          email: "george@test.com",
          detail:"I want a room faces north and near sea",
        },
      ],

      message: {
        name: null,
        email: null,
        detail:null,
      },
    }),
    methods: {
      submit() {
        this.request.push(this.message)
      }
    },
  }
</script>
