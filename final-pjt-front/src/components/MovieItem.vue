<template>
  <div>

    <div class="container">
      <img :src="movie.poster_path" 
      alt="poster" class="image">
      <div class="overlay" @click="modalOpen">
        <div class="text">{{ movie.title }}</div>
      </div>
    </div>
    

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
      modalOpen(){
        this.$router.push({name:"ModalView", params:{ movie: this.movie,}} )
      }

    }
}
</script>

<style scoped>

.container {
  position: relative;
  width: 100%;
  padding:0; 
  margin: 5px;
}

.image {
  display: block;
  height: 300px;
  border: 1px solid black;

}

.overlay {
  position:absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 300px;
  width: 200.53px;
  opacity: 0;
  transition:.5s ease;
  background: white;

  display: flex;
  justify-content: center;
  align-items: center;
}

.container:hover .overlay {
  opacity: 0.9;
}

.text {
  color: black;
  font-size:20px;
  position:absolute;
  text-align: center;
}


</style>