<template>
  <div class="review-list">
    <h2>인기 플레이리스트</h2>
    <hr>
    <h3>1위 <font-awesome-icon :icon="['fas', 'crown']" style="color: #ffd700;" /></h3>
    <ReviewListItem class="playlist-hot" :article="article1"/>
    <hr>
    <h3>2위 <font-awesome-icon :icon="['fas', 'crown']" style="color: #c0c0c0;" /></h3>
    <ReviewListItem class="playlist-hot" :article="article2"/>
    <hr>
    <h3>3위 <font-awesome-icon :icon="['fas', 'crown']" style="color: #8b4513;" /></h3>
    <ReviewListItem class="playlist-hot" :article="article3"/>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'

export default {
  name: 'ReviewList',
  components: {
    ReviewListItem,
  },
  data() {
    return {
      articles: this.$store.state.articles,
    }
  },
  computed: {
    sortedArticles() {
      const newArticles = []
      for (const article of this.$store.state.articles) {
        newArticles.push(article)
      }

      let editArticles = newArticles.sort(function(a,b){
        return b.like_user.length - a.like_user.length
      })
      return editArticles
    },
    article1(){
      return this.sortedArticles[0]
    },
    article2(){
      return this.sortedArticles[1]
    },
    article3(){
      return this.sortedArticles[2]
    }
  },
}
</script>

<style scoped>
.playlist-hot {
  padding: 10px;
  border-radius: 1rem;
  background-color: rgb(230, 230, 230);
}
</style>