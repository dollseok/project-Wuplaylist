<template>
  <div class="genre">
    <h1>Genre</h1>
    <div v-for="movie in allMovieList" :key="movie.id">
      {{ movie.title }}
      <br>
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
import axios from 'axios'
const API_URL='http://127.0.0.1:8000'

export default {
  name: 'GenreView',
  components: {
  },
  data() {
    return {
      allMovieList: [], 
    }
  },
  created() {
    // 전체 영화 데이터 불러오기
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`
    })
    .then((res) => {
      this.allMovieList = res.data
      console.log(this.allMovieList)
    })
    .catch(err => console.log(err))
  }
}
</script>

<style>

</style>