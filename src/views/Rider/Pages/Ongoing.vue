<template>
  <div class="ongoing-orders">
    <el-card class="order-card" shadow="hover">
      <h1 class="page-title">进行中订单</h1>

      <!-- Order List using el-table -->
      <el-table :data="displayedOrders" style="width: 100%">
        <el-table-column label="订单ID" prop="id"></el-table-column>
        <el-table-column label="商家位置" prop="merchantLocation"></el-table-column>
        <el-table-column label="送达位置" prop="deliveryLocation"></el-table-column>
        <el-table-column label="订单状态" prop="status"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="success" @click="completeOrder(scope.row.id)">完成订单</el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- Pagination -->
      <el-pagination
          :current-page="currentPage"
          :page-sizes="[5, 10, 20]"
          :page-size="pageSize"
          :total="onGoingOrders.length"
          @current-change="handlePageChange"
      />
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      onGoingOrders: [
        {
          id: 1,
          merchantLocation: "123 Main St, City",
          deliveryLocation: "456 Oak St, Town",
          status: "进行中",
        },
        {
          id: 2,
          merchantLocation: "789 Pine St, Village",
          deliveryLocation: "101 Elm St, Hamlet",
          status: "进行中",
        },
        {
          id: 3,
          merchantLocation: "202 Maple St, Borough",
          deliveryLocation: "303 Birch St, District",
          status: "进行中",
        },
        {
          id: 4,
          merchantLocation: "404 Cedar St, Township",
          deliveryLocation: "505 Walnut St, County",
          status: "进行中",
        },
        {
          id: 5,
          merchantLocation: "606 Fir St, Municipality",
          deliveryLocation: "503 Ps St, NewYork",
          status: "进行中",
        },
      ],
      currentPage: 1,
      pageSize: 5, // Number of orders per page
    };
  },
  computed: {
    displayedOrders() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.onGoingOrders.slice(startIndex, endIndex);
    },
  },
  methods: {
    completeOrder(orderId) {
      // Logic to handle completing an ongoing order
      console.log(`Order ${orderId} completed`);
    },
    handlePageChange(newPage) {
      this.currentPage = newPage;
    },
  },
};
</script>

<style scoped>
.ongoing-orders {
  max-width: 800px;
  margin: 20px auto;
}

.order-card {
  border-radius: 8px;
  margin: 20px 0;
}

.page-title {
  text-align: center;
}
</style>
