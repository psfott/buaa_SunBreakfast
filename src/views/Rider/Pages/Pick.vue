<template>
  <el-card class="order-card" shadow="hover">
    <h1 class="page-title">可接订单</h1>

    <!-- Order List using el-table -->
    <el-table :data="availableOrders" style="width: 100%" stripe>
      <el-table-column label="订单ID" prop="id"></el-table-column>
      <el-table-column label="商家位置" prop="merchantLocation"></el-table-column>
      <el-table-column label="送达位置" prop="deliveryLocation"></el-table-column>
      <el-table-column label="订单状态" prop="status"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="primary" @click="acceptOrder(scope.row.id)">接单</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- Pagination -->
    <el-pagination
        :current-page="currentPage"
        :page-size="pageSize"
        :total="availableOrders.length"
        @current-change="handlePageChange"
    />
  </el-card>
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
.order-card {
  border-radius: 8px;
  margin: 20px 0;
}

.page-title {
  text-align: center;
}
</style>
