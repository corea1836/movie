<template>
  <div id="main">
    <div>
      <h1 class="cd">{{profile.username}}님의 프로필 </h1>
    </div>
    <div>
      <label class="cd">이메일: </label>
      <div class="bor">
        <input 
        type="text" 
        v-model="profile.email">
      </div>
    </div>
    <div>
      <label class="cd">닉네임: </label>
      <div class="bor">
        <input 
        type="text" 
        v-model="profile.nickname">
      </div>
    </div>
    <div>
      <label class="cd">주소: </label>
      <div class="bor">
        <input 
        type="text" 
        v-model="profile.address">
      </div>
    </div>
    <div>
      <label class="cd">전화번호: </label>
      <div class="bor">
        <input 
        type="text" 
        v-model="profile.phone">
      </div>
    </div>
    <div class="chkboxdiv">
      <div v-for="genre in genres" :key="`${genre.id}`">
        <input class ="chkinput" type="checkbox"
        v-model="profile.genres"
        :id ="`${genre.id}`" :value="`${genre.id}`">
        <label class ="cp chklabel" :for="`${genre.id}`">{{ genre.genre_name }}</label>
      </div>
    </div>
    <div class="btnbor" @click="profile_Update">회원정보수정</div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name : "Profile",
  data: function() {
    return{
      profile : null,
      genres: null,
    }
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getProfile: function() {
      axios({
        method: "get",
        url:`http://127.0.0.1:8000/accounts/profile/`,
        headers: this.setToken()
      })
        .then((res)=>{
          console.log(res)
          this.profile =res.data
        })
        .catch((err)=>{
          console.log(err);
        })
    },
    getGenre: function() {
      axios({
        method: 'get',
        url: "http://127.0.0.1:8000/movies/genres",
      })
        .then( res => {
          console.log("getGenre")
          this.genres = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    profile_Update: function () {
      if (this.profile.genres.length > 3){
        alert("장르는 3개까지 선택해주세요")
      } else{
        axios({
          method:"put",
          url:`http://127.0.0.1:8000/accounts/profile/`,
          data: this.profile,
          headers: this.setToken()
        })
        .then((res) =>{
          console.log(res)
          alert("수정되었습니다.")
          this.getProfile()
        })
        .catch((err) =>{
          alert("정보를 확인해주세요")
          console.log(err)
        })
      }
    }
  },
  created: function() {
    this.getProfile()
    this.getGenre()
  }
}
</script>

<style scoped>
  #main{
  height: 800px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border:1px solid gray;
  border-radius: 10px;
  }
  #main>div{
    display: inline-block;
    text-align: center;
    margin: 7px;
  }
  .bor {
    display: inline-block;
    width: 300px;
    height: auto;
    padding: 10px;
    margin: 8px;
    border: 1px solid black;
    border-radius: 10px;
    background-color: white;
  }
  .bor input {
    border:0 solid black;
    outline:none;
    height:30px;
    width: 280px;
    font-size:23px;
  }
  .btnbor{
    width: 300px;
    height: auto;
    padding: 10px;
    font-size:20px;
    margin: 5px;
    border: 1px solid goldenrod;
    border-radius: 10px;
    color: goldenrod;
    cursor:pointer;
  }
  label, h1{
    color:goldenrod;
  }
  .btnbor:hover{
    color: bisque;
    background-color: burlywood;
    border-color: bisque;
  }
  .chkboxdiv{
    width: 400px;
    margin: 5px;
  }
  .chkboxdiv div{
    display: inline-block;
    margin: 7px;
  }
  .chkinput{
    display: none;
  }
  .chkinput:checked + label{
    background-color: burlywood;
    color: bisque;
  }
  .chklabel{
    padding: 6px;
    border: 1px solid goldenrod;
    color: goldenrod;
    border-radius: 8px;
  }
  .chklabel:hover{
    background-color: bisque;
  }
  .cp{
  cursor: pointer;
  }
  .cd{
    cursor: default;
  }
</style>