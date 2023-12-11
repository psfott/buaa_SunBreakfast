<template>
  <el-card class="completed-orders" shadow="hover">
    <h1 class="page-title">已完成订单</h1>

    <!-- Order List using el-table -->
    <el-table :data="completedOrders" style="width: 100%" stripe>
      <el-table-column label="订单ID" prop="id"></el-table-column>
      <el-table-column label="商家位置" prop="merchantLocation"></el-table-column>
      <el-table-column label="送达位置" prop="deliveryLocation"></el-table-column>
      <el-table-column label="订单状态" prop="status"></el-table-column>
    </el-table>

    <!-- Pagination -->
    <el-pagination
        :current-page="currentPage"
        :page-size="pageSize"
        :total="completedOrders.length"
        @current-change="handlePageChange"
    />
  </el-card>
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
  border-radius: 8px;
  margin: 20px 0;
}


.page-title {
  text-align: center;
}
</style>
