<template>
  <div class="user-main">
    <!-- 顶部搜索栏 -->
    <el-header class="header">
      <div class="logo">
        <!-- 外卖系统Logo，你可以替换成实际的Logo -->
        <img src="/logo.png" alt="外卖系统Logo">
        <span>北航阳光早餐</span>
      </div>

      <div class="user-info">
        <img class="avatar" src="@/assets/images/user_avatar.jpg" alt="用户头像">
        <div class="user-details">
          <span class="user-id">psfott</span>
          <span class="user-role" >学生</span>
        </div>
          <router-link to="/" class="logout-link">
          <el-button type="text" @click="logout">退出登录</el-button>
        </router-link>
      </div>
    </el-header>

    <!-- 主体内容区域 -->
    <el-container class="container">
      <!-- 侧边栏 -->
      <el-aside width="200px" class="aside">
        <!-- 根据需要设置的背景图片和模糊效果 -->
        <div class="background-image"></div>
        <el-menu
            :default-active="activeMenu"
            @select="handleMenuSelect"
            background-color="#35495e"
            text-color="#fff"
            active-text-color="#ffd04b"
        >
          <el-menu-item index="main">
            <router-link to="/user/main">首页</router-link>
          </el-menu-item>
          <el-sub-menu index="order">
            <template #title>
              <span>我的订单</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/ongoing"><el-icon><Odometer /></el-icon>
                <router-link to="/user/ongoing">进行中</router-link>
              </el-menu-item>
              <el-menu-item index="/finished"><el-icon><Plus /></el-icon>
                <router-link to="/user/finished">已完成</router-link>
              </el-menu-item>
            </el-menu-item-group>
          </el-sub-menu>
          <el-menu-item index="profile">
            <router-link to="/user/profile">个人中心</router-link>
          </el-menu-item>
        </el-menu>
      </el-aside>

      <!-- 主体内容区域，使用 <router-view> 渲染子路由 -->
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import { Odometer, Plus, Search } from "@element-plus/icons-vue";

export default {
  components: { Search, Plus, Odometer },
  data() {
    return {
      searchKeyword: "", // 搜索关键词
      activeMenu: "main", // 默认选中首页
    };
  },
  methods: {
    handleMenuSelect(index) {
      this.activeMenu = index;
    },
    logout() {
      // 执行退出登录的逻辑
    },
  },
};
</script>

<style scoped>
.user-main {
  height: 100vh;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0 auto;
}

.header {
  background-color: #35495e;
  color: #fff;
  padding: 10px;
  display: flex;
  width: 100%;
  box-sizing: border-box;
}

.logo {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
}

.logo > div {
  display: flex;
  align-items: center;
}

.logo span {
  font-size: 20px;
  color: #ffffff;
}

.logo img {
  width: 50px;
  height: 50px;
  margin-right: 10px;
}

.aside {
  background-color: #35495e;
}


.container {
  height: 100vh;
}

.user-info {
  display: flex;
  align-items: center;
  margin-left: auto;
}

.user-details {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-left: 10px; /* Adjust the margin as needed */
}

.user-role {
  background-color: orange;
  padding: 5px;
  margin-top: 5px; /* Adjust the margin as needed */
  font-family: "Cooper Black",serif
}

.avatar {
  width: 40px; /* 调整头像宽度 */
  height: 40px; /* 调整头像高度 */
  border-radius: 50%;
  margin-right: 10px;
}

.user-id {
  margin-right: 10px;
}

.search-bar {
  display: flex;
  align-items: center;
  flex-grow: 1; /* 搜索栏占据剩余空间 */
  max-width: 300px; /* 搜索框最大宽度 */
  justify-content: center;
}
.background-image {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  //background-image: url('../../../assets/images/user_background.png'); /* 请替换成你的图片路径 */
  background-color: white;
  background-size: cover;
  background-position: center;
  opacity: 0.7;
  filter: blur(5px); /* 调整模糊效果的强度 */
  z-index: -1; /* 将背景图放在最底层 */
}

.page-title {
  margin-top: 50px; /* 通过上边距调整标题距离顶部的位置 */
  font-size: 24px; /* 可以根据需要调整字体大小 */
  /* 其他样式... */
}

.home-container {
  text-align: center; /* 居中内容 */
}

.el-menu {
  margin-top: 20px;
}

.merchant-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin-top: 20px;
}

.merchant-item {
  margin: 10px;
  cursor: pointer;
}

.merchant-item img {
  width: 200px; /* Adjust as needed */
  height: 150px; /* Adjust as needed */
  border-radius: 8px;
  object-fit: cover;
}

.merchant-item h3 {
  margin-top: 10px;
}
/* 根据需要添加更多样式 */
</style>
