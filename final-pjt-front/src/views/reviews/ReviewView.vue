<template>
  <div class="review">
    <h1>무비 플레이리스트</h1>
    <router-link to="/create">글 작성하기</router-link>
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

<style>

</style>