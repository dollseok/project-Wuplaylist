<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <!-- 사용자 이름 -->
      <label for="username">아이디 : </label>
      <input type="text" id="username" v-model="username"><br>
      <!-- 비밀번호 -->
      <label for="password1">비밀번호 : </label>
      <input type="password" id="password" v-model="password"><br>
      <!-- 비밀번호 검증 -->
      <label for="password2">비밀번호 확인: </label>
      <input type="password" id="password2" v-model="password2"><br>
      <!-- 닉네임 -->
      <label for="nickname">별명 : </label>
      <input type="text" id="nickname" v-model="nickname"><br>
      <!-- 자기소개글 -->
      <label for="introduce">소개 : </label>
      <input type="text" id="introduce" v-model="introduce"><br>

      <input type="submit" value="회원가입">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignupForm',
  data() {
    return {
      username: null,
      password: null,
      password2: null,
      nickname: null,
      introduce: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password = this.password
      const password2 = this.password2
      const nickname = this.nickname
      const introduce = this.introduce

      const payload = {
        username, password, password2, nickname, introduce,
      }

      this.$store.dispatch('signUp', payload)
    }
  }
}

</script>

<style>

</style>