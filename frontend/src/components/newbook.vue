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

        <body class="bg-light">

          <div class="container">
            <div class="py-5 text-center">
              <!-- <img class="d-block mx-auto mb-4" src="../../assets/brand/bootstrap-solid.svg" alt="" width="72" height="72"> -->
              <h2>List Your Space</h2>
              <p class="lead">Register your property and become a part of the NotAirbnb family today!</p>
            </div>

            <div class="row">
              <div class="col-md-4 order-md-2 mb-4">
                <h4 class="d-flex justify-content-between align-items-center mb-3">
                  <span class="text-muted">Images</span>
                  <span class="badge badge-secondary badge-pill">3</span>
                </h4>
                <ul class="list-group mb-3">
                  <li class="list-group-item d-flex justify-content-between lh-condensed">
                    <div>
                      <img src="https://i5.walmartimages.com/dfw/4ff9c6c9-2673/k2-_19b82632-4ccd-4bea-b475-041a6e4828e7.v1.jpg" height="100px"/>
                    </div>
                    <span class="text-muted">1</span>
                    <a href="#">
                      <span class="glyphicon glyphicon-remove">remove</span>
                    </a>

                  </li>
                  <li class="list-group-item d-flex justify-content-between lh-condensed">
                      <div>
                        <img src="https://i5.walmartimages.com/dfw/4ff9c6c9-2673/k2-_19b82632-4ccd-4bea-b475-041a6e4828e7.v1.jpg" height="100px"/>
                      </div>
                      <span class="text-muted">2</span>
                      <a href="#">
                        <span class="glyphicon glyphicon-remove">remove</span>
                      </a>
                    </li>
                    <li class="list-group-item d-flex justify-content-between lh-condensed">
                      <div>
                        <img src="https://i5.walmartimages.com/dfw/4ff9c6c9-2673/k2-_19b82632-4ccd-4bea-b475-041a6e4828e7.v1.jpg" height="100px"/>
                      </div>
                      <span class="text-muted">3</span>
                      <a href="#">
                        <span class="glyphicon glyphicon-remove">remove</span>
                      </a>
                    </li>

                </ul>

                <form class="card p-2">
                  <div class="form-group">
                    <input type="file" class="form-control-file" id="exampleFormControlFile1">
                  </div>
                </form>
              </div>
              <div class="col-md-8 order-md-1">
                <h4 class="mb-3">Property Information</h4>
                <form class="needs-validation" novalidate>

                  <div class="mb-3">
                    <label for="type">Property Type</label>
                    <div class="form-check">
                      <input v-model="property_type" class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios1" value="apartment" checked>
                      <label class="form-check-label" for="exampleRadios1">
                        Apartment
                      </label>
                    </div>
                    <div class="form-check">
                      <input v-model="property_type" class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios2" value="house">
                      <label class="form-check-label" for="exampleRadios2">
                        House
                      </label>
                    </div>
                  </div>
                  <div class="mb-3">
                    <label for="address">Address</label>
                    <input v-model="address" type="text" class="form-control" id="address" placeholder="1234 Main St" required>
                    <div class="invalid-feedback">
                      Please enter your shipping address.
                    </div>
                  </div>

                  <div class="mb-3">
                    <label for="address2">Address 2 <span class="text-muted">(Optional)</span></label>
                    <input v-model="address2" type="text" class="form-control" id="address2" placeholder="Apartment or suite">
                  </div>

                  <div class="row">
                    <div class="col-md-5 mb-3">
                      <label for="country">City</label>
                      <input v-model="city" type="text" class="form-control" id="city" placeholder="" required>
                      <div class="invalid-feedback">
                        Please select a valid city.
                      </div>
                    </div>
                    <div class="col-md-3 mb-3">
                      <label for="zip">Zip</label>
                      <input v-model="zip"type="text" class="form-control" id="zip" placeholder="" required>
                      <div class="invalid-feedback">
                        Zip code required.
                      </div>
                    </div>
                  </div>
                  <hr class="mb-4">

                  <h4 class="mb-3">Listing Information</h4>

                  <div class="mb-3">
                    <label for="address">Listing name</label>
                    <input v-model="name"type="text" class="form-control" id="address" placeholder="Quiet 2 bedroom highrise flat in the CBD" required>
                  </div>

                  <div class="row">
                    <div class="col-md-4 mb-3">
                      <label for="guests">Number of Guests</label>
                      <select v-model="nguest"class="custom-select d-block w-100" id="guests" required>
                        <option value="">Choose...</option>
                        <option>1</option>
                        <option>&lt;2</option>
                        <option>&lt;3</option>
                        <option>&lt;4</option>
                        <option>&lt;5</option>
                        <option>&lt;6</option>
                        <option>&lt;7</option>
                        <option>&lt;8</option>
                      </select>
                    </div>

                    <div class="col-md-4 mb-3">
                      <label for="rooms">Number of Bedrooms</label>
                      <select v-model="nbedroom"class="custom-select d-block w-100" id="rooms" required>
                        <option value="">Choose...</option>
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                        <option>6</option>
                      </select>
                    </div>


                    <div class="col-md-4 mb-3">
                      <label for="rooms">Number of Bathrooms</label>
                      <select v-model="nbathroom"class="custom-select d-block w-100" id="rooms" required>
                        <option value="">Choose...</option>
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                        <option>6</option>
                      </select>
                    </div>

                  </div>

                  <div class="mb-3">
                    <label for="address">Amenities</label>
                    <textarea v-model="amenities" class="form-control" rows="5" id="comment"></textarea>
                  </div>

                  <div class="mb-3">
                    <label for="address">Description</label>
                    <textarea v-model="description"class="form-control" rows="5" id="comment"></textarea>
                  </div>

                  <div class="mb-3">
                    <label for="address">House Rules</label>
                    <textarea v-model="rules"class="form-control" rows="5" id="comment"></textarea>
                  </div>


                <button class="btn btn-primary btn-lg btn-block" >Continue</button>
                </form>
              </div>
            </div>

            <footer class="my-5 pt-5 text-muted text-center text-small">
              <p class="mb-1">&copy; 2017-2018 Company Name</p>
              <ul class="list-inline">
                <li class="list-inline-item"><a href="#">Privacy</a></li>
                <li class="list-inline-item"><a href="#">Terms</a></li>
                <li class="list-inline-item"><a href="#">Support</a></li>
              </ul>
            </footer>
          </div>
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
