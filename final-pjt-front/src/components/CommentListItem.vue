<template>
  <div class="eachComment">
    <div v-if="updateStatus">
      <li>
        {{ comment.content }}
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
      changedContent: null,
    }
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
  }
}
</script>

<style>

</style>