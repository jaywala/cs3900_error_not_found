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
Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
      {
        path:'/success',
        name:'success',
        component: success
      },
      {
        path: '/manage',
        name: 'manage',
        component: manage
      },
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
      },
      {
        path: '/test',
        name: 'test',
        component: test
      },
      {
          path: '/detail/:poster_id/:ad_id',
          component: detail,
          name: 'detailpage'

      },
      {
        path: '/search',
        component: search,
        name: search
      },
      {
        path: '/editprofile',
        component: editprofile,
        name: editprofile
      },
      {
        path: '/review',
        component: review,
        name: review
      },
      {
        path: '/request',
        component: request,
        name:request,
      },
      {
        path: '/image',
        component: image,
        name:image
      }
  ]
})

// very basic "setup" of a global guard
router.beforeEach((to, from, next) => {
  if(to.name == 'callback') { // check if "to"-route is "callback" and allow access
    next()
  } else if(to.name == 'home'){
    next()
  }
  else if(to.path == '/detail/*'){
    next()
  }
  else if(to.path == '/detail'){
    next()
  }else if (router.app.$auth.isAuthenticated()) { // if authenticated allow access
    next()
  } else{
    router.app.$auth.login()
  }
})

export default router
