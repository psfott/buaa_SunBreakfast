<template>
  <div class="merchant-layout">
    <el-card class="account-container">
      <h1>欢迎使用北航阳光早餐骑手系统</h1>

      <section>
        <h2>如何接单</h2>
        <p>在订单管理中，点击“去接单”按钮，即可跳转到接单界面，即可选择相应的订单。成功接单后，订单会添加到运送中订单表中。添加新的菜品。</p>
      </section>

      <section>
        <h2>订单取餐与送达</h2>
        <p>订单送达后，点击“进行中订单”，即可查看正在运送的订单。当订单送达时，联系乘客并点击已送达按钮即可。</p>
      </section>

      <section>
        <h2>已完成订单</h2>
        <p>已完成订单可以查看所有历史接过的订单并查看订单状态以及评价。</p>
      </section>

      <section>
        <h2>个人中心</h2>
        <p>个人中心用于修改骑手信息，你可以在这里修改骑手头像，电话号码等等。</p>
      </section>

      <p>以上仅是系统的核心功能介绍，详细操作可参考具体页面的帮助文档。祝你使用愉快！</p>
    </el-card>
  </div>
</template>

<script setup>
// 组件逻辑...
</script>

<style scoped>
.merchant-layout {
  min-height: 100vh;
  background-color: #ffffff;
}

.account-container {
  margin: 20px auto;
  padding: 20px;
  height: 100vh;
}

h1, h2 {
  color: #333;
}

section {
  margin-bottom: 20px;
}

p {
  line-height: 1.6;
}
</style>
