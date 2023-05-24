<template>
  <div class="home">
    <h1>HomeView</h1>
    <AllMovieList />
    <!-- 추천 플레이리스트 (좋아요 순으로 출력하기) -->
    <div class="recommend-playlist">
      <!-- <ReviewListItem /> -->
    </div>
  </div>
</template>

<script>
import AllMovieList from '@/components/AllMovieList.vue'
// import ReviewListItem from '@/components/ReviewListItem.vue'

export default {
  name: 'HomeView',
  components: {
    AllMovieList,
    // ReviewListItem,
  },
  created() {
    this.getAllMovies()
    this.getGenres()
  },
  methods: {
    getAllMovies(){
      this.$store.dispatch('getAllMovies')
    },
    getGenres(){
      this.$store.dispatch('getGenres')
    }
  },

  computed:{
  },
}
</script>
