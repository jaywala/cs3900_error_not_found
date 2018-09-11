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

Vue.use(VueMaterial)
const datepickerOptions = {}
Vue.use(AirbnbStyleDatepicker, datepickerOptions)
Vue.config.productionTip = false


Vue.use(BootstrapVue)

Vue.use(auth)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
