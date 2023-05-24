<template>
  <div>
    <hr>
    <div v-if="updatestatus">
      <h2>{{ article?.title }}</h2>
      <hr>
      <div class="d-flex">
        <span @click="goProfile">작성자 : {{ author }}</span>
        <div class="article-time">
          <p>작성시각 : {{ article?.created_at }} |  수정시각 : {{ article?.updated_at }}</p>
        </div>
      </div>
      <p>{{ article?.content }}</p>

      <!-- 플레이리스트에 담긴 영화들 -->
      <div class="contain-movies">
        <div class="column">
          <div v-for="movie in playlist_movies" :key="movie.id">
            <figure><img id="movie-image" :src="movie.poster_path" alt="movieImage" width="150px" height="225px"></figure>
            <span>{{ movie.title }}</span>
            <button v-if="!updatestatus" @click="deleteFromPlaylist(movie)">삭제</button>
          </div>
        </div>
      </div>
      
      <button class="btn btn-primary" @click="updateMode">수정</button>
      <button class="btn btn-danger" @click="deleteArticle">삭제</button>
      <button class="btn btn-secondary" @click="goBack">목록</button>
      
    </div>
    <!-- 수정버튼을 눌렀을 때 -->
    <div v-else>
      <h2><input type="text" v-model="changedTitle"></h2>
      <hr>
      <p>내용 : <input type="text" v-model="changedContent"></p>

      <!-- 플레이리스트에 담긴 영화들 -->
      <div class="contain-movies">
        <div class="column">
          <div v-for="movie in playlist_movies" :key="movie.id">
            <figure><img id="movie-image" :src="movie.poster_path" alt="movieImage" width="150px" height="225px"></figure>
            <span>{{ movie.title }}</span>
            <button class="btn" v-if="!updatestatus" @click="deleteFromPlaylist(movie)"><font-awesome-icon :icon="['fas', 'xmark']" /></button>
          </div>
        </div>
      </div>

      <button class="btn btn-primary" @click="updateArticle">저장</button>
      <button class="btn btn-danger" @click="updateMode">취소</button>
    </div>
    <button class="btn" v-if="isLiked" @click="likeArticle">{{ likeCount }} <font-awesome-icon :icon="['fas', 'heart']" size="lg" color="orangered" /></button>
    <button class="btn" v-else @click="likeArticle">{{ likeCount }} <font-awesome-icon :icon="['far', 'heart']" size="lg" color="orangered" /></button>

    <hr>
    <CommentList 
    v-if="article"
    :articleId="article?.id"
    />
  </div>
</template>

