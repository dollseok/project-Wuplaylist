<template>
  <div>
    <h1>Article Detail</h1>
    <hr>
    <div v-if="updatestatus">
      <p>글 번호 : {{ article?.id }}</p>
      <p>제목 : {{ article?.title }}</p>
      <p>내용 : {{ article?.content }}</p>
      <p>작성시각 : {{ article?.created_at }}</p>
      <p>수정시각 : {{ article?.updated_at }}</p>
      
      <button @click="updateMode">수정</button>
      <button @click="deleteArticle">삭제</button>
      <button @click="goBack">목록</button>
    </div>
    <!-- 수정버튼을 눌렀을 때 -->
    <div v-else>
      <p>글 번호 : {{ article?.id }}</p>
      <p>제목 : <input type="text" v-model="changedTitle"></p>
      <p>내용 : <input type="text" v-model="changedContent"></p>

      <button @click="updateArticle">저장</button>
      <button @click="updateMode">취소</button>
    </div>
    <hr>
    <CommentList 
    v-if="article"
    :articleId="article.id"
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
  data() {
    return {
      article: null,
      updatestatus: true,
      changedTitle: null,
      changedContent: null
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`
      })
      .then((res) => {
        this.article = res.data
      })
      .catch(err => console.log(err))
    },
    updateMode() {
      this.updatestatus = !this.updatestatus
    },

    updateArticle() {
      const title = this.changedTitle
      const content = this.changedContent

      axios({
        method: 'put',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
        data: { title, content }
      })
      .then(() => {
        this.$router.go(0)
      })
      .catch(err => console.log(err))
    },
    deleteArticle() {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
      })
      .then(() => {
        this.$router.push({ name: 'review' })
      })
    },
    goBack() {
      this.$router.push({ name: 'review'})
    }
  }
}
</script>

<style>

</style>