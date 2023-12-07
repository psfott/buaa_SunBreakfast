<template>
  <div class="merchant—layout">
<!--    <el-container v-if="state.showMenu" class="container">-->
    <el-container class="container">
      <el-aside class="aside">
        <div class="head">
          <div>
            <img src="/logo.png" alt="logo">
            <span>北航阳光早餐</span>
          </div>
        </div>
        <div class="line" />
        <el-menu
            background-color="#222832"
            text-color="#fff"
            :router="true"
            :default-openeds="state.defaultOpen"
            :default-active='state.currentPath'
        >
          <el-sub-menu index="1">
            <template #title>
              <span>Dashboard</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/merchant/intro"><el-icon><Odometer /></el-icon>后台帮助</el-menu-item>

            </el-menu-item-group>
          </el-sub-menu>
          <el-sub-menu index="2">
            <template #title>
              <span>菜品管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/merchant/add"><el-icon><Plus /></el-icon>添加菜品</el-menu-item>
              <el-menu-item index="/merchant/foods"><el-icon><Goods /></el-icon>菜品信息</el-menu-item>
<!--              <el-menu-item index="/merchant/hot"><el-icon><StarFilled /></el-icon>热销套餐</el-menu-item>-->
            </el-menu-item-group>
          </el-sub-menu>
          <el-sub-menu index="3">
            <template #title>
              <span>订单管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/merchant/category"><el-icon><Menu /></el-icon>分类管理</el-menu-item>
<!--              <el-menu-item index="/merchant/good"><el-icon><Goods /></el-icon>套餐管理</el-menu-item>-->
<!--              <el-menu-item index="/merchant/guest"><el-icon><User /></el-icon>会员管理</el-menu-item>-->
              <el-menu-item index="/merchant/order"><el-icon><List /></el-icon>订单管理</el-menu-item>
            </el-menu-item-group>
          </el-sub-menu>
          <el-sub-menu index="4">
            <template #title>
              <span>系统管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/merchant/account"><el-icon><Lock /></el-icon>商户信息修改</el-menu-item>
            </el-menu-item-group>
          </el-sub-menu>
        </el-menu>
      </el-aside>
      <el-container class="content">
        <Header />
        <div class="main">
          <router-view />
        </div>
<!--        <Footer />-->
      </el-container>
    </el-container>
<!--    <el-container v-else class="container">-->
    <el-container class="container">
      <router-view />
    </el-container>
  </div>
</template>

<script setup>

import {reactive} from "vue";
import {localGet, pathMap} from "@/utils";
import router from "@/router";
import Header from "@/components/Header.vue";
const noMenu = ['/login']

const state = reactive({
  showMenu: true,
  defaultOpen: ['1', '2', '3', '4'],
  currentPath: '/merchant',
})

// router.afterEach((to, from) => {
//   state.showMenu = !noMenu.includes(to.path)
// })

router.beforeEach((to, from, next) => {
  // if (to.path == '/login') {
  //   // 如果路径是 /login 则正常执行
  //   next()
  // } else {
  //   // 如果不是 /login，判断是否有 token
  //   if (!localGet('token')) {
  //     // 如果没有，则跳至登录页面
  //     next({ path: '/login' })
  //   } else {
  //     // 否则继续执行
  //     next()
  //   }
  // }
  next()
  state.currentPath = to.path
  document.title = pathMap[to.name]
})
</script>


<style scoped>
.layout {
  min-height: 100vh;
  background-color: #ffffff;
}
.container {
  height: 100vh;
}
.aside {
  width: 200px!important;
  background-color: #222832;
}
.head {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
}
.head > div {
  display: flex;
  align-items: center;
}

.head img {
  width: 50px;
  height: 50px;
  margin-right: 10px;
}
.head span {
  font-size: 20px;
  color: #ffffff;
}
.line {
  border-top: 1px solid hsla(0,0%,100%,.05);
  border-bottom: 1px solid rgba(0,0,0,.2);
}
.content {
  display: flex;
  flex-direction: column;
  max-height: 100vh;
  overflow: hidden;
}
.main {
  height: calc(100vh - 100px);
  overflow: auto;
  padding: 10px;
}
</style>

<style>
body {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
.el-menu {
  border-right: none!important;
}
.el-submenu {
  border-top: 1px solid hsla(0, 0%, 100%, .05);
  border-bottom: 1px solid rgba(0, 0, 0, .2);
}
.el-submenu:first-child {
  border-top: none;
}
.el-submenu [class^="el-icon-"] {
  vertical-align: -1px!important;
}
a {
  color: #409eff;
  text-decoration: none;
}
.el-pagination {
  text-align: center;
  margin-top: 20px;
}
.el-popper__arrow {
  display: none;
}
</style>
