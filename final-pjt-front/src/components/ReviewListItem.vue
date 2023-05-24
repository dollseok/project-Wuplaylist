<template>
  <div class="each-review">
 
    <router-link
      :to="{name:'detail', params:{id: String(article.id)}, query: { 
          articleData: articleData,
         } }"
    >
    {{ article.title }}
    </router-link>
    <font-awesome-icon :icon="['fas', 'heart']" size="lg" color="orangered" /> {{ article.like_user.length }}
    <div class="moviePreview">
      <img id="movie-image" v-for="poster in moviePosters" :key="poster.id" :src="poster" alt="movieimage" width="100px" height="150px">
    </div>
    <!-- <hr> -->
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
      
    }
  }
}
</script>

<style scoped>
a {
  text-decoration: none;
  font-size: 25px;
  color: dimgray;
}

#movie-image {
  margin: 10px;
}
</style>