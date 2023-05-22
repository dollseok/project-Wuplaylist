<template>
  <div>
    <img :src="movie.poster_path" alt="poster">
  </div>
</template>

<script>
export default {
    name:'MovieItem',
    props: {
        movie: Object,
    },
    data(){
        return {
            movies : this.movies
        }
    }
}
</script>

<style>

</style>