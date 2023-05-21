<template>
  <div>
    <h1 v-if="userData">{{ userData.username }}의 Profile Page</h1>
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
            userData: null,
            paramsData: null
        }
    },
    created(){
        this.paramsData = JSON.parse(this.$route.query.data)
        console.log(this.paramsData)
        this.getUserDetail()
    },
    methods: {
        getUserDetail() {
            axios({
                method: 'get',
                url: `${API_URL}/accounts/user/detail/${this.paramsData.userId}/`
            })
            .then((res) => {
                console.log('데이터 잘 들어오쥬?')
                this.userData = res.data
            })
            .catch((err)=>{
                console.log(err)
            })
        }
    }

}
</script>

<style>

</style>