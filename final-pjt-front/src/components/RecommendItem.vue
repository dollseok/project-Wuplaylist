<template>

  <div>

    <!-- modal 창 -->
    <div class="movieModal black-bg" v-if="modalopen == true" @click="modalclose">
      <div class="white-bg">
        <div class="modal-title">
          <h2>{{movie.title}} </h2>
          <div @click="modalclose" class="x-button">
            <font-awesome-icon :icon="['fas', 'xmark']" />
          </div>
        </div>
        <div class="container-box">
 
            <div class="modal-poster">
              <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" alt="poster">
            </div>
            <div class="modal-content">
              <p>개봉일 : {{movie.release_date}}</p>
              <p>평점 : {{movie.vote_average}}</p>
              <p>장르 : 
                <span v-for="genrename in getGenrename" :key="genrename.id">
                {{genrename}}
              </span>
              </p>
              <p>{{movie.overview}}</p>
            </div>

        </div>
      </div>
    </div>
    <img v-if="movie.poster_path" @click="modalopen=true" class="movieImage"
    :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" 
    alt="poster">
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
          modalopen: false,
          movies : this.movies,
        }
    },
    computed:{
      genres(){
        return this.$store.state.genres
      },
      getGenrename(){
        const genrenamesKR = []
        for (const genredata of this.genres) {
          if (this.movie.genre_ids.includes(genredata['genre_id'])) {
            genrenamesKR.push(genredata['genre_name'])
          }
        }
        return genrenamesKR
      }
    },
    methods:{
      modalclose(){
        this.modalopen = false
      }

    }
}
</script>

<style>
body {
  margin : 0
}
div {
  box-sizing : border-box;
}
.black-bg {
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
  position: fixed;
  top:0px;
  left:0px;
  padding: 20px;
}
.white-bg {
  width: 100%;
  background: white;
  border-radius: 8px;
  padding: 20px;
}

.movieModal {
  height: 100%;
  width: 100%;
  overflow: auto;
}

.movieImage {
  width: 245px;
  height:367.5px; 
  border-radius: 10px;
  cursor: pointer;
}

.container-box{
  display: flex;
}

.modal-poster {
  width: auto;
  height: 100%;
  margin-right: 10px;
}

.modal-content{
  width:60%;
  /* background-color: rgb(255, 255, 122, 0.5); */
}
.modal-content > p{
  margin-bottom: 30px;
}

.modal-title {
  display: flex;
  justify-content: space-between;
  /* align-items: center; */
}

.x-button {
  cursor: pointer;
}

</style>