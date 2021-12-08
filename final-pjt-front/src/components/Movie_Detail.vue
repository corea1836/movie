<template>
  <div>
    <div class="movie-backgournd">
      <div class="img-field mf5">
        <img :src= "`https://image.tmdb.org/t/p/w500${movie.poster_url}`" alt="">
      </div>
      <div>
        <h3 class="text-center mf5">{{ movie.title }}</h3>
        장르 : 
        <p class="genre-field mf5"
          v-for="genre_item in movie.genre"
          :key="genre_item.id">
            {{ genre_item["genre_name"] }}, 
          </p>
        <p class="overview mf5">{{ movie.overview }}</p>
        <p class='mf5'>개봉일 : {{ movie.release_date }}</p>
        <p class='mf5'>평점 : {{ movie.rank }}</p>
        <hr>
        <div class='Rbox'>
           <p class="reviewtag">리뷰</p>
          <div v-for="review in movie.reviews" :key="review.id" class="reviewbox">
            <h2>『 {{ review.title }} 』</h2>
          </div>
            <div class="btnbor" @click="createreview">리뷰쓰기</div>
        </div>
      </div>


    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Movie_Detail',
  data: function() {
    return {
      movie: null,
    }
  },
  props: {
    id: Number
  },
  methods: {
    getMovie: function (){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${ this.id }/`,
      })
      .then ( res => {
        console.log(res.data)
        this.movie = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },
    createreview: function () {
      this.$router.push({name: 'Community_Review_Create', params: { movie: this.movie }})
    }
  },
  mounted: function() {
    this.getMovie()
  }
}
</script>

<style scoped>
  *{
    box-sizing: border-box;
    margin:0;
    padding:0;
  }
  .movie-backgournd {
    margin-top: 50px;
    margin-bottom: 100px;
    display: flex;
    width: 100%;
    text-align: center;
    color: goldenrod;
    position: relative;
  }
  .img-field {
    display: inline-block;
  }
  .overview {
    padding: 20px
  }
  .genre-field {
    display: inline-block;
  }
  .reviewtag {
    margin-top: 20px;
    margin-bottom: 30px; 
    font-size: 30px;
  }
  .mf5 {
    margin-bottom: 5px;
  }
  .reviewbox h2{
    color: goldenrod
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
    display: inline-block;
  }
  .btnbor:hover{
    color: bisque;
    background-color: burlywood;
    border-color: bisque;
  }
  .Rbox {
    margin: auto;
  }
</style>