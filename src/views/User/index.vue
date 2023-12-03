<template>
  <div class="user-main">
    <!-- 顶部搜索栏 -->
    <el-header class="header">
      <div class="logo">
        <!-- 外卖系统Logo，你可以替换成实际的Logo -->
        <img src="/logo.png" alt="外卖系统Logo">
      </div>
      <div class="header-content">
        <div class="search-bar">
          <el-input v-model="searchKeyword" placeholder="搜索美食"></el-input>
          <el-icon @click="search">
            <Search/>
          </el-icon>
        </div>
      </div>
      <div class="user-info">
        <img class="avatar" src="/user_avatar.jpg" alt="用户头像">
        <span class="user-id">用户ID</span>
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
          <el-sub-menu index="home">
            <template #title>
              <span>去吃饭</span>
            </template>
          <el-menu-item-group>
            <el-menu-item index="/go-order"><el-icon><Odometer /></el-icon>去下单</el-menu-item>
            <el-menu-item index="/order-query"><el-icon><Plus /></el-icon>订单查询</el-menu-item>
          </el-menu-item-group>
          </el-sub-menu>
          <el-menu-item index="profile">个人中心</el-menu-item>
          <el-menu-item index="square">美食广场</el-menu-item>
        </el-menu>
      </el-aside>

      <!-- 主体内容区域 -->
      <el-main>
        <!-- 根据当前选中的菜单项显示不同的内容 -->
        <div v-if="activeMenu === 'home'"  class="home-container">
          <!-- 主页内容，你可以在这里展示推荐的美食、促销信息等 -->
          <h2 class="page-title">欢迎来到北航阳光早餐系统主页</h2>
          <!-- 商家列表和搜索功能 -->
          <div class="merchant-list">
            <!-- 显示系统推荐的商家 -->
            <div v-for="merchant in recommendedMerchants" :key="merchant.id">
              <div class="merchant-item" @click="showMerchantDetails(merchant)">
                <img :src="merchant.image" alt="'Image of ' + merchant.name">
                <h3>{{ merchant.name }}</h3>
                <!-- 其他商家信息展示，根据需要展示商家的其他信息 -->
              </div>
            </div>
          </div>

          <el-dialog :visible.sync="isMerchantDetailsVisible" title="商家详情">
            <!-- 显示商家详情的内容，根据需要展示商家的详细信息 -->
            <h3>{{ selectedMerchant.name }}</h3>
            <img :src="selectedMerchant.image" alt="商家图片">
            <p>{{ selectedMerchant.description }}</p>
            <p>Contact: {{ selectedMerchant.contactInfo }}</p>
            <h4>Menu</h4>
            <ul>
              <li v-for="item in selectedMerchant.menu" :key="item.id">
                {{ item.name }} - {{ item.price }}
              </li>
            </ul>
            <!-- 其他商家详细信息展示 -->
          </el-dialog>

          <!-- ... 其他内容 ... -->
        </div>
        <div v-if="activeMenu === '/go-order'">
          <!-- 去下单的内容 -->
          <h2>去下单</h2>
          <!-- 其他内容 -->
        </div>
        <div v-if="activeMenu === '/order-query'">
          <!-- 订单查询的内容 -->
          <h2>订单查询</h2>
          <!-- 其他内容 -->
        </div>
        <div v-if="activeMenu === 'profile'">
          <!-- 个人中心内容，你可以在这里展示用户信息、地址管理等 -->
          <h2>个人中心</h2>
        </div>
        <div v-if="activeMenu === 'square'">
          <!-- 广场内容，你可以在这里展示用户分享的美食、评价等 -->
          <h2>美食广场</h2>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import {Odometer, Plus, Search} from "@element-plus/icons-vue";

export default {
  components: {Search, Plus, Odometer},
  data() {
    return {
      searchKeyword: '', // 搜索关键词
      searchMerchantKeyword: '', // 搜索商家关键词
      isMerchantDetailsVisible: false,
      activeMenu: 'home', // 默认选中主页
      selectedMerchant: {},
      recommendedMerchants: [{
        id: 1,
        name: 'Merchant 1',
        image: '../../assets/images/merchant1.png', // Update with actual image path
        // Add more properties as needed
      },
        {
          id: 2,
          name: 'Merchant 2',
          image: '../../assets/images/merchant2.png', // Update with actual image path
          // Add more properties as needed
        },] // 系统推荐的商家列表
    };
  },
  methods: {
    showMerchantDetails(merchant) {
      this.selectedMerchant = merchant;
      this.isMerchantDetailsVisible = true;
    },
    handleMenuSelect(index) {
      this.activeMenu = index;
    },
    search() {
      // 处理搜索操作，你可以在这里跳转到搜索结果页面或者展示搜索结果等
      console.log('搜索关键词:', this.searchKeyword);
    },
    searchMerchant() {
      // 根据关键词搜索商家
      // 更新商家列表数据
    }
  },
  created() {
    // 根据路由参数或其他方式获取系统推荐的商家列表等数据
    // 初始化时获取系统推荐的商家列表
    // this.getRecommendedMerchants();
  },
  logout() {
    // Perform any logout logic here
  },
  handleImageError(event) {
    console.error('Image failed to load:', event.target.src);
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

.logo img {
  height: 40px;
  width: auto;
}

.aside {
  background-color: #35495e;
}

.logo {
  text-align: center;
  padding: 10px;
}

.container {
  height: 100vh;
}

.user-info {
  display: flex;
  align-items: center;
  margin-left: auto;
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
  background-image: url('../../assets/images/user_background.png'); /* 请替换成你的图片路径 */
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
