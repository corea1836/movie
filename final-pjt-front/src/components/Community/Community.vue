<template>
  <div id= "main">
    <div class="container">
      <div class="row">
        <div class="cd col col1">제목</div>
        <div class="cd col col2">작성자</div>
        <div class="col col3"> </div>
      </div>
      <div class="row" v-for="(review, index) in reviews" :key = "review.id">
        <div class="cd col col1">{{ review.title }}</div>
        <div class="cd col col2">{{ review.user.username }}</div>
        <div class="cp col col3" @click="showdetail(index)" v-if="btnud[index]">
          <i class="fas fa-chevron-down"></i>
        </div>
        <div class="cp col col3" @click="showdetail(index)" v-if="!btnud[index]">
            <i class="fas fa-chevron-up"></i>
        </div>
        <div class="col4">
          <community-detail :review = "review"  @del-review="getReview()"></community-detail>
        </div>
      </div>
      </div>
    <div class="btncon">
      <div class="btnbor" @click="movepage(pagenum-1, pageindex-1)">이전</div>
      <div v-for="(sel, index) in pageselector" :key="sel" class ="cp pagesel" @click="movepage(sel, index)">{{sel}}</div>
      <div class="btnbor" @click="movepage(pagenum+1, pageindex+1)">다음</div>
      <!-- <button class="btnbor" @click="createReview">글쓰기</button> -->
    </div>
      
  </div>
</template>
<script>
import axios from 'axios'
import Community_Detail from "./Community_Detail.vue"
export default {
  name : "Community",
  data: function(){
    return {
      reviews :null,
      pagenum : 1,
      totalpage: 100,
      btnud:[true, true, true, true, true, true, true, true, true, true],
      pageselector :[".",".",".",".",".",".",".",".",".","."],
      pageindex:0,
      flag:true
    }
  },
  components:{
    "community-detail" :Community_Detail,
  },
  methods:{
    getReview: function(){
      axios({
        method : "get",
        url: "http://127.0.0.1:8000/reviews/page/",
        params:{
          page:this.pagenum
        }
      })
      .then( res => {
        console.log(res.data)
        this.totalpage = res.data.page
        this.reviews = res.data.data
        if (this.flag){
          this.flag = false
          this.showsel()
        }
      })
      .catch(err =>{
        console.log(err)
      })
    },
    movepage: function(cp,  index){
      const arr = document.querySelectorAll(".pagesel")
      if (cp<1){
        alert("첫페이지입니다.")
      } else if (arr[index].innerText == "."){
        alert("끝페이지입니다.")
      } else {
        this.btnud=[true, true, true, true, true, true, true, true, true, true]
        this.pageindex=index
        this.pagenum = cp
        let ss = parseInt(this.pagenum /10)
        for (var i = 1; i<=10; i++){
          if (i-1 == this.pageindex){
            arr[i-1].style.fontSize = "30px";
          }else{
            arr[i-1].style.fontSize = "20px";
          }
          if (i+ss*10>parseInt(this.totalpage /10)+1){
            this.$set(this.pageselector, i-1, ".");
          } else{
            this.$set(this.pageselector, i-1, i+ss*10);
          }  
        }
        this.getReview()
      }
    },
    createReview: function(){
      this.$router.push({name:"Community_Review_Create"})
    },
    showdetail: function(idx){
      const mm = document.querySelectorAll(".col4")[idx]
      if (mm.style.height == '0px'|| mm.style.height == 0){
        mm.style.height = "auto"
        this.$set(this.btnud, idx, !this.btnud[idx]);
      } else {
        mm.style.height = 0
        this.$set(this.btnud, idx, !this.btnud[idx]);
      }
      this.getReview()
    },
    showsel: function(){
      for (var i = 1; i<=10; i++){
        if (i>parseInt(this.totalpage/10)+1){
          this.$set(this.pageselector, i-1, ".");
        } else{
          this.$set(this.pageselector, i-1, i);
        }
      }
    }
  },
  created: function() {
    this.getReview()
  },
  
}
</script>

<style scoped>
*{
  box-sizing: border-box;
  margin:0;
  padding:0;
}
#main{
  height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  border:1px solid gray;
  border-radius: 10px;
  color: goldenrod
}
.container{
  width: 80%;
  min-height: 700px;
  margin:20px auto;
}
th, td{
  border-bottom: 1px solid goldenrod;
  padding: 15px;
}
.row{
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}
.col{
  display: inline-block;
  height: 50px;
  padding: 15px;
  border-bottom: 1px solid goldenrod;
}
.col1{
  width: 65%;
}
.col2{
  width: 25%;
}
.col3{
  width: 10%;
}
.col4{
  width: 100%;
  height: 0px;
  overflow: hidden;
  border-bottom: 1px solid goldenrod;
}
.bor {
  width: 300px;
  height: 30px;
  padding: 10px;
  margin: 8px;
  border: 1px solid goldenrod;
  border-radius: 10px;
  color: goldenrod;
}
.bor input {
  border:0 solid goldenrod;
  outline:none;
  height:30px;
  width: 280px;
  font-size:23px;
}
.btnbor{
  display: inline-block;
  margin: px;
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
.pagesel{
  font-size: 20px;
  margin:5px;
  width: 10px;
  display: inline-block;
}
.cd {
  cursor: Default;
}
.cp {
  cursor: pointer;
}
.btncon{
  bottom: 20px;
  margin: 20px;
}

</style>