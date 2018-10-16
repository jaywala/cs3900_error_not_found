import Vue from 'vue'
import Router from 'vue-router'
import landing from '@/components/landing.vue'
import manage from '@/components/manage.vue'
import newbook from '@/components/newbook.vue'
import callback from '@/components/Callback.vue'
import test from '@/components/test.vue'
import detail from '@/components/detail.vue'
import search from '@/components/search.vue'
import editprofile from '@/components/editprofile.vue'
import review from '@/components/review.vue'
import image from '@/components/displayimage.vue'
import request from '@/components/requestform.vue'
import success from '@/components/success.vue'
import editfinish from '@/components/editfinish.vue'
Vue.use(Router)

const router = new Router({
  //router in history mode which will act like normal MPA
  mode: 'history',
  //all the routes
  routes: [
      //successful page
      {
        path:'/successedit',
        name:'successedit',
        component:editfinish,
      },
      //successful page
      {
        path:'/success',
        name:'success',
        component: success
      },
      //manage own property
      {
        path: '/manage',
        name: 'manage',
        component: manage
      },
      //add new property
      {
        path: '/newbook',
        name: 'newbook',
        component: newbook
      },
      //main search page
      {
          path: '/',
          name:'home',
          component: landing
      },
      //used to handle auth0 redir after login
      {
        path: '/callback',
        name:'callback',
        component: callback
      },
      //used for test
      /*{
        path: '/test',
        name: 'test',
        component: test
      },*/
      //detail page of a specific property
      {
          path: '/detail/:poster_id/:ad_id',
          component: detail,
          name: 'detailpage'

      },
      // main search page
      {
        path: '/search',
        component: search,
        name: search
      },
      // edit users profile
      {
        path: '/editprofile',
        component: editprofile,
        name: editprofile
      },
      //review all the booking
      {
        path: '/review',
        component: review,
        name: review
      },
      //page for request a specific property
      {
        path: '/request',
        component: request,
        name:request,
      },
      
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
