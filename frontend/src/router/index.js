import Vue from 'vue'
import Router from 'vue-router'
//commit test
Vue.use(Router)

import index from '@/pages/index'
import login from '@/pages/login'
import signup from '@/pages/signup'
import first from '@/pages/first'
import match from '@/pages/match/index'
import matchResult from '@/pages/match/result'

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: index
    },
    {
      path: '/login',
      component: login
    },
    {
      path: '/signup',
      component: signup
    },
    {
      path: '/first',
      component: first
    },
    {
      path: '/match',
      component: match
    },
    {
      path: '/match/result',
      component: matchResult
    },
  ]
})

router.beforeEach((to, from, next) => {
  window.scrollTo(0, 0)
  next()
})

export default router;