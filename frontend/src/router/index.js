import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import newbook from '@/components/newbook'
import landing from '@/components/landing'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [

    {
      path: '/newbook',
      component: newbook
    },
    {
        path: '/',
        component: landing
    }
  ]
})
