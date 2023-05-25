<template>
  <div class="review-list">
    <hr>
    <ReviewListItem 
    v-for="article in articles" :key="article.id"
    :article="article"
    />
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'

export default {
  name: 'ReviewList',
  data() {
    return {
      articles: this.$store.state.articles
    }
  },
  components: {
    ReviewListItem,
  }
}
</script>

<style>

</style>