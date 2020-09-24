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
import lost from '@/pages/lost/index'
import lostResult from '@/pages/lost/result'
import similar from '@/pages/similar'
import nearby from '@/pages/nearby'
import about from '@/pages/about'
import myScrap from '@/pages/my/scrap'
import mySimilar from '@/pages/my/similar'
import detail from '@/pages/detail'

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
    {
      path: '/lost',
      component: lost
    },
    {
      path: '/lost/result',
      component: lostResult
    },
    {
      path: '/similar',
      component: similar
    },
    {
      path: '/nearby',
      component: nearby
    },
    {
      path: '/about',
      component: about
    },
    {
      path: '/my/scrap',
      component: myScrap
    },
    {
      path: '/my/similar',
      component: mySimilar
    },
    {
      path: '/detail/:id',
      component: detail
    },
  ]
})

router.beforeEach((to, from, next) => {
  window.scrollTo(0, 0)
  next()
})

export default router;