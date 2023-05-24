<template>
  <div>
    <!-- modal 창 -->
    <div class="movieModal black-bg">
      <div class="white-bg">
        <h4>상세 페이지</h4>
        <img :src="movie.poster_path" alt="poster">
        <p> {{movie.title}} </p>
        <p>{{movie.released_date}}</p>
        <p>{{movie.vote_average}}</p>
        <p>{{movie.genres}}</p>
        <p>{{movie.overview}}</p>

        <button @click="modalclose">Close</button>
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
    created() {
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

</style>