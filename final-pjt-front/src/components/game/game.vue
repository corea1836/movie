<template>
  <div id ="main">
    <h1 class="cd txt Qtext">{{ qtxt }}</h1>
    <h3 class="cd txt count">{{ count }}점</h3>
    <div class="group">
      <div>
        <img class="poster" :src="`https://image.tmdb.org/t/p/w500${ twomovies[0].poster_url }`" alt="사진1">
      </div>
      <div class="cp txt Atext lt" @click ="select(2)">{{ atxt }}</div>
    </div>
    <div class="group">
      <div>
        <img class="poster" :src="`https://image.tmdb.org/t/p/w500${ twomovies[1].poster_url }`" alt="사진2">
      </div>
      <div class="cp txt Atext rt" @click ="select(1)">{{ atxt }}</div>
    </div>
    <div class="blackboard"></div>
  </div>
</template>

<script>
import _ from 'lodash'
import axios from "axios"
export default {
  name:"game",
  data:function() {
    return {
      movies:[],
      count:0,
      twomovies:null,
      checkthing:null,
      qtxt: null,
      atxt: null,
    }
  },
  methods: {
    getMovie: function () {
      axios({
        method: 'get',
        url: "http://127.0.0.1:8000/movies/",
      })
      .then( res => {
        console.log(res)
        this.movies = res.data
        this.picktwo()
      })
      .catch(err => {
        console.log(err)
      })
    },
    picktwo: function(){
      this.twomovies=_.sampleSize(this.movies, 2);
      this.checkthing=_.sample([1, 2]);
      if (this.checkthing == 1){
        this.qtxt = "어느쪽 평점이 더 높은가?"
        this.atxt = "이쪽이 더 높다!"
      } else if (this.checkthing == 2){
        this.qtxt = "어느쪽 더 최근에 나왔는가?"
        this.atxt = "이쪽이 더 최근이다!"
      }
    },
    select: function(selnum){
      let chknum = 0
      if (this.checkthing == 1){
        if(this.twomovies[0].rank > this.twomovies[1].rank){
          chknum = 2
        }else {
          chknum = 1
        }
      }else{
        if(this.twomovies[0].release_date > this.twomovies[1].release_date){
          chknum = 2
        }else {
          chknum = 1
        }
      }
      if(selnum == chknum){
        alert("정답입니다!")
        this.count++
      }else{
        alert("오답입니다!")
        this.count = 0
      }
      this.picktwo()
    }
  },
  created:function (){
    this.getMovie()
  }
}
</script>

<style>
*{
  box-sizing: border-box;
  margin:0;
  padding:0;
}
#main{
  display: flex;
  align-items: center;
  position: relative;
  z-index: 10;
  justify-content: center;
}
.txt{
  z-index: 100;
  font-size: 35px;
  position: absolute;
  color: goldenrod;
}
.poster{
  display: inline-block;
  height: 850px;
  text-align: center;
}
.blackboard{
  z-index: 99;
  position: absolute;
  background-color: black;
  width: 100%;
  height: 100%;
  opacity: 0.5;
}
.group{
  position: relative;
  justify-content: center;
}
.Qtext{
  top: 15%;
}
.count{
  right:30px;
  top:30px;
}
.Atext{
  bottom: 15%;
  width: 400px;
  font-size: 30px;
  cursor:pointer;
  left: 50%;
  transform: translate(-50%, 0%);
}
.Atext:hover{
  animation: big 0.3s forwards;
}

@keyframes big {
  from {
    font-size: 30px;
  }
  to {
    font-size: 35px;
  }
}
.cp{
  cursor: pointer;
}
.cd{
  cursor: default;
}
</style>