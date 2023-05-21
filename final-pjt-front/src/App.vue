<template>
  <div id="app">
    <nav>
      <router-link to="/">홈</router-link> |
      <router-link to="/genre">장르별 추천</router-link> |
      <router-link to="/review">영화 리뷰</router-link> |
      <router-link to="/signup">회원가입</router-link> |
      <router-link to="/profile">프로필</router-link>
      <!-- 토큰이 있을 때는 로그아웃 버튼 -->
      <button v-if="token" @click="logout">로그아웃</button> 
      <!-- 없을 때는 로그인 버튼 -->
      <router-link v-else to="/login"> 로그인</router-link>

    </nav>
    <router-view/>
  </div>
</template>

<script>
import router from '@/router'

export default {
  methods: {
    logout(){
      this.$store.dispatch('logout')
      router.go(0)
    },
  },
  computed: {
    token() {
      return this.$store.state.token
    }
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
