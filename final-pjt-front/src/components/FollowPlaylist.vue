<template>
  <div>
    <h2>팔로우 플레이리스트</h2>
    <hr>
    <div v-for="article in followingArticles" :key="article.id">
        {{ getAuthor(article.user) }}
        <ReviewListItem :article="article"/>
        <hr>
    </div>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'FollowPlaylist',
    data(){
        return {
            Articles : this.$store.state.articles,
            currentUser : this.$store.state.currentUser,
            followingArticles : [],
            author: null,
        }
    },
    components:{
        ReviewListItem,
    },
    created(){
        this.getUser()
        this.getArticles()
    },
    methods:{
        getUser(){
            this.$store.dispatch('getCurrentUser')
        },
        getArticles(){
            for (const article of this.Articles) {
                if (this.currentUser.followings.includes(article.user)) {
                    this.followingArticles.push(article)
                }
            }
        },
        // userId로 user의 정보를 가져오기
        getUserDetail(userId){
            axios({
                method: 'get',
                url: `${API_URL}/accounts/user/detail/${userId}/`
            })
            .then((res)=>{
                this.author = res.data.username
            })
            .catch(err=>console.log(err))
        },
        getAuthor(userId) {
            let currentAuthor = ''
            this.getUserDetail(userId)
            currentAuthor = this.author
            return currentAuthor
        }
    }
}

</script>

<style>

</style>