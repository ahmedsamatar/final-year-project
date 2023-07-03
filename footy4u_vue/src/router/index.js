// router used for navigation between pages
import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import HomeView from '../views/HomeView.vue' // import homeview from views

import Game from '../views/Game.vue' // import game from views 
import Matches from '../views/Matches.vue' // import matches from views
import Search from '../views/Search.vue' // import search from views
import Cart from '../views/Cart.vue' // import cart from views
import SignUp from '../views/SignUp.vue' // import signup from views
import LogIn from '../views/LogIn.vue' // import login from views
import MyAccount from '../views/MyAccount.vue' // import my acccount from views
import Checkout from '../views/Checkout.vue' // import checkout from views
import Success from '../views/Success.vue' // import success from views
import Stats from '../views/Stats.vue' // import stats from views

// dynamic routes
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true // must be logged in to access this page which protected by the router guard
    }
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: Success
  },
  {
    path: '/stats',
    name: 'Stats',
    component: Stats
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    meta: {
      requireLogin: true // must be logged in to access this page which protected by the router guard
    }
  },
  {
    path: '/:matches_slug/:game_slug/', // seperation of slugs in the path 
    name: 'Game',
    component: Game
  },
  {
    path: '/:matches_slug',
    name: 'Matches',
    component: Matches
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => { // checking if state is logged in
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) { // triggers login, if user is not logged in and wants to proceed to checkout, user will be automatically be sent to the login screen 
    next({ name: 'LogIn', query: { to: to.path } }); // redirects user to log in
  } else {
    next()
  }
})

export default router
