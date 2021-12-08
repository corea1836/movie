<template>
  <div id ="main">
    <div class ="bor">
      <input 
      type="text" 
      id="username"
      @change="chkID"
      v-model="credentials.username"
      autofocus
      placeholder="아이디">
      
    </div>
    <p v-if="iderror" style="color:red;">같은 아이디가 존재합니다.</p>
    <p v-if="idsuccess" style="color:green;">사용가능합니다.</p>
    <div class ="bor">
      <input
      type="password"
      id="password"
      v-model="credentials.password"
      placeholder="비밀번호">
    </div>
    <div class ="bor">
      <input 
      type="password" 
      id="passwordConfirmation"
      v-model="credentials.passwordConfirmation"
      @change="chkPw"
      @keyup.enter="signup"
      placeholder="비밀번호 확인">
    </div>
    <p v-if="pwerror" style="color:red;">비밀번호를 확인해주세요</p>
    <div class ="bor">
      <input 
      type="text" 
      id="email"
      v-model="credentials.email"
      placeholder="이메일">
    </div>
    <div class ="bor">
      <input 
      type="text" 
      id="nickname"
      v-model="credentials.nickname"
      placeholder="닉네임">
    </div>
    <div class ="bor">
      <input 
      type="text" 
      id="address"
      v-model="credentials.address"
      placeholder="주소">
    </div>
    <div class ="bor">
      <input 
      type="text" 
      id="phone"
      v-model="credentials.phone"
      placeholder="전화번호">
    </div>
    <div class="chkboxdiv">
      <div v-for="genre in genres" :key="`${genre.id}`">
        <input class ="chkinput" type="checkbox"
        v-model="credentials.genres"
        :id ="`${genre.id}`" :value="`${genre.id}`">
        <label class ="cp chklabel" :for="`${genre.id}`">{{ genre.genre_name }}</label>
      </div>
    </div>
    <div class="btnbor" @click="signup">회원가입</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Singup',
  data: function () {
    return {
      credentials: {
        username : null,
        password : null,
        passwordConfirmation : null,
        email : null,
        nickname : null,
        address : null,
        phone : null,
        genres : [],
      },
      pwerror:false,
      iderror:false,
      idsuccess: false,
      genres :null,
    }
  },
  methods: {
    chkPw: function(){
      if (this.credentials.password != this.credentials.passwordConfirmation){
        console.log("비밀 번호를 확인해주세요");
        this.pwerror = true
      } else{
        this.pwerror = false
      }
    },
    chkID: function(){
      axios({
        method: "post",
        url: 'http://127.0.0.1:8000/accounts/chkID/',
        data: {
          username : this.credentials.username
        },
      })
        .then((res) =>{
          console.log(res.data.results);
          this.iderror=false
          this.idsuccess=true
        })
        .catch ((err) => {
          console.log(err);
          this.iderror=true
          this.idsuccess=false
        })
    },
    signup: function () {
      if (this.credentials.genres.length > 3){
        alert("장르는 최대 3개까지만 선택해주세요")
      } else{
        axios({
        method: "post",
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
        })
        .then(() =>{
          this.$router.push({ name: 'Login' })
        })
        .catch (err => {
          console.log(err)
        })
      }
      
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
  },
  created: function(){
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
  }
  .bor {
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