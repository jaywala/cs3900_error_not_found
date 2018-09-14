<template lang="html">
    <main role="main">
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" rel="stylesheet">

        <!-- Custom styles for this template -->
      <section class="jumbotron text-center">
        <div class="container">
          <p>
            <h1 style="color:aliceblue;">Sydney</h1>
            <p style="color:aliceblue;">Relentlessly enterprising and culturally diverse, all eyes are on Sydney when this influential city takes the stage.</p>
            <br><br><br><br>
          </p>
        </div>
      </section>

      <div class="album py-5 bg-light">
        <div class="container">

          <div class="row">
            <li v-for="current in total">
            <div class="col-md-4">
              <div class="card mb-4 box-shadow">
                <img class="card-img-top" data-src="holder.js/100px225?theme=thumb&bg=55595c&fg=eceeef&text=Thumbnail" alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                  <div class="d-flex justify-content-between align-items-center">
                    <div class="btn-group">
                      <router-link :to="'detail/' + current" tag = "button">detail</router-link>
                      <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                    </div>
                    <small class="text-muted">9 mins</small>
                  </div>
                </div>
              </div>
            </div>
            </li>
          </div>
        </div>
      </div>

    </main>
</template>

<script>
import Vue from 'vue'
import router from '../router'
export default {
  data() {
    return {
      total: 10,
      current: Number
    }
  }
}
</script>
<style src="./album.css"></style>
