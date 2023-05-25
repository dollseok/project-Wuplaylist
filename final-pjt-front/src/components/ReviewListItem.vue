<template>
  <div class="each-review">
    <div class="title-bar">
      <div>
        <router-link
          :to="{name:'detail', params:{id: String(article.id)}, query: { 
              articleData: articleData,
            } }"
        >
        # {{ article.title }}
        </router-link>
      </div>
      <div>
        <font-awesome-icon class="flex-end" :icon="['fas', 'heart']" size="lg" color="orangered" /> 
        <span>
          {{ article.like_user.length }}
        </span>
      </div>

    </div>
    
    <div class="scroll moviePreview">
      <img id="movie-image" v-for="poster in moviePosters" :key="poster.id" :src="poster" alt="movieimage" width="100px" height="150px">
    </div>
    <br>

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
  mounted() {
    this.getMoviePoster()
    // console.log(this.article)
  },
  methods: {
    // 플레이리스트 미리보기를 위해 담긴 영화들의 포스터 링크 가져오기
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

.moviePreview {
  display: flex;
  overflow-x: auto;
}

div::-webkit-scrollbar {
  height:10px;
}

div::-webkit-scrollbar-thumb{
  background-color: rgb(34, 194, 119, 0.8);
  border-radius: 10px;
}

div::-webkit-scrollbar-track {
  background-color: rgb(228, 228, 228);
  opacity: 0.5;
  border-radius: 10px;
}

.title-bar{
  display: flex;
  justify-content: space-between;
  align-items: center;
}

</style>