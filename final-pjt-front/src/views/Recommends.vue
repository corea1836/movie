<template>
  <div class="recobox">
    <li v-for="genre in favorGenre" :key = genre.id>
      <button @click="filteredMovies(genre)">{{ genre }}</button>
    </li>
    <div class="movieSlider">
      <button @click="prev" type="button" class="btn btn-left" ></button>
      <MovieListCard class="movieCard" :style="{transform: `translateX(${index}px)`, transition: `${transition}`}"
        v-for="movie in recomovies"
        :key="movie.id"
        :movie="movie"
        v-on:movie-detail="movieDetail($event)"/>
    <button @click="next" type="button" class="btn btn-right" ></button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListCard from '../components/MovieListCard.vue'

export default {
  name: "Recommends",
  components: {
    MovieListCard,
  },
  data: function() {
    return{
      favorGenre: [],
      movies: null,
      recomovies: null,
      
      index: 0,
      transition: "transform 0.8s ease"
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
    getFavoGenres: function() {
      axios({
        method: "get",
        url:`http://127.0.0.1:8000/accounts/profile/`,
        headers: this.setToken()
      })
        .then((res)=>{
          this.favorGenre =res.data.genres
          console.log(this.favorGenre)
        })
        .catch((err)=>{
          console.log(err);
        })
    },
    getMovies: function() {
      axios({
        method: 'get',
        url: "http://127.0.0.1:8000/movies/",
      })
        .then( res => {
          this.movies = res.data
          console.log(this.movies)
        })
        .catch(err => {
          console.log(err)
        })
    },
    filteredMovies: function(gid) {
      console.log('aaaaaaaaaaa')
      this.recomovies = this.movies.filter(movie => {
        console.log(movie)
        return movie.genre.some(g => {
          console.log(g)
          return g.id == gid
        })
        })
        console.log(this.recomovies)
      },
    prev() {
      console.log(this.index)
      if(this.index === 0){
        this.transition = "none"
        this.index = -1500
      } else {
        this.transition = "transform 0.8s ease"
        this.index += 500;
      }
    },
    next() {
      console.log(this.index)
      if(this.index === -1500) {
        this.transition = "none"
        this.index = 0;
      } else {
        this.transition = "transform 0.8s ease"
        this.index -= 500;
      }
    },
  },  
  created: function() {
    this.getFavoGenres()
    this.getMovies()
    this.filteredMovies()
  },
}
</script>

<style scoped>
  .movieSlider {
    display: flex;
    width: 80%;
    height: 80%;
    margin: 80px auto 0;
    /*background: black;*/
    overflow: hidden;
    position: relative;
  }
  .btn {
    outline: none;
    border: none;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: block;
    position: absolute;
    z-index: 1000;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .btn-left {
    top: 50%;
    left: 5px;
    transform: translateY(-50%);
  }
  .btn-right {
    top: 50%;
    right: 5px;
    transform: translateY(-50%);
  }
</style>