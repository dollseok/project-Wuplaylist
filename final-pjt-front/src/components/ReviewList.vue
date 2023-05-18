<template>
  <div class="review-list">
    <h3>review list</h3>
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
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
  components: {
    ReviewListItem,
  }
}
</script>

<style>

</style>