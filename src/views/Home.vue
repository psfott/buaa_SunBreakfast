<template>
  <div class="home">
    <h1 class="title">北航阳光早餐系统</h1>
<!--    <router-link to="/login">-->
      <el-button @click="loginUser" type="success" size="large" round :icon="User">我是学生</el-button>
      <el-button @click="loginMerchant" type="primary" size="large" round :icon="Avatar">我是商家</el-button>
      <el-button @click="loginRider" type="danger" size="large" round :icon="UserFilled">我是骑手</el-button>
<!--    </router-link>-->
  </div>
</template>

<script>
import {ElMessage} from "element-plus";
import {Avatar, User, UserFilled} from "@element-plus/icons-vue";
import router from "@/router";

export default {
  computed: {
    UserFilled() {
      return UserFilled
    },
    Avatar() {
      return Avatar
    },
    User() {
      return User
    }
  },
  data(){
    return{}
  },
  methods: {
    loginMerchant(){
      router.replace('/merchantLogin')
      this.showMessage()
    },
    loginUser(){
      router.replace('/userLogin')
      this.showMessage()
    },

    showMessage() {
      ElMessage({type: 'success',message:'欢迎光临'})
    }
  }
}
</script>

<style scoped>
.home {
  text-align: center; /* Center-align the content */
  padding: 80px; /* Add some padding for better visual appearance */
  height: 75vh;
  background-image: url('@/assets/Home.jpg');
  background-size: cover;
  background-position: center;
  color: #fff;
}

.title {
  font-size: 50px; /* Adjust the font size as needed */
  margin-top: 150px;
  margin-bottom: 150px; /* Add some space below the title */
  color: #b1d7fd;
}

/* Style adjustments for the buttons */
.el-button {
  margin: 10px; /* Add margin to separate buttons */
  font-size: 16px; /* Adjust the font size of the buttons */
  width: 200px; /* Set a fixed width for the buttons */
}
</style>
