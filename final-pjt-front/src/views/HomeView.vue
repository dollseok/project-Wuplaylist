<template>
  <div class="home">
    <h1>HomeView</h1>
    <AllMovieList />
    <!-- 추천 플레이리스트 (좋아요 순으로 출력하기) -->
    
    <div class="recommend-playlist">
      <ReviewPopular />
    </div>
  </div>
</template>

<script>
import AllMovieList from '@/components/AllMovieList.vue'
import ReviewPopular from '@/components/ReviewPopular.vue'

export default {
  name: 'HomeView',
  components: {
    AllMovieList,
    ReviewPopular,
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
