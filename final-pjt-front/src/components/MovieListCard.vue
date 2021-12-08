<template>
    <router-link :to="`/Movie_Detail/${ movie.id }`">
      <div class="card" @mouseover="isShow=true" @mouseleave="isShow=false">
        <div v-show="isShow" class="summary">
          <div class="summarytitle">
            <h2>{{ movie.title }}</h2>
          </div>
          <div>
            <h3 class="genres"
            v-for="genre_item in movie.genre"
            :key="genre_item.id">
            {{ genre_item["genre_name"] }}, 
            </h3>
          </div>
        </div>
        <img :src= "`https://image.tmdb.org/t/p/w500${movie.poster_url}`" alt="">
      </div>
    </router-link> 
</template>

<script>

export default {
  props: ['movie'],
  data: function () {
    return {
      isShow: false,
    }
  },
}
</script>

<style scoped>
  .card {
    width: 220px;
    height: 420px;
    margin: 10%;
    padding: 15px;
    border-radius: 5px;
    color: goldenrod;
    box-shadow: 0 0 5px;
    float: left ;
    position: relative;    
    text-align: center;
  }
  .summary {
    position: absolute;
    flex: columns;
    height: 93%;
    width: 92%;
    background-color: rgb(222, 222, 222);
    opacity: 0.6;
  }
  .summarytitle {
    height: 20%;
    text-align: center;
    padding: 30px 0;
    background-color: rgb(228, 184, 255);
    color: black;
    opacity: 100%;
    font-size: 60%;
  }
  .genres {
    position: relative;
    padding: 30px 0;
    display: inline;
    font-size: 70%;
    color: black;
    
  }
  .genres h3 {
    display: inline;
  }
  .card:hover {
    transform: scale(1.2);
    transition: .5s;
  }
  .movie-info:hover {
    visibility: visible;
  }
  .card img{
    width: 100%;
    height: 100%;
    display: block;
    border-radius: 5px;
    object-fit: cover;
  }
  @media (min-width: 500px) {
    .card {
      width: 350px;
      margin: 50px;
      margin-top: 100px;
    }
  }
</style>