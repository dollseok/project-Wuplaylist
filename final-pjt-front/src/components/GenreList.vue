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
      <h1>선택한 장르에 따른 영화 추천</h1>
      
    </div>

  </div>
</template>

<script>
export default {
    name: 'GenreList',
    data(){
      return {
        selectedGenreList : []
      }
    },
    methods : {
      checkSelected(genre_id){
        return this.selectedGenreList.includes(genre_id)
      },
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
      }
    },
    computed:{
      genres(){
        return this.$store.state.genres
      },    
    }
}
</script>

<style scoped>
.genre {
  display: flex;
  flex-wrap: wrap;
}
.genre_button{
  margin: 10px;
  width: 100px;
  height: 50px;
  border: 1px solid black;
  border-radius: 10px;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.selected {
  background-color:rgb(169, 232, 236);
}

</style>