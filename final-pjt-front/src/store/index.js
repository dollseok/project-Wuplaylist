import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    articles: []
  },
  getters: {
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    }
  },
  actions: {
    getArticles(context) {
      // 리뷰 게시글 불러오는 요청
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
      })
      .then((res) => {
        // console.log(res, context)
        context.commit('GET_ARTICLES', res.data)
      })
      .catch(err => console.log(err))
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
    }
  },
  modules: {
  }
})