<script>
import CommentList from '@/components/CommentList.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components: {
    CommentList
  },
  props: {
    id: String,
  },
  data() {
    return {
      article: null,
      author: null,
      updatestatus: true,
      changedTitle: this.$route.query.articleData.title,
      changedContent: this.$route.query.articleData.content,
      changedContainMoviesId: [],

      currentUser: {},
      isLiked: false,
      likeCount: 0,

      playlist_movies: [],
    }
  },
  mounted() {
    this.getCurrentUser()
  },

  methods: {
    // 해당 글에 담긴 영화들을 가져오는함수
    getPlaylistMovies() {
      const movies = this.$store.state.movies // 전체 영화 데이터
      if (this.article.contain_movies) {
        for (const movieId of this.article.contain_movies) {
          this.playlist_movies.push(movies[movieId-1])
          this.changedContainMoviesId.push(movieId)
        }
      }
    },
    // 해당 게시글 좋아요를 누른 사용자인지 확인하는 함수
    checkLike(list, userId) {
      if (list.indexOf(userId) != -1 ) {
          return true
      } else {
          return false
      }
    },
    // -----------------------------------------
    // getArticleDetail() {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/api/v1/articles/${this.$route.query.id}/`
    //   })
    //   .then((res) => {
    //     // console.log(res.data.like_user)
    //     this.article = res.data
    //     this.getUserDetail(this.article.user)
    //     this.likeCount = res.data.like_user.length
    //     this.isLiked = this.checkLike(res.data.like_user, this.currentUser.id)
    //     console.log(this.currentUser.id)

    //     // 이 부분 수정(username을 가져오기 위한 함수)
    //     // console.log(this.article.user)
    //   })
    //   .catch(err => {console.log(err)})
    // },
    // -----------------------------------------

    // user의 디테일을 가져오기 위한 method
    getUserDetail(userId){
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/detail/${userId}/`
      })
      .then((res)=>{
        this.author = res.data.username
      })
      .catch(err=>console.log(err))
    },
    // 해당 작성자의 프로필로 이동
    goProfile() {
        this.$router.push({ name: 'ProfileView', query: { data: JSON.stringify({userId: this.article.user}) } })
    },
    
    updateMode() {
      this.updatestatus = !this.updatestatus
    },
    // 글 수정
    updateArticle() {
      const title = this.changedTitle
      const content = this.changedContent
      const contain_movies = this.changedContainMoviesId
      // const articleUser = this.article.user

      axios({
        method: 'put',
        url: `${API_URL}/api/v1/articles/${this.id}/`,
        data: { title, content, contain_movies }
      })
      .then(() => {
        this.$router.go(0)
      })
      .catch(err => console.log(err))
    },
    // 글 삭제
    deleteArticle() {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/articles/${this.id}/`,
      })
      .then(() => {
        this.$router.push({ name: 'review' })
      })
    },
    goBack() {
      this.$router.push({ name: 'review'})
    },
    // 플레이리스트 영화 삭제
    deleteFromPlaylist(movie) {
      const movieIdx = this.playlist_movies.indexOf(movie)
      this.playlist_movies.splice(movieIdx, 1)
      this.changedContainMoviesId.splice(movieIdx, 1)
    },
    // 게시글 좋아요
    likeArticle() {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/${this.article.id}/likes/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
      .then((res) => {
        this.likeCount = res.data.like_user.length
        this.isLiked = !this.isLiked
      })
      .catch(err => console.log(err))
    },
    getCurrentUser(){
        axios({
            method: 'get',
            url:`${API_URL}/accounts/user/current/`,
            headers:{
                Authorization: `Token ${this.$store.state.token}`
            }
        })
        .then((res) => {
            this.currentUser = res.data
            const userId = res.data.id // 현재 접속한 유저의 id
              axios({ // Article의 세부정보를 가져오는 요청
                method: 'get',
                url: `${API_URL}/api/v1/articles/${this.id}/`
              })
              .then((res) => {
                this.article = res.data
                this.getUserDetail(this.article.user) // 작성자 username 가져오는 함수
                this.likeCount = res.data.like_user.length
                this.isLiked = this.checkLike(res.data.like_user, userId) // 접속한 유저가 좋아요를 눌렀는지 확인
                this.getPlaylistMovies() // 플레이리스트의 영화들 가져오기
              })
              .catch(err => {console.log(err)})            
            })
        .catch(err => console.log(err))
    },
  }
}
</script>

<style scoped>

#movie-image:hover {
  /* 마우스를 올렸을 때 손바닥 모양 커서 */
  cursor: pointer;
  /* 서서히 느려지게 */
  transition: all 0.2s linear; 
  /* 이미지 확장 */
  transform: scale(1.1);
}

.column {
  margin: 15px 15px 0;
  padding: 0;
}

.column:last-child {
  padding-bottom: 60px;
}

.column::after {
  content: '';
  clear: both;
  display: block;
}

.column div {
  position: relative;
  float: left;
  width: 160px;
  height: 250px;
  margin: 0 0 0 25px;
  padding: 0;
}

.column div:first-child {
  margin-left: 0;
}

.column div span {
  position: absolute;

  z-index: -1;
  display: block;
  width: 160px;
  margin: 0;
  padding: 0;
  color: #444;
  font-size: 18px;
  text-decoration: none;
  text-align: center;
  -webkit-transition: .3s ease-in-out;
  transition: .3s ease-in-out;
  opacity: 0; 
}

figure {
  width: 160px;
  height: 250px;
  margin: 0;
  padding: 0;
  background: #fff;
}
figure:hover+span {
  bottom: -55px;
  opacity: 1;
}

.d-flex {
  padding-left: 20px;
  padding-right: 20px;
  justify-content: space-between;
}

.article-time {
  float: right;
}
</style>