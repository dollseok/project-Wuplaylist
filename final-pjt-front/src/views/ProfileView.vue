<template>
  <div>
    <h1>Profile Page</h1>
    <div v-if="username">
        <p>Username : {{ username }}</p>
        <p>Nickname : {{ nickname }}</p>
        <p>Follower Count : {{ followerCount }}</p>
        <p>Following Count : {{ followingCount }}</p>
        <button v-if="username != currentUser.username " @click="follow">{{ isFollowing? 'Unfollow':'follow'}}</button>

        {{userData['article_set']}}
    </div>
  </div>
</template>

<script>
import router from '@/router'
import axios from 'axios'
const API_URL='http://127.0.0.1:8000'

export default {
    name: 'ProfileView',
    components: {},
    data(){
        return {
            username: null,
            nickname: null,
            followerCount: 0,
            followingCount: 0,
            userData: {},
            paramsData: null,

            currentUser : null,
            isFollowing:false, // 팔로우 상태 저장하는 변수
        }
    },
    mounted(){
        this.getCurrentUser()   
        this.paramsData = JSON.parse(this.$route.query.data) // 게시글에서 작성자 UserId를 받아오고
        if (this.paramsData.username) { // username으로 받아오는 경우 
            this.fetchProfileData(this.paramsData.username)
        } else { // userId로 받아오는 경우 ( 게시글이나 댓글을 통해 )
            this.getUserDetail()    // 작성자의 프로필 정보 가져오기
        } 
    },
    methods:{
        // 타고 들어간 해당 유저의 데이터
        // username을 이용해 프로필 데이터를 가져오기
        fetchProfileData(username){
            axios({
                method: 'get',
                url: `${API_URL}/accounts/user/profile/${username}/`
            })
            .then((response) => {
                this.user = response.data
                // console.log(this.user)
                this.username = response.data.username
                this.nickname = response.data.nickname
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
        // userId를 활용해 username과 nickname을 받아오기
        // 현재 유저의 데이터
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
        // 팔로워 리스트에 있는지 확인하는 함수
        checkIdExists(data, id){
            if (data.indexOf(id) != -1) {
                return true
            } else { 
                return false
            }

        },

        getUserDetail() {
            axios({
                method: 'get',
                url: `${API_URL}/accounts/user/detail/${this.paramsData.userId}/`
            })
            .then((res) => {
                console.log(res.data)
                this.userData = res.data
                const username = this.userData.username
                this.fetchProfileData(username)
            })
            .catch(err => console.log(err))
        },

        follow(){
            const username = this.userData.username
            axios({
                method: 'post',
                url: `${API_URL}/accounts/user/profile/${username}/follow/`,
                headers: {
                    Authorization: `Token ${ this.$store.state.token }`
                }
            })
            .then((res) => {
                router.go(0)
                this.isFollowing = !this.isFollowing
                console.log(this.isFollowing)
                console.log(res.data)

            })
            .catch((err) => console.log(err))
        }
    }
}
</script>

<style>

</style>