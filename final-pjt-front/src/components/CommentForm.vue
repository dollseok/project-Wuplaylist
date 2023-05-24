<template>
  <div>
    <input type="text" placeholder="댓글을 입력하세요" v-model="content" >
    <button @click="createComment">작성</button>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentForm',
  data() {
    return {
      content: null,
    }
  },
  props: {
    articleId: Number,
  },
  methods: {
    // 댓글 작성 메소드
    createComment() {
      const content = this.content

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/${this.articleId}/comments_article/`,
        data: { content },
        // headers 추가로 댓글 작성 가능하게 함(user data의 요구)
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
      .then(() => {
        // 인자로 넘긴 숫자만큼 히스토리 스택에서 앞, 뒤 페이지로 이동
        this.$router.go(0)
      })
      .catch(err => console.log(err))
    },
  }
}
</script>

<style scoped>
div {
  margin-left: 30px;
  text-align: start;
}
</style>