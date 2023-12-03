<script setup>

</script>

<template>
  <div class="header">
    <div class="left">
      <el-icon class="back" v-if="state.hasBack" @click="back"><Back /></el-icon>
      <span style="font-size: 20px">{{ state.name }}</span>
    </div>
    <div class="right">
      <el-popover
          placement="bottom"
          :width="320"
          trigger="click"
          popper-class="popper-user-box"
      >
        <template #reference>
          <div class="author">
            <i class="icon el-icon-s-custom" />
            {{ state.userInfo && state.userInfo.nickName || '' }}
            <i class="el-icon-caret-bottom" />
          </div>
        </template>
        <div class="nickname">
          <p>登录名：{{ state.userInfo && state.userInfo.loginUserName || '' }}</p>
          <p>昵称：{{ state.userInfo && state.userInfo.nickName || '' }}</p>
          <el-tag size="small" effect="dark" class="logout" @click="logout">退出</el-tag>
        </div>
      </el-popover>
    </div>
  </div>
</template>


<style scoped>

</style>