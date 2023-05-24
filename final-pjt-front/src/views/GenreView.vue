<template>
  <div>
    <h1>Select Genre</h1>
    <div class="genre">
      <div
        v-for="genre in genres" :key="genre.id"
        :class="['genre_button', { 'selected': checkSelected(genre.genre_id) }]"
        @click="selectedGenre(genre.genre_id)"        
      >
        {{ genre.genre_name }}
      </div>
    </div>
    <div>
      <h1>당신이 선택한 장르는?</h1>
      <span style="font-size : 30px;" v-for="genrename in selectedGenreNameList" :key="genrename.id">
        {{ genrename }}
      </span>
      <div class="movieList">
        <RecommendItem 
        class="recommendItem"
        v-for="movie in this.recommendMovies" :key="movie.id"
        :movie="movie"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import RecommendItem from '@/components/RecommendItem.vue'

export default {
  name: 'GenreView',
  components: {
    RecommendItem
  },
  data(){
    return {
      selectedGenreList : [],
      recommendMovies : {},
    }
  },
  methods : {
      // 선택되었는지 확인하는 함수
      checkSelected(genre_id){
        return this.selectedGenreList.includes(genre_id)
      },

      // 선택을 하고 취소 하는 함수
      selectedGenre(genre_id){
        if (this.selectedGenreList.includes(genre_id)){
          const index = this.selectedGenreList.indexOf(genre_id)
          if (index > -1) {
            this.selectedGenreList.splice(index, 1)
          }
        }
        else {
          this.selectedGenreList.push(genre_id)
        }
        
        this.GenreRecommendList()
      },

      GenreRecommendList(){
        let genreCode = ''
        for (const index in this.selectedGenreList){
          console.log(index)
          console.log(this.selectedGenreList.length - 1)
          if (index != this.selectedGenreList.length - 1){
            genreCode += this.selectedGenreList[index] + '%2C%20'
          }
          else {
            genreCode += this.selectedGenreList[index] 
          }
        }
        if (genreCode === ''){
          this.recommendMovies = {}
        }
        else {
          axios({
            method:'get',
            url : `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-Kr&page=1&sort_by=popularity.desc&with_genres=${genreCode}`,
            headers :{
              "accept": "application/json",
              "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0YjNlM2FhNjVlOTZlOTVjN2Y0MWZmMDdmY2NkMzAxYiIsInN1YiI6IjYzZDMxYTM4NWEwN2Y1MDA5ZTk4MDM0YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.svzZx8RMTp1kjkBzxbvcOuoduFUJjduTqyQf-ufCBfo"
            },
          })
          .then(res=> {
            this.recommendMovies = res.data.results
          })
          .catch(err=>console.log(err))
        }
      }
    },
  computed:{
    genres(){
      return this.$store.state.genres
    },
    selectedGenreNameList(){
      const nameList = []
      for (const genreId of this.selectedGenreList) {
        for (const genre of this.genres){
          if (genre.genre_id === genreId) {
            nameList.push(genre.genre_name)
          }
        }
      }
      return nameList

    }
    
  }
}

</script>

<style scoped>
.genre {
  display: flex;
  flex-wrap: wrap;
}
.genre_button{
  font-size: 13px;
  display: flex;
  margin: 10px;
  width: 70px;
  height: 35px;
  border: 1px solid black;
  border-radius: 10px;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.selected {
  background-color:rgb(169, 232, 236);
}

.movieList {
  display: flex;
  flex-wrap: wrap;
}

.recommendItem {
  margin:5px;
}

</style>