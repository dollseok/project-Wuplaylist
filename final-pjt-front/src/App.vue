<template>
  <div id="app">
    <!-- 로고 이미지 -->
    <nav class="d-flex p-2" id="mainNav">
      <div class="me-auto">
        <img src="./assets/우플리로고.jpg" alt="로고" style="width:100px;" class="p-2">
      </div>
      
      <div class="loginBar my-auto">
        <div v-if="token">
          <router-link :to="{ name: 'ProfileView', query: { data: JSON.stringify({ username: currentUsername }) } }" class="routerlink">프로필</router-link>
          <span v-if="token" @click="logout" class="routerlink">로그아웃</span> 
        </div>
        <div v-else class="my-auto">
          <router-link to="/login" class="routerlink"> 로그인</router-link>
          <router-link to="/signup" class="routerlink">회원가입</router-link>
        </div>
      </div>
    </nav>

    <nav id="routerNav">
      <router-link class="routerlink" to="/">홈</router-link>
      <router-link class="routerlink" to="/genre">장르별 추천</router-link>
      <router-link class="routerlink" to="/review">영화 리뷰</router-link>
      <!-- 토큰이 있을 때는 로그아웃 버튼 -->
      <!-- 없을 때는 로그인 버튼 -->
    </nav>
    <router-view :key="$route.fullPath" />
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
    },
    currentUsername() {
      return this.$store.state.currentUsername
    }
  }
}
</script>


<style>
@font-face {
  font-family: "cinema";
  src: url("./font/a시네마M.ttf");
}

#app {
  /* font-family: 'Noto Sans KR', sans-serif; */
  font-family: 'cinema';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  margin: 10px 10px
}

.routerlink{
  padding: 10px;
  text-decoration: none;
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

#mainNav {
  justify-content: center;
}

#routerNav {
  text-align: center;
}


</style>
