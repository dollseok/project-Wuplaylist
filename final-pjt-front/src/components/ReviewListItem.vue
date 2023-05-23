<template>
  <div class="each-review">
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <router-link
      :to="{name:'detail', params:{id: String(article.id)}, query: { 
          articleTitle: articleTitle,
          articleContent: articleContent
         } }"
    >
    [DETAIL]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ReviewListItem',
  components: {
    
  },
  props: {
    article: Object,
  },
  data() {
    return {
      articleTitle: this.article.title,
      articleContent: this.article.content
    }
  }
}
</script>

<style>

</style>