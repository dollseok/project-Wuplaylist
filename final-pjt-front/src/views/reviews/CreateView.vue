<template>
  <div>
    <h1>플레이리스트 만들기</h1>
    <hr>
    <!-- 영화 추가하는 모달 팝업 -->
    <div class="movieModal black-bg" v-if="isModalViewed" @close-modal="isModalViewed=false">
      <div class="white-bg">
          <h4><font-awesome-icon :icon="['fas', 'film']" size="lg" /> 플레이리스트에 영화 담기 </h4>
          <hr>
          <label for="searchKeyword">검색어 </label>
          <button class="btn closebtn" @click="isModalViewed=false"><font-awesome-icon :icon="['fas', 'xmark']" /></button>
        <input v-model="searchKeyword" @keyup.enter="searchMovie" id="searchKeyword">
        <br>
        <div class="column">
          <div class="searchedMovies" v-for="movie in movielist" :key="movie.id">
            <div class="movie-card">
              <div class="movie-title">{{ movie.title }}</div>
              <img :class="{selected: containedMovie.includes(movie)}" @click="addToPlaylist(movie)" id="movie-image" :src="movie.poster_path" alt="movieImage" width="200px" height="300px">
            </div>
          </div>
        </div>
      </div>
    </div>

    
    
    <form @submit.prevent="createArticle">
      <div class="container">
        <div>
        <label class="label" for="title">제목 : </label>
        <input class="title-form" type="text" id="title" v-model="title">
        </div>
        <div>
        <label class="label" for="content">내용 : </label>
        <textarea 
          class="content-form"
          id="content" cols="30" rows="10"
          v-model="content"
        >
        </textarea>
        </div>
      </div>
      <br>
      <ContentView 
      :containedMovie="containedMovie"
      />
      <hr v-if="!isModalViewed">
      <button class="btn addMoviebtn" @click.prevent="isModalViewed=true"><font-awesome-icon :icon="['fas', 'film']" size="lg" /> 영화 담기</button>
      <input class="btn btn-success" type="submit" id="submit" value="작성">
    </form>

  </div>
</template>

<script>
import ContentView from '@/components/ContentView.vue'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'CreateView',
  components: {
    ContentView
  },
  data() {
    return {
      title: null,
      content: null,

      isModalViewed: false, // 모달창을 띄울지 말지를 결정하는 변수
      searchKeyword: '',    // 검색 키워드
      totalMovielist: this.$store.state.movies, // db에 있는 전체 영화 리스트
      movielist: [],        // 키워드가 포함된 영화 리스트 (검색마다 초기화)
      containedMovie: []    // 해당 플레이리스트에 추가된 영화 리스트

    }
  },
  methods: {
    // moveToContent(articleNum, id) { // 영화 클릭시 해당 영화 디테일로 이동
    //   window.location.href = 'http://127.0.0.1.8080/'
    // },

    // 플레이리스트에 추가할 영화 검색 (제목으로만)
    searchMovie() {
      if (this.searchKeyword == '') {
        alert('키워드가 없습니다!')
      } else {
        this.movielist = []
        this.totalMovielist.forEach(movie => {
          const movieTitle = movie.title.replace(/(\s*)/g, "") 
          // str.replace(/(\s*)/g, "") 문자열의 모든 공백 제거
          if (movieTitle.includes(this.searchKeyword.replace(/(\s*)/g, ""))) {
            this.movielist.push(movie)
          }
        })     
      }

    },
    // 플레이리스트에 영화를 추가
    addToPlaylist(movie) {
      if (this.containedMovie.includes(movie)) {
        alert('이미 들어있는 영화입니다.')
      } else {
        this.containedMovie.push(movie)
      }
    },
    // 플레이리스트 생성
    createArticle() {
      const title = this.title
      const content = this.content
      const containMovie = this.containedMovie
      const contain_movies = []
      containMovie.forEach(movie => {
        console.log(movie.id)
        contain_movies.push(movie.id)
      })
      
      
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: {title, content, contain_movies},
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
      .then(() => {
        this.$router.push({ name: 'review' })
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>
  .closebtn {
    float: right;
  }

  /* 밑에서 지정한 width와 height를 넘어가는 경우 스크롤이 생성된다. */
  .movieModal {
    width: 100%;
    height: 100%;
    overflow: auto;
  }

  #movie-image {
    cursor: pointer;
  }

  .input-form {
    width: 95%;
  }

  .container {
    margin-left: 0;
    margin-right: auto;
  }

  .container * {
    display: flex;
  }

  .content-form * {
    vertical-align: middle;
  }

  .column {
    display: flex;
    overflow-x: auto;
    margin-top: 10px;
  }

  .movie-card {
    margin-right: 10px;
    text-align: center;
  }

  .movie-title {
    display: flex;
    width: 200px;
    height: 50px;
    /* border: 1px solid grey; */
    color: black;
    background-color: rgb(245, 245, 245);
    justify-content: center;
    align-items: center;
  }

  .selected {
    opacity: 0.5;
  }

  .title-form {
    width : 50%;
    margin-bottom: 20px;
    margin-left: 10px;
  }
  .content-form {
    width: 50%;
    height: 80px;
    resize: none;
    margin-left: 10px;
  }

  .label {
    font-size: 17px;
  }
</style>