<template>
  <div>
    <div id ="mainin">
      <div class="imgdiv">
        <img class="imgimg" :src="`https://image.tmdb.org/t/p/w500${ review.movie.poster_url }`" alt="포스터">
      </div>
      <div class="content">
        <div class="cd">『{{ review.content }}』</div>
        <div class="star-ratings">
          <div 
            class="star-ratings-fill"
            :style="{ width: `${review.rank * 20}` + '%' }"
          >
            <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
          </div>
          <div class="star-ratings-base">
            <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
          </div>
        </div>
        <div v-if="plusbutton">
          <div class="btnbor" @click ="updateReview">수정</div>
          <div class="btnbor" @click ="deleteReview">삭제</div>
        </div>
      </div>
    </div>
    <div class ="comments">
      <div v-if="usedbtn" class="bor">
        <label for="commenttxt"><input type="text" class="bla" id="commenttxt" v-model="commenttxt"></label>
      </div>
      <div v-if="usedbtn" class="btnbor" @click="comment_create">댓글 생성</div>
      <div v-for="comment in review.comments" class="com cd" :key=comment.id >
        <review-comment :comment="comment"
        @refresh="getReview"></review-comment>  
        </div>
      </div>
  </div>
</template>

<script>
import axios from "axios"
import Review_Comment from './Review_Comment.vue'

export default {
  name: 'Community_Detail',
  data : function(){
    return {
      commenttxt:null,
      plusbutton: false,
      usedbtn:true,
    }
  },
  components:{
    "review-comment": Review_Comment,
  },
  props: {
      review:Object
  },
  methods:{
    checktoken: function(){
      if (!localStorage.get("jwt")){
        this.usedbtn = false
      }
    },
    setToken: function(){
      const token = localStorage.getItem('jwt')
      const config ={
        Authorization: `JWT ${token}`
      }
      return config
    },
    getReview: function(){
      axios({
        method : "get",
        url: `http://127.0.0.1:8000/reviews/${ this.review.id }/`,
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
    updateReview: function(){
      this.$router.push({ name:"Community_Review_Update", params:{id:this.review.id} })
    },
    deleteReview: function(){
      axios({
        method: "delete",
        url : `http://127.0.0.1:8000/reviews/${ this.review.id }/`,
        headers: this.setToken(),
      })
        .then(res => {
          console.log(res)
          this.$emit("del-review")
        })
        .catch(err =>{
          console.log(err)
        })
    },
    comment_create: function(){
      const comment_data ={
        content: this.commenttxt,
        user_name: localStorage.getItem("user_id")
        
      }
      axios({
        method: "post",
        url : `http://127.0.0.1:8000/reviews/${ this.review.id }/comments/`,
        data : comment_data,
        headers: this.setToken(),
      })
        .then(res => {
          console.log(res)
          this.commenttxt =null
          this.getReview()
        })
        .catch(err =>{
          console.log(err)
        })
    },
    name_check: function(){
      let uname = localStorage.getItem("user_id")
      console.log(uname);
      this.plusbutton = this.review.user.username == uname
    },
  },
  created: function() {
    this.name_check()
    this.checktoken()
  }
}
</script>

<style scoped>
#mainin{
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  justify-content: space-around;
}
.comments {
  display: inline-block;
}
.imgdiv {
  width: 200px;
  height : 300px;
  position: relative;
  overflow: hidden;
}
.imgimg{
  width: 100%;
}
.star-ratings {
  cursor: Default;
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  margin: auto;
  margin-bottom: 7px;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: #2b2a29;
}
.content>div{
  margin-bottom: 18px;
  font-size: 25px;
}
#commenttxt{
  background-color: black;
  color: goldenrod;
}
.star-ratings-fill {
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: gold;
}
.star-ratings-base {
  z-index: 0;
  padding: 0;
}
.bor {
  display: inline-block;
  padding: 10px;
  margin: 8px;
  border: 1px solid goldenrod;
  border-radius: 10px;
  background-color: black;
}
.cd {
  cursor: Default;
}
.bor input {
  color: aliceblue;
  border:0 solid white;
  background-color: black;
  outline:none;
  height:22px;
  width: 280px;
  font-size:18px;
}
.com {
  margin-top: 4px;
  margin-bottom: 4px;
}
.btnbor{
  display: inline-block;
  margin: 5px;
  padding: 7px;
  font-size:15px;
  color : goldenrod;
  border: 1px solid goldenrod;
  border-radius: 10px;
  cursor:pointer;
}
.btnbor:hover{
  color: bisque;
  background-color: burlywood;
  border-color: bisque;
}

</style>