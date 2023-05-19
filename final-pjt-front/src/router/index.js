import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GenreView from '../views/GenreView.vue'

import ReviewView from '../views/reviews/ReviewView.vue'
import CreateView from '../views/reviews/CreateView.vue'
import DetailView from '../views/reviews/DetailView.vue'

import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  // 장르로 영화 검색하는 페이지
  {
    path: '/genre',
    name: 'genre',
    component: GenreView
  },
  // 리뷰 게시판
  {
    path: '/review',
    name: 'review',
    component: ReviewView
  },
  // 게시글 생성 페이지
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
  // 게시글 상세 페이지
  {
    path: '/review/:id',
    name: 'detail',
    component: DetailView
  },
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
