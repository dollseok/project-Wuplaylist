<template>
  <div class="eachComment">
    <li>{{ comment.content }}</li>
  </div>
</template>

<script>

export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
  }
}
</script>

<style>

</style>