<template>
  <div class="user-main">
    <!-- 顶部搜索栏 -->
    <el-header class="header">
      <div class="logo">
        <!-- 外卖系统Logo，你可以替换成实际的Logo -->
        <img src="/logo.png" alt="外卖系统Logo">
      </div>
      <div class="search-bar">
        <el-input v-model="searchKeyword" placeholder="搜索美食"></el-input>
        <el-button type="primary" icon="el-icon-search" @click="search">搜索</el-button>
      </div>
    </el-header>

    <!-- 主体内容区域 -->
    <el-container>
      <!-- 侧边栏 -->
      <el-aside width="200px" class="aside">
        <div class="logo">
          <!-- 你可以在这里放置用户头像等个人信息 -->
          <img src="user-avatar-url" alt="用户头像">
        </div>
        <el-menu :default-active="activeMenu" @select="handleMenuSelect" background-color="#35495e" text-color="#fff" active-text-color="#ffd04b">
          <el-menu-item index="home">主页</el-menu-item>
          <el-menu-item index="profile">个人中心</el-menu-item>
          <el-menu-item index="orders">订单列表</el-menu-item>
          <el-menu-item index="square">美食广场</el-menu-item>
        </el-menu>
      </el-aside>

      <!-- 主体内容区域 -->
      <el-main>
        <!-- 根据当前选中的菜单项显示不同的内容 -->
        <div v-if="activeMenu === 'home'">
          <!-- 主页内容，你可以在这里展示推荐的美食、促销信息等 -->
          <h2>欢迎来到外卖系统主页</h2>
          <!-- 商家列表和搜索功能 -->
          <div class="merchant-list">
            <!-- 显示系统推荐的商家 -->
            <div v-for="merchant in recommendedMerchants" :key="merchant.id">
              <h3>{{ merchant.name }}</h3>
              <!-- 其他商家信息展示 -->
            </div>

            <!-- 搜索框 -->
            <el-input v-model="searchMerchantKeyword" placeholder="搜索商家"></el-input>
            <el-button type="primary" @click="searchMerchant">搜索</el-button>
          </div>

          <!-- ... 其他内容 ... -->
        </div>
        <div v-if="activeMenu === 'profile'">
          <!-- 个人中心内容，你可以在这里展示用户信息、地址管理等 -->
          <h2>个人中心</h2>
        </div>
        <div v-if="activeMenu === 'orders'">
          <!-- 订单列表内容，你可以在这里展示订单历史、当前订单等 -->
          <h2>订单列表</h2>
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
export default {
  data() {
    return {
      searchKeyword: '', // 搜索关键词
      searchMerchantKeyword: '', // 搜索商家关键词
      activeMenu: 'home', // 默认选中主页
      recommendedMerchants: [] // 系统推荐的商家列表
    };
  },
  methods: {
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
  }
};
</script>

<style scoped>
.user-main {
  height: 100vh;
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

.search-bar {
  display: flex;
  align-items: center;
  justify-content: center;
}
.el-menu {
  margin-top: 20px;
}

/* 根据需要添加更多样式 */
</style>
