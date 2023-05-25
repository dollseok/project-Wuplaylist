<template>
  <div>
    <h2>팔로우 플레이리스트</h2>
    <hr>
    <div v-if="token">
        <div v-for="article in followingArticles" :key="article.id">
            {{ getAuthor(article.user) }}
            <ReviewListItem :article="article"/>
            {{ getElapsedTime(article.created_at) }}
            <hr>
        </div>
    </div>
    <div v-else>
        <p>로그인이 필요합니다</p>
        <button @click="goLogin">로그인 하러 가기</button>
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
            token: this.$store.state.token
        }
    },
    components:{
        ReviewListItem,
    },
    mounted(){
        if (this.token) {
            this.getUser()
        }
        this.getArticles()
    },
    methods:{
        getUser(){
            this.$store.dispatch('getCurrentUser')
        },
        getArticles(){
            // 팔로잉한 사람의 게시글을 최근 게시글부터 탐색
            for (const article of this.Articles.reverse()) {
                if (this.currentUser.followings.includes(article.user)) {
                    this.followingArticles.push(article)
                }
            }
        },
        // userId로 user의 정보를 가져오기
        getUserDetail(userId){
            axios({
                method: 'get',
                url: `${API_URL}/accounts/user/detail/${userId}/`,
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
        },
        // 경과시간 구하는 함수
        getElapsedTime(created) {
            const start = new Date(created) // 작성 시각
            const end = new Date()          // 현재 시각
            
            const diff = (end - start) / 1000 // 경과 시간 (밀리초 빼주기)

            const times = [
                { name: '년', milliSeconds: 60 * 60 * 24 * 30 * 365 },
                { name: '개월', milliSeconds: 60 * 60 * 24 * 30 },
                { name: '일', milliSeconds: 60 * 60 * 24 },
                { name: '시간', milliSeconds: 60 * 60 },
                { name: '분', milliSeconds: 60 },
            ]

            for (const value of times) {
                const betweenTime = Math.floor(diff / value.milliSeconds)
                // 큰 단위는 1보다 작은 소수점 값이 나옴
                if (betweenTime >= 1) {
                    return `${betweenTime}${value.name} 전`
                }
            }
            // 모든 단위가 맞지 않을 시 
            return "방금 전"
        },
        goLogin() {
            this.$router.push({ name: 'LoginView' })
        }
    }
}

</script>

<style>

</style>