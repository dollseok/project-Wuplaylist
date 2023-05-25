<template>
  <div class="review">
    <div class="view-nav">
      <h1>무비 플레이리스트</h1>
      <router-link to="/create"><font-awesome-icon :icon="['far', 'pen-to-square']" /> 작성하기</router-link>
    </div>
    <ReviewList/>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'

export default {
  name: 'ReviewView',
  components: {
    ReviewList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LoginView' })
      }

    }
  }
}
</script>

<style scoped>
.view-nav {
  margin: 0 10px;
  padding: 10px;
  border-top: 1px solid;
  border-bottom: 1px solid;
  border-radius: 1rem;
  width:96%;

}

a {
  text-decoration: none;
  margin-left: 10px;
  font-size: 20px;
}

</style>