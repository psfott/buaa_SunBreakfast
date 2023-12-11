<template>
  <div class="order-list">
    <h1 class="page-title">可接订单</h1>

    <!-- Order List -->
    <ul>
      <li v-for="order in displayedOrders" :key="order.id" class="order-item">
        <div class="order-info">
          <div><strong>订单ID:</strong> {{ order.id }}</div>
          <div><strong>商家位置:</strong> {{ order.merchantLocation }}</div>
          <div><strong>送达位置:</strong> {{ order.deliveryLocation }}</div>
          <div><strong>订单状态:</strong> {{ order.status }}</div>
        </div>
        <button @click="acceptOrder(order.id)">接单</button>
      </li>
    </ul>

    <!-- Pagination -->
    <el-pagination
        :current-page="currentPage"
        :page-size="pageSize"
        :total="availableOrders.length"
        @current-change="handlePageChange"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      availableOrders: [
        // Your order data here...
      ],
      currentPage: 1,
      pageSize: 5, // Number of orders per page
    };
  },
  computed: {
    displayedOrders() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.availableOrders.slice(startIndex, endIndex);
    },
  },
  methods: {
    acceptOrder(orderId) {
      // Logic to handle accepting an order
      console.log(`Order ${orderId} accepted`);
    },
    handlePageChange(newPage) {
      this.currentPage = newPage;
    },
  },
};
</script>

<style scoped>
.order-list {
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

button {
  flex: 1;
  background-color: #4caf50;
  color: #fff;
  border: none;
  padding: 10px;
  border-radius: 4px;
  cursor: pointer;
}
</style>
