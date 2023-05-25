<template>
  <div>
    <!-- 현재 접속자 -->
    <!-- <p v-if="currentUser">hello, {{ currentUser.username }}</p>  -->
    <div v-if="username">
        <div class="profile-top-bar">
            <h1>@{{ username }}</h1>
            <button v-if="username != currentUser.username " @click="follow" :class="{buttonColor: !isFollowing}">
                {{ isFollowing? '언팔로우':'팔로우'}}
            </button>
        </div>

        <div class="count-bar">
            <div>
                <p>플레이리스트</p>
                <p>{{ userArticles.length }}</p>
            </div>
            <div>
                <p>팔로워</p>
                {{ followerCount }}
            </div>
            <div>
                <p>팔로잉</p>
                {{ followingCount }}
            </div>
        </div>
        <!-- 자기 소개 파트 -->
        <div class="introduce-bar my-3">
            <p style="font-weight: bold;">{{ nickname }}</p>
            <p>{{ introduce }}</p>
        </div>


        
        <h3>  <span style="font-weight:bold;">{{ nickname }}</span>의 플레이리스트</h3>
        <hr>
        <!-- 작성한 플레이리스트의 id (article.id)를 가져와서 v-for 활용하자 -->
        <!-- 해당 프로필 유저의 작성게시글 출력 -->
        <ReviewListItem 
        class="profileReviewListItem"
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

.count-bar {
    display: flex;
    background-color: rgb(228, 228, 228);
    justify-content: space-evenly;
    border-radius: 10px;
}

.count-bar div {
    padding: 5px;
    width: 150px;
    text-align: center;
    vertical-align: middle;
}

.count-bar div p {
    margin: 0;
    padding : 3px;
}

.profile-top-bar {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}
.profile-top-bar button{ 
    margin-left: 30px;
    display: flex;
    text-align: center;
    align-items: center;
    justify-content: center;
    height: 30px;
    width : 100px;
    padding:5px;
    border-radius: 5px;
    border: 0.5px solid black;
}
.profile-top-bar h1{
    margin: 0;
}

.buttonColor {
    background-color: rgba(49, 75, 221, 0.747);
    color: white;
}

.profileReviewListItem{
    padding: 10px;
    margin-bottom: 10px;
    background-color: rgb(238, 238, 238, 0.3);
    border: 1px solid rgb(238, 238, 238);
    border-radius: 10px;
    
}
</style>