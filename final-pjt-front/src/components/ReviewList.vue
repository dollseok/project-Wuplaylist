<template>
  <div class="review-list">
    <hr>
    <ReviewListItem 
    class="review-item"
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

<style scoped>

.review-list {
  display: flex;
  flex-wrap: wrap;
}

.review-item {
  padding:10px;
  margin: 10px;
  width: 47%;
  border: 2px solid black;
  border-radius:10px
}

</style>