<template>
  <div class="home">
    <h1>HomeView</h1>
    <!-- <MovieCard 
    v-for=" movie in newMovies" :key=""
    />
    <MovieCard 
    v-for=" movie in topRatedMovies"
    /> -->

    <!-- <div class="movie-title" v-for="movie in movieData" :key="movie.id">
      <p>{{ movie.title }}</p>
      <img :src="`https://image.tmdb.org/t/p/w200${movie.poster_path}`" alt="">
    </div> -->
  </div>
</template>

<script>
// import movieData from '@/assets/movie_data.json'

export default {
  name: 'HomeView',
  components: {
  },
  computed: {
    // movieData() {
    //   return movieData.map((movie) => {
    //     return movie.fields
    //   })
    // }
  }
}
</script>
