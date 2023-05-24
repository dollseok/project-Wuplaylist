<template>
  <div>
    <h4>담은 영화들</h4>
    <div class="playlist-content">
      <div class="movie-card column" v-for="movie in containedMovieList" :key="movie.id">
        <div class="movie-title">{{ movie.title }}</div>
        <img @click="addToPlaylist(movie)" class="movie-image" :src="movie.poster_path" alt="movieImage" width="200px" height="300px">
        <br>
        <button @click.prevent="deleteFromPlaylist(movie)">삭제</button>
      </div>
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
    },
    // 플레이리스트에 영화 추가
    addToPlaylist(movie) {
      this.containedMovieList.push(movie)
    },
  }
}
</script>

<style scoped>
.playlist-content {
  display: flex;
  overflow-x: auto;
}

.movie-title {
  display: flex;
  height: 50px;
  border: 1px solid grey;
  background-color: lightgrey;
  justify-content: center;
  align-items: center;
}

.movie-card {
  margin: 10px;
}
</style>