<template>
  <div class="playlist-content row">
    <h4>담은 영화들</h4>
    <div class="movie-card col" v-for="movie in containedMovieList" :key="movie.id">
      {{ movie.title }}
      <img class="movie-image" :src="movie.poster_path" alt="movieImage">
      <br>
      <button @click.prevent="deleteFromPlaylist(movie)">삭제</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContentView',
  data() {
    return {
      containedMovieList: this.containedMovie

    }
  },
  // 플레이리스트가 생성될 때 담은 영화 리스트
  props: {
    containedMovie: Array,
  },
  methods: {
    // 플레이리스트에서 영화 삭제
    deleteFromPlaylist(movie) {
      const movieIdx = this.containedMovieList.indexOf(movie)
      this.containedMovieList.splice(movieIdx, 1)
    }
  }
}
</script>

<style>

</style>