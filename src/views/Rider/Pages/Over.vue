<template>
  <div class="completed-orders">
    <h1 class="page-title">已完成订单</h1>

    <!-- Order List -->
    <ul>
      <li v-for="order in displayedOrders" :key="order.id" class="order-item">
        <div class="order-info">
          <div><strong>订单ID:</strong> {{ order.id }}</div>
          <div><strong>商家位置:</strong> {{ order.merchantLocation }}</div>
          <div><strong>送达位置:</strong> {{ order.deliveryLocation }}</div>
          <div><strong>订单状态:</strong> {{ order.status }}</div>
        </div>
      </li>
    </ul>

    <!-- Pagination -->
    <el-pagination
        :current-page="currentPage"
        :page-size="pageSize"
        :total="completedOrders.length"
        @current-change="handlePageChange"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      completedOrders: [
        // Your completed order data here...
      ],
      currentPage: 1,
      pageSize: 5, // Number of orders per page
    };
  },
  computed: {
    displayedOrders() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.completedOrders.slice(startIndex, endIndex);
    },
  },
  methods: {
    handlePageChange(newPage) {
      this.currentPage = newPage;
    },
  },
};
</script>

<style scoped>
.completed-orders {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f8f8f8;
}

.page-title {
  text-align: center;
}

.order-item {
  list-style: none;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin: 10px 0;
  padding: 10px;
  display: flex;
  justify-content: space-between;
}

.order-info {
  flex: 3;
}
</style>
