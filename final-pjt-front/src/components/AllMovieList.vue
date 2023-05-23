<template>
  <div>
    <h1>All Movie List</h1>
    <div class="movieList">
      <!-- <vueper-slides-->

      <MovieItem
        v-for="movie in movies" :key="movie.id"
        :movie="movie"
      />


    </div>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem.vue'

export default {
    name: 'AllMovieList',
    data(){
      return {
      }
    },
    computed : {
        movies(){
            return this.$store.state.movies
        },

    },
    components:{
        MovieItem,
    }
}
</script>

<style>

.movieList {
  display: flex;
  gap : 10px;
  height : 500px;
  overflow-x: auto;
}
</style>