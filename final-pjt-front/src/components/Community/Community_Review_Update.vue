<template>
  <div id ="main">
    <h1 class="cd goc">정보수정</h1>
    <div>
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
        v-model.trim="review.rank" id="rank" @keyup.enter="updateReview">
      </div>
    </div>
    <button class="cp btu btnbor" @click="updateReview">수정</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Community_Review_Update',
  data: function () {
    return {
      review : null
    }
  },
  props:{
    id: Number,
  },
  methods: {
    setToken: function(){
      const token = localStorage.getItem('jwt')
      const config ={
        Authorization: `JWT ${token}`
      }
      return config
    },
    updateReview: function() {
      if(this.review.title) {
        axios({
          method: "put",
          url : `http://127.0.0.1:8000/reviews/${ this.id }/`,
          data : this.review,
          headers: this.setToken(),
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
    getReview: function(){
      axios({
        method : "get",
        url: `http://127.0.0.1:8000/reviews/${ this.id }/`,
        headers: this.setToken(),
      })
      .then( res => {
        console.log(res.data)
        this.review = res.data
      })
      .catch(err =>{
        console.log(err)
      })
    },
  },
  created: function(){
    if (this.id){
      this.getReview()
    } else{
      this.$router.push({ name:"Community" })
    }
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
  height: 800px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border:1px solid gray;
  border-radius: 10px;
  min-height: 850px;
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
  color: goldenrod;
  border: 1px solid goldenrod;
  border-radius: 10px;
  background-color: black;
}
.bor input {
  border:0 solid goldenrod;
  outline:none;
  height:auto;
  width: 400px;
  font-size:23px;
  color: goldenrod;
  background-color: black;
}
.bor textarea {
  border:0 solid goldenrod;
  outline:none;
  height:auto;
  color: goldenrod;
  background-color: black;
  width: 400px;
  font-size:20px;
  resize:none
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