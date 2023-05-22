<template>
  <div>
    <h1>All Movie List</h1>
    <MovieItem 
        
        v-for="movie in movies" :key="movie.id"
        :movie="movie"
    />
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem.vue'

export default {
    name: 'AllMovieList',
    computed : {
        movies(){
            return this.$store.state.movies
        }
    },
    components:{
        MovieItem,
    }
}
</script>

<style>

</style>