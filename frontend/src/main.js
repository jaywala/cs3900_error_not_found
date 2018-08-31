// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router'

import auth from '@/auth'
import BootstrapVue from 'bootstrap-vue'



Vue.use(BootstrapVue)

Vue.use(auth)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
