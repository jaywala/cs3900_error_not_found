<template >
  <div id="app">
  <h1>{{this.info}}, {{this.thing}}</h1>

</div>
</template>


<script>
import axios from 'axios';
import {APIService} from '../auth/APIService';
/*import Loading from './Loading';*/
const API_URL = 'http://localhost:8000';
const apiService = new APIService();

export default {
  name: 'detail',
  data() {
    return {
      selectedAdvertisement:null,
      advertisements: [],
      numberOfPages:0,
      pages : [],
      numberOfProducts:0,
      /*loading: false,*/
      nextPageURL:'',
      previousPageURL:''
    };
  },
  methods: {
    getAdvertisements(){

      /*this.loading = true;    */
      apiService.getAdvertisements().then((page) => {
        this.advertisements = page.data;
        console.log(page);
        console.log(page.nextlink);
        this.numberOfProducts = page.count;
        this.numberOfPages = page.numpages;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        if(this.numberOfPages)
        {
          for(var i = 1 ; i <= this.numberOfPages ; i++)
          {
            const link = `/advertisement/?page=${i}`;
            this.pages.push({pageNumber: i , link: link})
          }
        }
        /*this.loading = false;*/
      });
    },
    getPage(link){
      this.loading = true;
      apiService.getAdvertisementsByURL(link).then((page) => {
        this.products = page.data;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        /*this.loading = false;*/
      });
    },
    getNextPage(){
      console.log('next' + this.nextPageURL);
      /*this.loading = true;*/
      apiService.getAdvertisementsByURL(this.nextPageURL).then((page) => {
        this.products = page.data;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        /*this.loading = false;*/
      });

    },
    getPreviousPage(){
      /*this.loading = true;*/
      apiService.getAdvertisementsByURL(this.previousPageURL).then((page) => {
        this.products = page.data;
        this.nextPageURL = page.nextlink;
        this.previousPageURL = page.prevlink;
        /*this.loading = false;*/
      });

    },
    deleteProduct(advertisement){
      console.log("deleting advertisement: " + JSON.stringify(advertisement))
      apiService.deleteAdvertisement(advertisement).then((r)=>{
        console.log(r);
        if(r.status === 204)
        {
          alert("advertisement deleted");
          this.$router.go()

        }
      })
    },
    selectProduct(advertisement){
      this.selectedAdvertisement = advertisement;
    }
  },
  mounted() {

    /*this.ad = this.getAdvertisements();*/
    axios
      .getAdvertisements()
      .then(response => {
        this.info = response.data
      })
      .catch(error => {
        console.log(error)
        this.errored = 'get method has error'
      })

      this.thing = 'hello'


  },
}



/*
  mounted () {
    axios
      .get('http://localhost:8000/advertisement/1/')
      .then(response => {
        this.info = response.data
      })
      .catch(error => {
        console.log(error)
        this.info.errored = 'get method has error'
      })
      .finally(() => this.loading = false)

    axios
        .post('http://localhost:8000/advertisement/1/', this.info)
        .catch(error => {
            console.log(error)
            this.info.errored = 'post method has error'
        })
    axios
        .post('http://localhost:8000/login/', this.info)
        .catch(error => {
            console.log(error)
            this.errored = 'post method has error'
        })
    axios
        .post('http://localhost:8000/advertisement/1/', this.my_data)
        .catch(error => {
            console.log(error)
            this.errored = 'post method has error'
        })


  }
}*/
</script>

<style lang="css">
</style>
