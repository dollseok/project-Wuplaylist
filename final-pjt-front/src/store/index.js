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
    createPersistedState({
    }),
  ],
  state: {
    articles: [
    ],
    token: null,
    currentUsername: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {  // commit으로 호출하여 사용
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SAVE_USER(state, currentUsername) {
      state.currentUsername = currentUsername
      localStorage.setItem('currentUsername', state.currentUsername)
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'review' })
    },
    DELETE_TOKEN(state) {
      state.token = null
    }
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
        // console.log(res, context)
        context.commit('GET_ARTICLES', res.data)
      })
      .catch(err => console.log(err))
    },
    // 회원가입
    signUp(context, payload) {
      const username = payload.username
      const password = payload.password
      const password2 = payload.password2
      const nickname = payload.nickname
      console.log(username)
      console.log(nickname)

      axios({
        method: 'post',
        url: `${API_URL}/accounts/user/signup/`,
        data: {
          username, password, password2, nickname,
        }
      })
      .then((res) => {
        // console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
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
        console.log(res)
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
      .then((res) => {
        context.commit('DELETE_TOKEN') 
        console.log(res)
      })
      .catch(err => console.log(err))
    }
  },
  modules: {
  }
})
