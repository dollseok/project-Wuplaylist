<template>
<div>

  <h1>All Movie List</h1>
  <div class="scroll movieItems">
    <MovieItem 
      v-for="movie in movies" 
      :key="movie.id" 
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

<style scoped>

.movieList {
  margin:0;
  padding:0;
  box-sizing: border-box;
}

.movieItems{
  display: flex;
  overflow-x: scroll;
  height: 340px;
  /* align-items: center; */
}

div::-webkit-scrollbar {
  height:20px;
}

div::-webkit-scrollbar-thumb{
  background-color: rgb(255, 255, 122);
  border-radius: 10px;
}

div::-webkit-scrollbar-track {
  background-color: rgb(228, 228, 228);
  opacity: 0.5;
  border-radius: 10px;
}



</style>