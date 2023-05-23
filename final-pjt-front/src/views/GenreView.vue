<template>
  <div class="genre">
    <h1>Main</h1>
    
    <AllMovieList />

    <!-- <div v-for="movie in allMovieList" :key="movie.id">
      {{ movie.title }}
      <img :src="movie.poster_path" alt="movieImage">
    </div> -->



    <!-- 장르 버튼 -->
    <!-- <GenreButton /> -->
    <!-- 장르 영화 리스트 -->
    <!-- 전체 영화 데이터를 불러와서 List 컴포넌트에서 필터링해서 출력? -->
    <!-- <GenreMovieList /> -->
  </div>
</template>

<script>
import AllMovieList from '@/components/AllMovieList.vue'

export default {
  name: 'GenreView',
  components: {
    AllMovieList,
  },
  computed:{
    allMovieList(){
      return this.$store.state.movies
    }
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
}

</script>

<style>

</style>