<template>
  <div>
    <!-- 현재 접속자 -->
    <p>hello, {{ currentUser.username }}</p> 
    <div v-if="username">
        <h1>@{{ username }}</h1>
        <p>팔로워: {{ followerCount }} 팔로잉 : {{ followingCount }}</p>
        <p>별명 : {{ nickname }}</p>
        <p>소개 : {{ introduce }}</p>
        <button v-if="username != currentUser.username " @click="follow">{{ isFollowing? 'Unfollow':'follow'}}</button>
        <h3>{{username}}의 플레이리스트</h3>
        <hr>
        <!-- 작성한 플레이리스트의 id (article.id)를 가져와서 v-for 활용하자 -->
        <!-- 해당 프로필 유저의 작성게시글 출력 -->
        <ReviewListItem 
        v-for="article in userArticles" :key="article.id"
        :article="article"
        />


    </div>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
import router from '@/router'
import axios from 'axios'
const API_URL='http://127.0.0.1:8000'

export default {
    name: 'ProfileView',
    components: {
        ReviewListItem,
    },
    data(){
        return {
            username: null,
            nickname: null,
            introduce: null,
            followerCount: 0,
            followingCount: 0,
            userData: {},
            paramsData: null,

            currentUser : null,
            isFollowing:false, // 팔로우 상태 저장하는 변수
            userArticles: [],   // 프로필 유저의 작성 게시글
            // currentUserArticles: [], // 접속 유저의 작성 게시글
        }
    },
    computed: {
        isLogin() {
            return this.$store.getters.isLogin
        }
    },
    created() {
        // this.getCurrentUserArticles() // 접속 유저의 작성게시글 불러오기
    },
    mounted(){
        if (this.isLogin) {
            this.getCurrentUser()   
            this.paramsData = JSON.parse(this.$route.query.data) // 게시글에서 작성자 UserId를 받아오고
            if (this.paramsData.username) { // username으로 받아오는 경우 
                this.fetchProfileData(this.paramsData.username)
            } else { // userId로 받아오는 경우 ( 게시글이나 댓글을 통해 )
                this.getUserDetail()    // 작성자의 프로필 정보 가져오기
            }          
        } else {
            alert('로그인이 필요한 서비스입니다')
            this.$router.push({ name: 'LogInView '})
        }
        
    },
    methods:{
        // username을 이용해 프로필 유저의 데이터를 가져오기
        fetchProfileData(username){
            axios({
                method: 'get',
                url: `${API_URL}/accounts/user/profile/${username}/`,
                headers: {
                    Authorization: `Token ${ this.$store.state.token }`
                }
            })
            .then((response) => {
                this.user = response.data
                this.userArticles = response.data.article_set
                this.username = response.data.username
                this.nickname = response.data.nickname
                this.introduce = response.data.introduce
                this.followerCount = response.data.followers.length
                this.followingCount = response.data.followings.length

                const loggedInUserId = this.currentUser.id // 현재 로그인된 유저의 아이디
                const followersList = response.data.followers
                this.isFollowing = this.checkIdExists(followersList, loggedInUserId)
            })
            .catch((err)=>{
                console.log(err)
            })
        },
        // 현재 유저의 데이터
        // 현재 유저가 프로필 유저를 팔로우했는지 확인하기 위해 필요!
        getCurrentUser(){
            axios({
                method: 'get',
                url:`${API_URL}/accounts/user/current/`,
                headers:{
                    Authorization: `Token ${this.$store.state.token}`
                }
            })
            .then((res) => {
                this.currentUser = res.data
                console.log(res.data)
            })
            .catch(err => console.log(err))
        },
        // 접속유저가 프로필유저를 팔로우했는지 확인
        checkIdExists(data, id){
            if (data.indexOf(id) != -1) {
                return true
            } else { 
                return false
            }

        },
        // 유저아이디로 유저네임 가져오기
        getUserDetail() {
            axios({
                method: 'get',
                url: `${API_URL}/accounts/user/detail/${this.paramsData.userId}/`
            })
            .then((res) => {
                this.userData = res.data
                const username = this.userData.username
                this.fetchProfileData(username)
            })
            .catch(err => console.log(err))
        },
        // 팔로우 기능
        follow(){
            const username = this.userData.username
            axios({
                method: 'post',
                url: `${API_URL}/accounts/user/profile/${username}/follow/`,
                headers: {
                    Authorization: `Token ${ this.$store.state.token }`
                }
            })
            .then(() => {
                router.go(0)
                this.isFollowing = !this.isFollowing

            })
            .catch((err) => console.log(err))
        }
    }
}
</script>

<style>

</style>