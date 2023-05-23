<template>
  <div class="each-review">
    <p>{{ article.title }}</p>
    <div class="moviePreview">
      <img id="movie-image" v-for="poster in moviePosters" :key="poster.id" :src="poster" alt="movieimage" width="100px" height="150px">
    </div>
    <router-link
      :to="{name:'detail', params:{id: String(article.id)}, query: { 
          articleData: articleData,
         } }"
    >
    [DETAIL]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ReviewListItem',
  components: {
    
  },
  props: {
    article: Object,
  },
  data() {
    return {
      articleData: this.article,
      totalMovies: this.$store.state.movies,
      moviePosters: [],
    }
  },
  created() {
    this.getMoviePoster()
  },
  methods: {
    getMoviePoster() {
      for (const movie of this.totalMovies) {
        if (this.article.contain_movies.includes(movie.id)) {
          this.moviePosters.push(movie.poster_path)
        }
      }
      console.log(this.moviePosters)
    }
  }
}
</script>

<style>

#movie-image {
  margin: 10px;
}
</style>