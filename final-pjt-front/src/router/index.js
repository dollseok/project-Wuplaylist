import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GenreView from '../views/GenreView.vue'
import ReviewView from '../views/reviews/ReviewView.vue'
import CreateView from '../views/reviews/CreateView.vue'
import DetailView from '../views/reviews/DetailView.vue'

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
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
  {
    path: '/review/:id',
    name: 'detail',
    component: DetailView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
