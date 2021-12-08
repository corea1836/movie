<template>
  <div id="main">
    
    <div class="bor"><input type="text" id="username" v-model ="Logindata.username" autofocus placeholder="아이디"></div>
    
    <div class="bor"><input type="password" id="password" @keyup.enter="login" v-model ="Logindata.password" placeholder="비밀번호"></div>
    <div class="btnbor" @click="login">로그인</div>
    <div class="btnbor" @click="movesignup">회원가입</div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name : "Login",
  data: function (){
    return {
      Logindata:{
        username : null,
        password : null,
      }
    }
  },
  methods:{
    login: function(){
      axios({
        method:'post',
        url : 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data : this.Logindata,
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          localStorage.setItem('user_id', this.Logindata.username)
          this.$emit('login')
          this.$router.push({ name: "Movie" })
        })
        .catch(err => {
          console.log(err)
        })
    },
    movesignup: function(){
      this.$router.push({ name: "Signup" })
    }
  }
}
</script>

<style scoped>
* { margin: 0; padding: 0; }
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
  cursor:pointer;
  width: 300px;
  height: auto;
  padding: 10px;
  font-size:20px;
  margin: 5px;
  border: 1px solid goldenrod;
  border-radius: 10px;
  color: goldenrod;
}
.btnbor:hover{
  color: bisque;
  background-color: burlywood;
  border-color: bisque;
}
</style>