<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <!-- 사용자 이름 -->
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>
      <!-- 비밀번호 -->
      <label for="password1">password : </label>
      <input type="password" id="password" v-model="password"><br>
      <!-- 비밀번호 검증 -->
      <label for="password2">password confirmation: </label>
      <input type="password" id="password2" v-model="password2"><br>
      <!-- 닉네임 -->
      <label for="nickname">nickname : </label>
      <input type="text" id="nickname" v-model="nickname"><br>

      <input type="submit" value="SignUp">
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
      nickname:null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password = this.password
      const password2 = this.password2
      const nickname = this.nickname

      const payload = {
        username, password, password2, nickname,
      }

      this.$store.dispatch('signUp', payload)
    }
  }
}

</script>

<style>

</style>