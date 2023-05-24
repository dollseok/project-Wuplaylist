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
  components: {
    ReviewListItem,
  },
  data(){
    return {

    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
  methods:{
    
  }
  
}
</script>

<style>

</style>