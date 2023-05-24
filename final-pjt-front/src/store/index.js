import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

// $router에 접근할 수 없기 때문에 import
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [],
    popularArticles:[],
    // 유저 관련
    token: null,
    currentUsername: null,
    currentUser:null,
    
    // 영화 관련
    movies: [],
    genres: [],
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {  // commit으로 호출하여 사용
    GET_POPULAR_ARTICLES(state, articles){
      console.log(articles)
      state.popularArticles
    },

    GET_ARTICLES(state, articles) {
      state.articles
      state.articles = articles
    },
    SAVE_USER(state, currentUsername) {
      state.currentUsername = currentUsername
      localStorage.setItem('currentUsername', state.currentUsername)
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.go(-1)
    },
    DELETE_TOKEN(state) {
      state.token = null
    },

    //영화 전체 리스트
    GET_ALL_MOVIES(state, movies){
      state.movies = movies
    },

    // 장르 전체 리스트
    GET_ALL_GENRES(state, genres){
      state.genres = genres
    },

    GET_CURRENT_USER(state, user){
      state.currentUser = user
    },

  },
  actions: {  // dispatch로 호출하여 사용
    // 리뷰 게시글 불러오는 요청
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then((res) => {
        context.commit('GET_ARTICLES', res.data)
        context.commit('GET_POPULAR_ARTICLES',res.data)
      })
      .catch(err => console.log(err))
    },
    // 회원가입
    signUp(context, payload) {
      const username = payload.username
      const password = payload.password
      const password2 = payload.password2
      const nickname = payload.nickname

      axios({
        method: 'post',
        url: `${API_URL}/accounts/user/signup/`,
        data: {
          username, password, password2, nickname,
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        alert('회원가입이 완료되었습니다.')
      })
      .catch(err => console.log(err))
    },
    // 로그인
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
      .then((res) => {
        context.commit('SAVE_USER', username)
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => console.log(err))
    },
    // 로그아웃
    logout(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`
      })
      .then(() => {
        context.commit('DELETE_TOKEN') 
      })
      .catch(err => console.log(err))
    },

    // 전체 영화 데이터 불러오기
    getAllMovies(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
      })
      .then((res) => {
        context.commit('GET_ALL_MOVIES', res.data)
      })
      .catch(err => console.log(err))
    },

    // 전체 장르 데이터 불러오기
    getGenres(context){
      axios({
        method:'get',
        url: `${API_URL}/api/v1/genres/`
      })
      .then((res) => {
        context.commit('GET_ALL_GENRES', res.data)
      })
      .catch(err => console.log(err))
    },

    // 현재 유저 데이터 가져오기
    getCurrentUser(context){
      axios({
          method: 'get',
          url:`${API_URL}/accounts/user/current/`,
          headers:{
              Authorization: `Token ${this.state.token}`
          }
      })
      .then((res) => {
        context.commit('GET_CURRENT_USER', res.data)
      })
      .catch((err) => 
        console.log(err))
  },

  },
  modules: {
  }
})
