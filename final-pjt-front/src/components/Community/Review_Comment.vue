<template>
  <div class="fin">
    <span>{{ comment.content }}</span>
    <div v-if="delOk" class="btnbor" @click="comment_del">X</div>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name : "Review_Comment",
  data:function(){
    return {
      delOk :false
    }
  },
  props :{
    comment: Object,
  },
  methods:{
    setToken: function(){
      const token = localStorage.getItem('jwt')
      const config ={
        Authorization: `JWT ${token}`
      }
      return config
    },
    comment_del: function() {
      axios({
        method: "delete",
        url : `http://127.0.0.1:8000/reviews/comments/${ this.comment.id }/`,
        headers: this.setToken(),
      })
        .then(res => {
          console.log(res)
          this.$emit("refresh")
        })
        .catch(err =>{
          console.log(err)
        })
    },
    chekc:function(){
      if (this.comment.user_name == localStorage.getItem("user_id")){
        this.delOk = true
      } else{
        this.delOk = false
      }
    }
  },
  created:function(){
    this.chekc()
  }
}
</script>

<style scoped>
.btnbor{
  display: inline-block;
  margin: 3px;
  padding: 5px;
  font-size:15px;
  color : goldenrod;
  cursor:pointer;
}
.fin {
  border-bottom: 1px solid goldenrod;
}

</style>