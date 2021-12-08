<template>
  <div id="main">
    <h1 class="cd goc">글쓰기</h1>
    <hr>
    <div>
      <label class="cd goc">작성자</label>
      <h3>{{ username }}</h3>
      <hr> 
      <label class="cd goc">제목</label>
      <div class="bor">
        <input 
        type="text" 
        v-model.trim="review.title" id="title">
      </div>
    </div>
    <div>
      <label class="cd goc">내용</label>
      <div class="bor">
        <textarea
        v-model.trim="review.content" id="content">
        </textarea>
      </div>
    </div>
    <div>
      <label class="cd goc">별점</label>
      <div class="bor">
        <input 
        type="text" 
        v-model.trim="review.rank" id="rank" @keyup.enter="createReview">
      </div>
    </div>
    <button class="btnbor btu cp" @click="createReview">생성</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Community_Review_Create',
  data: function () {
    return {
      username: null,
      review : {movie: {}, user: {}},
      
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getUserName: function() {
      axios({
        method: "get",
        url:`http://127.0.0.1:8000/accounts/profile/`,
        headers: this.setToken()
      })
        .then((res)=>{
          console.log(res.data.username)
          this.username = res.data.username
          //console.log(userid)
          this.getMovieId()
        })
        .catch((err)=>{
          console.log(err);
        })
    },    
    createReview: function() {
      if(this.review.title) {
        console.log(this.review)
        axios({
          method: "post",
          url : `http://127.0.0.1:8000/reviews/`,
          data : this.review,
        })
          .then(res => {
            console.log(res)
            this.$router.push({ name:"Community" })
          })
          .catch(err =>{
            console.log(err)
          })
      }
    },
   getMovieId: function() {
      console.log(this.$route.params.movie.id)
      console.log(this.userid)
      this.review.movie.id = this.$route.params.movie.id
      this.review.user.username = this.username
      console.log(this.review)
    }
  },
  created: function() {
    this.getUserName()
  }
}
</script>

<style scoped>
* { 
  margin: 0; 
  padding: 0; 
  box-sizing: border-box;
  }
#main{
  margin-top: 30px;
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
  width: 420px;
  height: auto;
  padding: 10px;
  margin: 10px auto;
  border: 1px solid goldenrod;
  color: goldenrod;
  border-radius: 10px;
  background-color: black;
}
.bor input {
  border:0 solid goldenrod;
  outline:none;
  height:auto;
  color: goldenrod;
  width: 400px;
  font-size:23px;
  background-color: black;
}
.bor textarea {
  border:0 solid goldenrod;
  color: goldenrod;
  outline:none;
  height:auto;
  width: 400px;
  font-size:20px;
  resize:none;
  background-color: black;
}
.btnbor{
  width: 300px;
  height: auto;
  padding: 10px;
  font-size:20px;
  margin: 5px;
  border: 1px solid goldenrod;
  color: goldenrod;
  border-radius: 10px;
}
.btnbor:hover{
  color: bisque;
  background-color: burlywood;
  border-color: bisque;
}
.goc{
  color: goldenrod;
  margin: 7px;
  font-size: 22px;
}
.cp{
  cursor: pointer;
}
.cd{
  cursor: default;
}
.btu{
  background-color: rgba(1, 1, 1, 0);
}
</style>