<template>
  <div>
    <div class="view-nav">
      <h1>당신이 선택할 장르는?</h1>
    </div>
    <div class="genre">
      <div
        v-for="genre in genres" :key="genre.id"
        :class="['genre_button', { 'selected': checkSelected(genre.genre_id) }]"
        @click="selectedGenre(genre.genre_id)"        
      >
        {{ genre.genre_name }}
      </div>
      <div @click="resetGenre" class="resetButton">전체해제</div>
    </div>
    <div>
      
      <!-- <span style="font-size : 30px;" v-for="genrename in selectedGenreNameList" :key="genrename.id">
        {{ genrename }}
      </span> -->

      <div v-if="selectedGenreList.length === 0" class="message1">선택한 장르가 없습니다</div>
      <div v-else-if="recommendMovies.length===0" class="message1">관련 영화가 없습니다</div>    
      <div v-else class="movieList">
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
        console.log(this.selectedGenreList)
        console.log(this.recommendMovies)
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
      },
      resetGenre(){
        this.selectedGenreList = []
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
    
  },
}

</script>

<style scoped>
.view-nav {
  margin: 0 10px;
  padding: 10px;
  border-top: 1px solid;
  border-bottom: 1px solid;
  border-radius: 1rem;

}

.genre {
  display: flex;
  flex-wrap: wrap;
}
.genre_button{
  font-size: 15px;
  display: flex;
  margin: 10px;
  width: 90px;
  height: 35px;
  cursor: pointer;
  border: 1px solid black;
  border-radius: 10px;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.resetButton {
  background-color: rgb(253, 62, 62, 0.5);
  margin: 10px;
  padding: 10px;
  border-top: 1px solid;
  border-bottom: 1px solid;
  border-radius: 1rem;
  font-size: 15px;
  display: flex;
  width: 90px;
  height: 35px;
  border: 1px solid black;
  border-radius: 10px;
  justify-content: center;
  align-items: center;
  text-align: center;
  cursor: pointer;
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

h1 {
  margin: 0;
}

.message1 {
  font-size: 50px;
  margin-top: 100px;
  text-align: center;
}
</style>