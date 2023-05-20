<template>
  <div>
    <h1>Profile Page</h1>

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

        }
    },
    created(){
        axios({
            method: 'get',
            url: `${API_URL}/accounts/profile/`
        })
        .then((res) => {
            console.log(res)
        })
        .catch((err)=>{
            console.log(err)
        })
    }

}
</script>

<style>

</style>