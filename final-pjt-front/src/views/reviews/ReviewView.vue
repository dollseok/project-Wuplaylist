<template>
  <div class="review">
    <h1>Review</h1>
    <router-link to="/create">글 작성하기</router-link>
    <ReviewList />
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'

export default {
  name: 'ReviewView',
  components: {
    ReviewList,
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      this.$store.dispatch('getArticles')
    }
  }
}
</script>

<style>

</style>