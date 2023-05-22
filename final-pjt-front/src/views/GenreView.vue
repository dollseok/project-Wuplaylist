<template>
  <div class="genre">
    <h1>Genre</h1>
    
    <AllMovieList />

    <div v-for="movie in allMovieList" :key="movie.id">
      {{ movie.title }}
      <img :src="movie.poster_path" alt="movieImage">
    </div>



    <!-- 장르 버튼 -->
    <!-- <GenreButton /> -->
    <!-- 장르 영화 리스트 -->
    <!-- 전체 영화 데이터를 불러와서 List 컴포넌트에서 필터링해서 출력? -->
    <!-- <GenreMovieList /> -->
  </div>
</template>

<script>
import AllMovieList from '@/components/AllMovieList.vue'

// import axios from 'axios'
// const API_URL='http://127.0.0.1:8000'

export default {
  name: 'GenreView',
  components: {
    AllMovieList,
  },
  // data() {
  //   return {
  //     allMovieList: [], 
  //   }
  // },
  created() {
    this.getAllMovies()
  },
  methods: {
    getAllMovies(){
      this.$store.dispatch('getAllMovies')
      // console.log(this.$store.state.movies)
    },

    // 전체 영화 데이터 불러오기
    // axios({
    //   method: 'get',
    //   url: `${API_URL}/api/v1/movies/`
    // })
    // .then((res) => {
    //   this.allMovieList = res.data
    //   console.log(this.allMovieList)
    // })
    // .catch(err => console.log(err))
  },
}

</script>

<style>

</style>