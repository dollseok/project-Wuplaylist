<template>
  <div>
    <!-- <h1 v-if="userData">{{ userData.username }}의 Profile Page</h1> -->
    <h1>Profile Page</h1>
    <p v-if="userData">Username : {{ username }}</p>
    <p>Nickname : {{ nickname }}</p>
    <p>Follower Count : {{ followerCount }}</p>
    <p>Following Count : {{ followingCount }}</p>
    <button @click="follow">follow</button>
  </div>
</template>

<script>
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
        }
    },
    created(){
        this.paramsData = JSON.parse(this.$route.query.data) // 게시글에서 작성자 UserId를 받아오고
        console.log(this.paramsData)
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
                // console.log(response.data.username)
                this.username = response.data.username
                this.nickname = response.data.nickname
                this.followerCount = response.data.followers.length
                this.followingCount = response.data.followings.length
            })
            .catch((err)=>{
                console.log(err)
            })
        },
        // userId를 활용해 username과 nickname을 받아오기
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
            console.log(username)
            axios({
                method: 'post',
                url: `${API_URL}/accounts/user/profile/${username}/follow/`,
                
                headers: {
                    Authorization: `Token ${ this.$store.state.token }`
                }
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => console.log(err))
        }
    }
}
</script>

<style>

</style>