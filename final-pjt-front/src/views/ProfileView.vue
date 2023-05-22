<template>
  <div>
    <!-- <h1 v-if="userData">{{ userData.username }}의 Profile Page</h1> -->
    <h1>Profile Page</h1>
    <p v-if="userData">Username : {{ userData.username }}</p>
    <p>Nickname : {{ userData.nickname }}</p>
    <p>Follower Count : {{ followerCount }}</p>
    <p>Following Count : {{ followingCount }}</p>
    <button @click="follow">{{ isFollowing? 'Unfollow':'follow'}}</button>
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
            followerCount: 0,
            followingCount: 0,
            userData: {},
            paramsData: null,

            currentUser : null,
            isFollowing:false, // 팔로우 상태 저장하는 변수
        }
    },
    created(){
        this.paramsData = JSON.parse(this.$route.query.data)
        this.getUserDetail()
        this.getCurrentUser()    
    },
    methods:{
        fetchProfileData(){
            const username = this.userData.username
            axios({
                method: 'get',
                url: `${API_URL}/accounts/user/profile/${username}/`
            })
            .then((response) => {
                this.user = response.data
                console.log(this.user)
                this.followerCount = response.data.followers.length
                this.followingCount = response.data.followings.length

                const loggedInUserId = this.currentUser.id // 현재 로그인된 유저의 아이디
                const followersList = response.data.followers
                this.isFollowing = this.checkIdExists(followersList, loggedInUserId)
                console.log(this.isFollowing)
            })
            .catch((err)=>{
                console.log(err)
            })
        },
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
                // console.log(res.data)
                this.userData = res.data
                this.fetchProfileData()
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