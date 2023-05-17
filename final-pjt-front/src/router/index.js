import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GenreView from '../views/GenreView.vue'
import ReviewView from '../views/ReviewView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/genre',
    name: 'genre',
    component: GenreView
  },
  {
    path: '/review',
    name: 'review',
    component: ReviewView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
