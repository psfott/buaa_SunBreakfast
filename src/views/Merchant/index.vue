<template>
  <div class="merchant-home">
    <el-container>
      <!-- 侧边栏 -->
      <el-aside width="200px" class="aside">
        <div class="logo">
          <!-- 商家Logo，你可以替换成实际的Logo -->
          <img src="/logo.png" alt="商家Logo">
        </div>
        <el-menu :default-active="activeMenu" @select="handleMenuSelect" background-color="#f4f4f5" text-color="#333" active-text-color="#ffd04b">
          <el-menu-item index="home">首页</el-menu-item>
          <el-menu-item index="dishes">菜品</el-menu-item>
          <el-menu-item index="profile">个人信息</el-menu-item>
        </el-menu>
      </el-aside>

      <!-- 主内容区域 -->
      <el-container>
        <el-header style="background-color: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
          <!-- 商家名称，你可以替换成实际的商家名称 -->
          <div class="merchant-name">商家名称</div>
          <!-- 其他头部信息，比如搜索框、通知等，根据需要添加 -->
          <el-input placeholder="搜索菜品" class="search-input"></el-input>
          <el-badge class="notification" value="3" type="danger" @click="handleNotificationClick">
            <i class="el-icon-bell"></i>
          </el-badge>
        </el-header>

        <el-main>
          <!-- 根据当前选中的菜单项显示不同的内容 -->
          <div v-if="activeMenu === 'home'">
            <!-- 首页内容 -->
            <!-- 你可以在这里添加商家推荐、优惠信息等 -->
          </div>
          <div v-if="activeMenu === 'dishes'">
            <!-- 菜品内容 -->
            <!-- 你可以在这里展示菜品列表、分类等 -->
          </div>
          <div v-if="activeMenu === 'profile'">
            <!-- 个人信息内容 -->
            <!-- 你可以在这里展示商家个人信息、编辑按钮等 -->
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeMenu: 'home' // 默认选中首页
    };
  },
  methods: {
    handleMenuSelect(index) {
      this.activeMenu = index;
    },
    handleNotificationClick() {
      // 处理通知点击事件，你可以弹出通知列表或其他操作
    }
  }
};
</script>

<style scoped>
.merchant-home {
  height: 100vh;
}

.aside {
  background-color: #f4f4f5;
}

.logo {
  text-align: center;
  padding: 20px;
}

.merchant-name {
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

.search-input {
  width: 200px;
  margin-left: 20px;
}

.notification {
  margin-left: 20px;
  cursor: pointer;
}

/* 根据需要添加更多样式 */
</style>
