<template>
  <div class="merchant-layout">
    <el-card class="account-container">
      <h1>欢迎使用北航阳光早餐商家管理系统</h1>

      <section>
        <h2>Dashboard 概览</h2>
        <p>Dashboard 是系统的核心，它提供了关键指标和数据的一览。你可以在这里快速了解销售情况、订单状态等信息。</p>
      </section>

      <section>
        <h2>添加新菜品</h2>
        <p>在菜品管理中，点击“添加菜品”按钮，填写相关信息，即可成功添加新的菜品。确保提供准确的菜品信息，以便吸引顾客。</p>
      </section>

      <section>
        <h2>首页配置</h2>
        <p>首页配置允许你自定义展示内容，包括菜品轮播和热销套餐。在这里，你可以编辑菜品展示顺序和设置热销套餐。</p>
      </section>

      <section>
        <h2>模块管理</h2>
        <p>模块管理涵盖了分类管理、套餐管理、会员管理和订单管理。你可以在这里管理商品分类、编辑套餐内容，以及查看订单状态。</p>
      </section>

      <section>
        <h2>系统管理</h2>
        <p>系统管理用于修改商户信息，你可以在这里修改商户头像，编辑章后信息等等。</p>
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
