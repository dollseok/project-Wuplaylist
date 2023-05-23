<template>
  <div>
    <h1>Choice Genre</h1>
    <div class="genre">
      <div
        v-for="genre in genres" :key="genre.id"
        class="genre_button"
      >
        {{ genre.genre_name }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'GenreList',
    data(){
      return {}
    },
    computed :{
      genres(){
        return this.$store.state.genres
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
  margin: 10px;
  width: 70px;
  height: 50px;
  background-color: yellow;

}

</style>