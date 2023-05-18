<template>
  <div>
    <input type="text" placeholder="댓글을 입력하세요" v-model="content">
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
    createComment() {
      const content = this.content

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/${this.articleId}/comments_article/`,
        data: { content },
      })
      .then(() => {
        this.$router.go(0)
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style>

</style>