<template>
  <div>
    <h1>All Movie List</h1>
    <div class="movieList">
      <!-- <vueper-slides
        class="no-shadow"
        :infinite="false"
        :bullets="false"
        :visible-slides="3"
        :slide-ratio="1 / 4"
        :dragging-distance="70"
        :gap="3"
        >

        <template #arrow-left>
          <i class="icon icon-arrow-left" />
        </template>

        <template #arrow-right>
          <i class="icon icon-arrow-right" />
        </template>
        
        <vueper-slide v-for="(movie,i) in movies" :key="i" 
          :image="movie.poster_path"
        />
      </vueper-slides> -->

      <MovieItem
        v-for="movie in movies" :key="movie.id"
        :movie="movie"
      />


    </div>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem.vue'

// import { VueperSlides, VueperSlide } from 'vueperslides'
// import 'vueperslides/dist/vueperslides.css'

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
        // VueperSlides, 
        // VueperSlide,
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