<template>
  <div id="app">
    <div id="nav">
      <router-link to="/Movie">Movie</router-link>
      <router-link to="/Community">Community</router-link>
      <span v-if="!isLogin">
        <router-link to="/Login">Login</router-link>
        <router-link to="/Signup">Signup</router-link>
      </span>
      <span v-if="isLogin">
          <router-link to="/Profile">Profile</router-link>
          <a @click="logout">Logout</a>
      </span>
      
      <router-link to="/game">game</router-link>
      <router-view @login="isLogin=true"/>
    </div>

    <footer id="footer">
      <div id="footer_info">
          <div class="footer_info">
            <h2><img src="https://www.ssafy.com/swp_m/images/common/logo3.png" alt="SSAFY"></h2>
            <address>
              <p>Copyright 2021 by SSAFY Inc. All right resereved.</p>
            </address>
          </div>
      </div>
    </footer>
    
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      localStorage.removeItem('user_pk')
      this.$router.push({ name: 'Login'})
    },
  },
}
</script>

<style>
body{
  background-image: url('./cosmos-g5a7e1a86d_1920.jpg');
  background-size: cover;
  background-attachment: fixed;
	background-repeat: no-repeat;
  height: 100%;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  min-height: 100%;
}

#nav {
  margin-top: 30px;
  height: auto;
  min-height: 100%;
  padding-bottom: 60px;
}

#nav a {
  font-weight: bold;
  color: goldenrod;
  text-decoration: none;
  font-size: 30px;
  margin: 10px;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
#footer{
  background: #211f1f;
}
.footer_info {
  padding: 12px 0;
}
.footer_info h2 img {
  width: 150px;
  display: flex;
}
.footer_info address p {
  color: #8f8f8f;
}
</style>
