<template>
  <div>
    <h1 class="page-title">已完成的订单</h1>
    <el-dialog title="订单评价">
      <!-- Your review form goes here -->
      <!-- You can use a textarea or any other form elements for the review -->
      <textarea v-model="reviewText" placeholder="请输入订单评价"></textarea>

      <!-- Button to submit the review -->
      <el-button @click="submitReview">提交评价</el-button>
    </el-dialog>

    <table class="order-table">
      <thead>
      <tr>
        <th>商家名称</th>
        <th>骑手ID</th>
        <th>送达时间</th>
        <th>评价订单</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(order, index) in finishedOrders" :key="index">
        <td>{{ order.merchantName }}</td>
        <td>{{ order.deliveryPersonId }}</td>
        <td>{{ order.deliveryTime }}</td>
        <td>
          <!-- Button to open the review dialog -->
          <button @click="openReviewDialog(index)">评价订单</button>
        </td>
      </tr>
      </tbody>

    </table>

    <!-- Review Dialog -->

  </div>
</template>

<script>
export default {
  data() {
    return {
      finishedOrders: [
        {
          orderId: 1,
          merchantName: 'Merchant A',
          deliveryPersonId: 'Rider123',
          deliveryTime: '2023-01-02 12:30:00',
        },
        // Add more finished orders as needed
      ],
      reviewDialogVisible: false,
      reviewText: '',
      selectedOrderIndex: null,
    };
  },
  methods: {
    openReviewDialog(index) {
      this.selectedOrderIndex = index;
      this.reviewText = ''; // Clear previous review text
      this.reviewDialogVisible = true;
      console.log('OpenDialog:', this.reviewText);
    },
    submitReview() {
      // Perform any action with the reviewText, e.g., send it to the server
      console.log('Review submitted:', this.reviewText);

      // Close the review dialog
      this.reviewDialogVisible = false;

      // Update the UI or perform any other necessary actions
      this.$set(this.finishedOrders, this.selectedOrderIndex, {
        ...this.finishedOrders[this.selectedOrderIndex],
        review: this.reviewText,
      });
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

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f8f8f8;
}

/* Add your custom styles for the review dialog */
.el-dialog textarea {
  width: 100%;
  height: 100px;
  margin-bottom: 10px;
}
</style>
