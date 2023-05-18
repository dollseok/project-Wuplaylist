<template>
  <div class="comment-list">
    <h3>댓글 목록</h3>
    {{articleId}}
    <!-- <CommentListItem 
    v-for="comment in commentObj" :key="comment.id"
    /> -->
    <CommentForm />
  </div>
</template>

<script>
// import CommentListItem from '@/components/CommentListItem.vue'
import CommentForm from '@/components/CommentForm.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentList',
  components: {
    // CommentListItem,
    CommentForm
  },
  props: {
    articleId: Number, // 게시글의 id 받아오기
  },
  data() {
    return {
      // commentObj: 
    }
  },
  created() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/comments/`,
    })
    .then((res) => {
      console.log(res.data)
    })
    .catch(err => console.log(err))
  }
}
</script>

<style>

</style>