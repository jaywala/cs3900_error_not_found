import Vue from 'vue'
import Router from 'vue-router'
import landing from '@/components/landing.vue'
import newbook from '@/components/newbook.vue'
import callback from '@/components/Callback.vue'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
      {
        path: '/newbook',
        name: 'newbook',
        component: newbook
      },
      {
          path: '/',
          name:'home',
          component: landing
      },
      {
        path: '/callback',
        name:'callback',
        component: callback
      }
  ]
})

// very basic "setup" of a global guard
router.beforeEach((to, from, next) => {
  if(to.name == 'callback') { // check if "to"-route is "callback" and allow access
    next()
  } else if(to.name == 'home'){
    next()
  }else if (router.app.$auth.isAuthenticated()) { // if authenticated allow access
    next()
  } else{
    router.app.$auth.login()
  }
})

export default router