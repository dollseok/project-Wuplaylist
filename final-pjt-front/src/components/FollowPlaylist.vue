<template>
  <div>
    <h2>팔로우 플레이리스트</h2>
    <hr>
    <ReviewListItem
    v-for="article in followingArticles" :key="article.id"
    :article="article"
    />
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'

export default {
    name: 'FollowPlaylist',
    data(){
        return {
            Articles : this.$store.state.articles,
            currentUser : this.$store.state.currentUser,
            followingArticles : []
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
        }
    }
}

</script>

<style>

</style>