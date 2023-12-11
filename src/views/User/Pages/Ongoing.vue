<template>
  <el-card class="order-card" shadow="hover">
    <h1 class="page-title">进行中的订单</h1>

    <table class="order-table">
      <thead>
      <tr>
        <th>商家名称</th>
        <th>下单时间</th>
        <th>接单时间</th>
        <th>预计送达时间</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(order, index) in displayedOrders" :key="index">
        <td>{{ order.merchantName }}</td>
        <td>{{ order.orderTime }}</td>
        <td>{{ order.acceptTime }}</td>
        <td>{{ order.estimatedDeliveryTime }}</td>
      </tr>
      </tbody>
    </table>

    <el-pagination
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-size="pageSize"
        :total="ongoingOrders.length"
    />
  </el-card>
</template>

<script>
export default {
  data() {
    return {
      ongoingOrders: [
        {
          merchantName: 'Merchant A',
          orderTime: '2023-01-01 10:00:00',
          acceptTime: '2023-01-01 10:15:00',
          estimatedDeliveryTime: '2023-01-01 11:00:00',
        },
        // Add more ongoing orders as needed
      ],
      currentPage: 1,
      pageSize: 10,
    };
  },
  computed: {
    displayedOrders() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.ongoingOrders.slice(startIndex, endIndex);
    },
  },
  methods: {
    handleCurrentChange(newPage) {
      this.currentPage = newPage;
    },
  },
};
</script>

<style scoped>
.page-title {
  text-align: center;
}

.order-table {
  width: 80%;
  margin: 20px auto;
  border-collapse: collapse;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f8f8f8;
}

.order-card {
  border-radius: 8px;
  margin: 20px 0;
}
</style>
