// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router'

import auth from '@/auth'
import BootstrapVue from 'bootstrap-vue'

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

import AirbnbStyleDatepicker from 'vue-airbnb-style-datepicker'
import 'vue-airbnb-style-datepicker/dist/styles.css'

import * as VueGoogleMaps from 'vue2-google-maps'

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyA-XVCnucBeYchFGBfMlgpORJnzTI_TCec',
    libraries: 'places', // This is required if you use the Autocomplete plugin
    // OR: libraries: 'places,drawing'
    // OR: libraries: 'places,drawing,visualization'
    // (as you require)
 
    //// If you want to set the version, you can do so:
    // v: '3.26',
  },
 
  //// If you intend to programmatically custom event listener code
  //// (e.g. `this.$refs.gmap.$on('zoom_changed', someFunc)`)
  //// instead of going through Vue templates (e.g. `<GmapMap @zoom_changed="someFunc">`)
  //// you might need to turn this on.
  // autobindAllEvents: false,
 
  //// If you want to manually install components, e.g.
  //// import {GmapMarker} from 'vue2-google-maps/src/components/marker'
  //// Vue.component('GmapMarker', GmapMarker)
  //// then disable the following:
  // installComponents: true,
})

Vue.use(VueMaterial)
const datepickerOptions = {}
Vue.use(AirbnbStyleDatepicker, datepickerOptions)
Vue.config.productionTip = false


Vue.use(BootstrapVue)

Vue.use(auth)

Vue.config.productionTip = false

var filter = function(text, length, clamp){
  clamp = clamp || '...';
  var node = document.createElement('div');
  node.innerHTML = text;
  var content = node.textContent;
  return content.length > length ? content.slice(0, length) + clamp : content;
};

Vue.filter('truncate', filter);

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
