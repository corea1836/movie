<template>
  <div>
     <div class="movieSlider">
      <div @click="prev" class="btn btn-left"><i class="fas fa-chevron-left"></i></div>
      <MovieListCard class="movieCard" :style="{transform: `translateX(${index}px)`, transition: `${transition}`}"
        v-for="movie in movies" 
        :key="movie.id"
        :movie="movie"
        v-on:movie-detail="movieDetail($event)"/>
      <div @click="next" class="btn btn-right"><i class="fas fa-chevron-right"></i></div>
    </div>
    <h2 class="recogenre">장르별 추천</h2>
    <div class="movieSlider2" v-for="(recomovie, i) in recomovies" :key= recomovie.id>
        <div @click="prev2(i)" class="btn btn-left"><i class="fas fa-chevron-left"></i></div>

        <MovieListCard class="movieCard" :style="{transform: `translateX(${index2[i]}px)`, transition: `${transition}`}"
          v-for="movie in recomovie"
          :key="movie.id"
          :movie="movie"
          />

        <div @click="next2(i)" class="btn btn-right"><i class="fas fa-chevron-right"></i></div>
    </div>

    </div>

</template>

<script>
import axios from 'axios'
import MovieListCard from './MovieListCard.vue'


export default {
  name: 'Movie',
  components: {
    MovieListCard,
  },
  computed: {
    moviesLens() {
      return this.movies.length
    }
  },
  data: function () {
    return {
      movies: null,
      genres: [],
      index: 0,
      index2: [0, 0, 0],
      transition: "transform 0.8s ease",
      favorGenre: [],
      recomovies: [[], [], []],
    }
  },
  methods: {
    getMovie: function () {
      axios({
        method: 'get',
        url: "http://127.0.0.1:8000/movies/",
      })
      .then( res => {
        this.movies = res.data
        this.getGenre()
      })
      .catch(err => {
        console.log(err)
      })
    },
    getDetail: function(event) {
      console.log(event.target.data);
    },
    getGenre: function() {
      axios({
        mehtod: 'get',
        url: "http://127.0.0.1:8000/movies/genres"
      })
      .then( res=> {
        this.genres = res.data
        this.getFavoGenres()
      })
    },
    prev() {
      if(this.index === 0) {
        this.transition = "none"
        this.index = 0
      }else {
        this.transition = "transform 0.8s ease"
        this.index += 500;
      }
    },
    next() {
      console.log(this.movies.length)
      if(this.index === this.movies.length) {
        this.transition = "none"
        this.index = 0;
      }else {
        this.transition = "transform 0.8s ease"
        this.index -= 500;
        console.log(this.index)
      }
    },

    prev2(i) {
      if(this.index2[i] === 0) {
        this.transition = "none"
        this.$set(this.index2, i, 0)
      }else {
        this.transition = "transform 0.8s ease"
        this.$set(this.index2, i, this.index2[i] + 500)
      }
    },
    next2(i) {
      console.log(this.recomovies[i].length)
      if(this.index2[i] === this.recomovies[i].length) {
        this.transition = "none"
        this.$set(this.index2, i, 0)
      }else {
        this.transition = "transform 0.8s ease"
        this.$set(this.index2, i, this.index2[i] - 500)
      }
    },
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
          for(var i = 0; i < 3; i ++) {
            this.$set(this.recomovies, i, this.filteredMovies(this.favorGenre[i]))
            //this.recomovies[i] = this.filteredMovies(this.favorGenre[i])
          }
          console.log(this.recomovies)
        })
        .catch((err)=>{
          console.log(err);
        })
    },
    filteredMovies: function(gid) {
      const recommends = this.movies.filter(movie => {
        return movie.genre.some(g => {
          return g.id == gid
        })
        }) 
        return recommends
      },
  },
  created: function () {
    this.getMovie()
  },
}
</script>

<style scoped>
  .movieSlider {
    display: flex; 
    width: 90%;
    height: 50%;
    margin: 80px;
    /*background: black;*/
    position: relative;
    overflow: hidden;
  }
  .movieSlider2 {
    display: flex; 
    width: 90%;
    height: 50%;
    margin: 80px;
    /*background: black;*/
    position: relative;
    overflow: hidden;
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
  .recogenre {
    color: goldenrod;
    font-size: 70px;
  }
  i {
    font-size: 50px;
    color: goldenrod;
  }
</style>