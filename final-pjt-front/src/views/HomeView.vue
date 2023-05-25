<template>
  <div class="home">
    <AllMovieList />
    <!-- 추천 플레이리스트 (좋아요 순으로 출력하기) -->
    
    <div class="menu2">

        <div class="recommend-playlist">
          <ReviewPopular />
        </div>
        <div class="follow-playlist">
          <FollowPlaylist/>
        </div>

    </div>
  </div>
</template>

<script>
import AllMovieList from '@/components/AllMovieList.vue'
import ReviewPopular from '@/components/ReviewPopular.vue'
import FollowPlaylist from '@/components/FollowPlaylist.vue'

export default {
  name: 'HomeView',
  components: {
    AllMovieList,
    ReviewPopular,
    FollowPlaylist,
  },
  mounted() {
    this.getAllMovies()
    this.getGenres()
  },
  methods: {
    getAllMovies(){
      this.$store.dispatch('getAllMovies')
    },
    getGenres(){
      this.$store.dispatch('getGenres')
    },
  },

  computed:{
  },
}
</script>

<style scoped>
.menu2 {
  display: flex;
}

.recommend-playlist{
  padding: 10px;
  width:50%;
  border: 1px solid black;
  margin: 10px;
  border-radius: 10px;
}
.follow-playlist{
  padding: 10px;
  width:50%;
  border: 1px solid black;
  margin: 10px;
  border-radius: 10px;
}


</style>