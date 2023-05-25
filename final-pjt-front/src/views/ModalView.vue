<template>
  <div>
    <!-- modal 창 -->
    <div class="movieModal black-bg">
      <div class="white-bg">
        <div class="modal-title">
          <h2>{{movie.title}} </h2>
          <div @click="modalclose">
            <font-awesome-icon :icon="['fas', 'xmark']" />
          </div>
        </div>

        <div class="container">
  
            <div class="modal-poster">
              <img class="modal-poster" :src="movie.poster_path" alt="poster">
            </div>
            <div class="modal-content">
              <p>개봉일 : {{movie.released_date}}</p>
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
  </div>
</template>

<script>


export default {
    name:"ModalView",
    data(){
        return {
          movie: this.$route.params.movie
        }
    },
    computed:{
      genres(){
        return this.$store.state.genres
      },
      getGenrename(){
        const genrenamesKR = []
        for (const genredata of this.genres) {
          if (this.movie.genres.includes(genredata['genre_id'])) {
            genrenamesKR.push(genredata['genre_name'])
          }
        }
        return genrenamesKR
      }
    },
    created() {
      // this.$store.dispatch('getGenres')
      console.log(this.$route.params.movie)
    },
    methods:{
      modalclose(){
        this.$router.go(-1)
      }
    }
}

</script>

<style scoped>

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


.modal-title {
  display: flex;
  justify-content: space-between;
  /* align-items: center; */
}


.modal-poster {
  width: auto;
  height: 100%;
}

.modal-content{
  width:60%;
  background-color: rgb(255, 255, 122, 0.1);;
}
.modal-content > p{
  margin-top: 30px;
}

</style>