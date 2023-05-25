<template>
  <div>  
    <div class="sign-up-container">
      <div class="sign-up-box">

        <h1 class="m-5">회원가입</h1>
        <form @submit.prevent="signUp" class="sign-up-items">
          <!-- 사용자 이름 -->
          <div>      
            <label for="username" class="mb-2">아이디</label> <br>
            <input placeholder="아이디를 입력해주세요" class="input-form mb-3" ype="text" id="username" v-model="username"><br>
          </div>
          <!-- 비밀번호 -->
          <div>
            <label for="password1" class="mb-2">비밀번호</label><br>
            <input placeholder="비밀번호를 입력해주세요" class="input-form mb-3" type="password" id="password" v-model="password"><br>
          </div>
          <!-- 비밀번호 검증 -->
          <div>
            <label for="password2" class="mb-2">비밀번호 확인</label><br>
            <input placeholder="비밀번호를 확인해주세요" class="input-form mb-3" type="password" id="password2" v-model="password2"><br>
          </div>
          <!-- 닉네임 -->
          <div>
            <label for="nickname" class="mb-2">이름</label><br>
            <input placeholder="이름을 입력해주세요" class="input-form mb-3" type="text" id="nickname" v-model="nickname"><br>
          </div>
          <!-- 자기소개글 -->
          <div>
            <label for="introduce" class="mb-2">소개</label><br>
            <textarea placeholder="당신을 소개해주세요" class="input-text-form mb-3" type="text" id="introduce" v-model="introduce"></textarea><br>
          
          </div>

          <div class="submit-button">
            <input type="submit" value="회원가입">
          </div>
        </form>
      </div>
   </div>
   
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
  height: 720px;
}

.sign-up-items {
  text-align: center;
}

.input-form{
  width: 70%;
  height: 30px;
}

.input-text-form{
  width: 70%;
  height: 100px;
  resize: none;
}

.submit-button{
  margin-top: 30px;
  text-align: center;
}

</style>