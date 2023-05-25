<template>
  <div class="sign-up-container">
    <div class="sign-up-box">
      <h1 class="m-5">로그인</h1>
      <form @submit.prevent="login" class="sign-up-items">
        <label for="username" class="mb-2">아이디</label> <br>
        <input type="text" id="username" class="input-form mb-3" v-model="username"><br>

        <label for="password" class="mb-2"> 비밀번호 </label> <br>
        <input type="password" id="password" class="input-form mb-3" v-model="password"><br>

        <input type="submit" value="로그인" class="submit-button">
      </form>
      <h1>WELCOME TO 우:플리</h1>
      <h5 class="m-4">우리들의 영화 이야기</h5>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)
    }
  }
}
</script>

<style scoped>
  
.sign-up-container{
  position: relative;
  top: 5vh;
  display: flex;
  justify-content: center;
}

.sign-up-box{
  text-align: center;
  background-color:  rgb(228, 228, 228);
  border: 1px solid rgba(34, 194, 119, 0.8);
  width: 600px;
  height: 560px;
}

.sign-up-items {
  text-align: center;
  margin-bottom: 50px;
}

.input-form{
  width:70%;
  height:30px;
}

.submit-button{
  margin-top: 30px;
  text-align: center;
}

</style>