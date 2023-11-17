<template>
  <div class="home">
    <h1 class="title">北航阳光早餐系统</h1>
    <el-button @click="showMessage" type="success" size="large" round>我是学生</el-button>
    <el-button @click="showMessage" type="primary" size="large" round>我是商家</el-button>
    <el-button @click="showMessage" type="danger" size="large" round>我是骑手</el-button>
  </div>
</template>

<script>
import {ElMessage} from "element-plus";

export default {
  data(){
    return{}
  },
  methods: {
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
  margin-bottom: 150px; /* Add some space below the title */
  color: #83c0fd;
}

/* Style adjustments for the buttons */
.el-button {
  margin: 10px; /* Add margin to separate buttons */
  font-size: 16px; /* Adjust the font size of the buttons */
  width: 200px; /* Set a fixed width for the buttons */
}
</style>
