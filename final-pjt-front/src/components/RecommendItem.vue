<template>
  <div>

    <!-- modal 창 -->
    <div class="movieModal black-bg" v-if="modalopen == true" @click="modalclose">
      <div class="white-bg">
        <h4>상세 페이지</h4>
        <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" alt="poster">
        <p> {{movie.title}} </p>
        <p>{{movie.released_date}}</p>
        <p>{{movie.vote_average}}</p>
        <p>{{movie.genres}}</p>
        <p>{{movie.overview}}</p>

        <button @click="modalclose">Close</button>
      </div>
    </div>


    <img @click="modalopen=true" class="modalImage"
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

.modalImage {
  width: 300px;
  height:450px; 
  border-radius: 10px;
  cursor: pointer;
}

</style>