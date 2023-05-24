<template>
  <div class="comment-list">
    <h3>댓글 목록</h3>
    <hr>
    <ul>
      <CommentListItem 
      v-for="comment in comments" :key="comment.id"
      :comment="comment"
      />
    </ul>
    <CommentForm 
    :articleId="articleId"
    />
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentForm from '@/components/CommentForm.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentList',
  components: {
    CommentListItem,
    CommentForm
  },
  props: {
    articleId: Number, // 게시글의 id 받아오기
  },
  data() {
    return {
      comments: [] 
    }
  },
  created() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/${this.articleId}/comments_article/`,
    })
    .then((res) => {
      // console.log(res.data)
      this.comments = res.data
      // console.log(this.comments)
    })
    .catch(err => console.log(err))
  }
}
</script>

<style>

</style>