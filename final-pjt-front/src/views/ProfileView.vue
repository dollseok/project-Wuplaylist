<template>
  <div>
    <!-- <h1 v-if="userData">{{ userData.username }}의 Profile Page</h1> -->
    <h1>Profile Page</h1>
    <p v-if="userData">Username : {{ userData.username }}</p>
    <p>Nickname : {{ userData.nickname }}</p>
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
            followerCount: 0,
            followingCount: 0,
            userData: {},
            paramsData: null,
        }
    },
    created(){
        this.paramsData = JSON.parse(this.$route.query.data)
        this.getUserDetail()
        
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
            })
            .catch((err)=>{
                console.log(err)
            })
        },
        getUserDetail() {
            axios({
                method: 'get',
                url: `${API_URL}/accounts/user/detail/${this.paramsData.userId}/`
            })
            .then((res) => {
                console.log(res.data)
                this.userData = res.data
                this.fetchProfileData()
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