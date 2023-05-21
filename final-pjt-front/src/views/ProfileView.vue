<template>
  <div>
    <!-- <h1 v-if="userData">{{ userData.username }}의 Profile Page</h1> -->
    <h1>Profile Page</h1>
    <p v-if="userData">Username : {{ userData.username }}</p>
    <p>Nickname : {{ user.nickname }}</p>
    <p>Follower Count : {{ followerCount }}</p>
    <p>Following Count : {{ followingCount }}</p>
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
            userData: null,
            paramsData: null,
        }
    },
    created(){
        this.paramsData = JSON.parse(this.$route.query.data)
        console.log(this.paramsData)
        this.getUserDetail()

        this.fetchProfileData()

        
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
                this.userData = res.data
                console.log(this.userData)
            })
            .catch(err => console.log(err))
        }
    }
}
</script>

<style>

</style>