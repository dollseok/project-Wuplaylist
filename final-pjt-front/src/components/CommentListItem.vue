<template>
  <div class="eachComment">
    <div v-if="updateStatus">
      <li>
        <div class="each-comment">
          <div><span class="author" @click="goProfile">{{ author }}</span> - {{ comment.content }}</div>
          <div class="btn-package">
            <button class="btn" v-if="isLiked" @click="likeComment">{{ likeCount }} <font-awesome-icon :icon="['fas', 'heart']" size="lg" color="orangered" /></button>
            <button class="btn" v-else @click="likeComment">{{ likeCount }} <font-awesome-icon :icon="['far', 'heart']" size="lg" color="orangered" /></button>
            <button class="btn" @click="updateMode"><font-awesome-icon :icon="['far', 'pen-to-square']" /></button>
            <button class="btn" @click="deleteComment"><font-awesome-icon :icon="['fas', 'trash']" /></button>
          </div>
        </div>
      </li>
    </div>
    
    <!-- 수정 버튼을 눌렀을 때 -->
    <div v-else>
      <li>
        <div class="each-comment">
        <input type="text" v-model="changedContent">
        <div class="btn-package">
          <button class="btn" v-if="isLiked" @click="likeComment">{{ likeCount }} <font-awesome-icon :icon="['fas', 'heart']" size="lg" color="orangered" /></button>
          <button class="btn" v-else @click="likeComment">{{ likeCount }} <font-awesome-icon :icon="['far', 'heart']" size="lg" color="orangered" /></button>
          <button class="btn" @click="updateComment"><font-awesome-icon :icon="['fas', 'floppy-disk']" /></button>
          <button class="btn" @click="updateMode"><font-awesome-icon :icon="['fas', 'xmark']" /></button>
        </div>
        </div>
      </li>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
  },
  data() {
    return {
      updateStatus: true,
      changedContent: this.comment.content,
      author : null,
      articleId: null,
      likeCount: 0,
      isLiked: false,
    }
  },

  created(){
    this.getUserDetail(this.comment.user)
  },
  mounted(){
    this.getCurrentUser()
  },
  methods: {
    goProfile() {
        this.$router.push({ name: 'ProfileView', query: { data: JSON.stringify({userId: this.comment.user}) } })
    },
    updateMode() {
      this.updateStatus = !this.updateStatus
    },
    // 댓글 수정 메소드
    updateComment() {
      const content = this.changedContent

      axios({
        method: 'put',
        url: `${API_URL}/api/v1/comments_article/${this.comment.id}/`,
        data: { content }
      })
      .then(() => {
        this.$router.go(0)
      })
      .catch(err => console.log(err))
    },

    // 댓글 삭제 메소드
    deleteComment() {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/comments_article/${this.comment.id}/`
      })
      .then(() => {
        this.$router.go(0)
      })
      .catch(err => console.log(err))
    },

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
    // 댓글 좋아요
    likeComment() {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/comments_article/${this.comment.id}/likes/`,
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
    // 현재 접속한 유저의 id를 확인하고
    // 확인이 되었다면 comment의 세부정보를 가져옴
    // 현재 접속한 유저가 좋아요를 눌렀는지 여부 포함
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
        const userId = res.data.id
          // comment의 세부정보를 가져오는 요청
          axios({
            method: 'get',
            url: `${API_URL}/api/v1/comments_article/${this.comment.id}/`
          })
          .then((res) => {
            console.log(res.data)
            this.commentData = res.data // comment 정보
            this.articleId = res.data.article // 게시글 id
            // this.getUserDetail(res.data.user) // 작성자 세부정보 가져오기
            this.likeCount = res.data.like_user.length
            this.isLiked = this.checkLike(res.data.like_user, userId)

            // 이 부분 수정(username을 가져오기 위한 함수)
            // console.log(this.article.user)
          })
          .catch(err => {console.log(err)})            
        })
    .catch(err => console.log(err))
    },
    checkLike(list, userId) {
      if (list.indexOf(userId) != -1 ) {
          return true
      } else {
          return false
      }
    },
  }
}
</script>

<style scoped>
li {
  text-align: start;
}

.each-comment {
  display: flex;
  justify-content: space-between;
}

.author {
  cursor: pointer;
  font-weight: 800;
}
</style>