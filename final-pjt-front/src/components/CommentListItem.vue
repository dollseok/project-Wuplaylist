<template>
  <div class="eachComment">
    <div v-if="updateStatus">
      <li>
        {{ author }} - {{ comment.content }}
        <button @click="updateMode">수정</button>
        <button @click="deleteComment">삭제</button>
      </li>
    </div>
    <!-- 수정 버튼을 누르지 않았을 때 -->
    <div v-else>
      <li>
        <input type="text" v-model="changedContent">
        <button @click="updateComment">저장</button>
        <button @click="updateMode">취소</button>
      </li>
    </div>
    <button v-if="isLiked" @click="likeComment">좋아요 취소</button>
    <button v-else @click="likeComment">좋아요</button>
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
    // console.log(this.comment.user)
    this.getUserDetail(this.comment.user)
  },
  mounted(){
    this.getCurrentUser()
  },
  methods: {
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
      console.log(this.articleId)
      console.log(this.comment.id)
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/${this.articleId}/comments_article/${this.comment.id}/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
      .then((res) => {
        console.log(res)
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

<style>

</style>