import Vue from 'vue'
import VueRouter from 'vue-router'
import Movie from '../components/Movie.vue'
import Movie_Detail from '../components/Movie_Detail.vue'
import Community from '../components/Community/Community.vue'
import Community_Detail from '../components/Community/Community_Detail.vue'
import Community_Review_Create from '../components/Community/Community_Review_Create.vue'
import Community_Review_Update from '../components/Community/Community_Review_Update.vue'
import Login from '../components/Login/Login.vue'
import Signup from '../components/Login/Signup.vue'
import Profile from '../components/Login/Profile.vue'
import game from '../components/game/game.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Movie',
    component: Movie,
    meta: {
      title:"무비",
    }
  },
  {
    path: '/Movie_Detail/:id',
    name: 'Movie_Detail',
    component: Movie_Detail,
    props: route => ({
      id: Number(route.params.id)
    }),
    meta: {
      title:"무비 상세",
    }
  },
  {
    path: '/Community',
    name: 'Community',
    component: Community,
    meta: {
      title:"리뷰목록",
    }
  },
  {
    path: '/Community_Detail/:id',
    name: 'Community_Detail',
    component: Community_Detail,
    props: route => ({
      id: Number(route.params.id)
    })
  },
  {
    path: '/Community_Review_Create',
    name: 'Community_Review_Create',
    component: Community_Review_Create
  },
  {
    path: '/Community_Review_Update',
    name: 'Community_Review_Update',
    component: Community_Review_Update,
    props: route => ({
      id: Number(route.params.id)
    })
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login
  },
  {
    path: '/Signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/Profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/game',
    name: 'game',
    component: game
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
