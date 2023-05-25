<template>
  <div id="app">
    <!-- 로고 이미지 -->
    <nav class="d-flex p-0 py-3" id="mainNav">
      <div class="me-auto leftnav">
        <img src="./assets/우플리로고2.jpg" alt="로고" style="height:70px;" class="m-auto">
        <nav id="routerNav">
          <router-link class="routerlink" to="/">홈</router-link>
          <router-link class="routerlink" to="/genre">장르별로 보기</router-link>
          <router-link class="routerlink" to="/review">플레이리스트</router-link>
        </nav>
      
      </div>
      
      <div class="loginBar my-auto">
        <!-- 토큰이 있을 때는 로그아웃 버튼 -->
        <!-- 없을 때는 로그인 버튼 -->
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

    
    <!-- 다른 유저의 프로필에서 나의 프로필로  -->
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
  margin: 10px 10px;
  padding: 2px;
}

.routerlink{
  padding: 10px;
  text-decoration: none;
  font-weight: 800;
  font-size: 20px;
  cursor: pointer;
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

.leftnav {
  display: flex;
}


</style>
