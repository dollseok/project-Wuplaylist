<template>
  <div class="home">
    <h1>HomeView</h1>
    <AllMovieList />
  </div>
</template>

<script>
import AllMovieList from '@/components/AllMovieList.vue'

export default {
  name: 'HomeView',
  components: {
    AllMovieList
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

  computed:{
  },
}
</script>
