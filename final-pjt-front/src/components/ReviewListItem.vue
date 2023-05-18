<template>
  <div class="each-review">
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
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
  }
}
</script>

<style>

</style>