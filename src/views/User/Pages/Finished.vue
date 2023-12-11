<template>
  <el-card class="order-card" shadow="hover">
    <h1 class="page-title">已完成的订单</h1>

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
      <tr v-for="(order, index) in displayedOrders" :key="index">
        <td>{{ order.merchantName }}</td>
        <td>{{ order.deliveryPersonId }}</td>
        <td>{{ order.deliveryTime }}</td>
        <td>
          <!-- Button to open the review dialog -->
          <el-button text @click="openReviewDialog(index)" :type="reviewCompleted ? 'success' : 'primary'">
            {{ reviewCompleted ? '完成评价' : '评价订单' }}
          </el-button>

          <el-dialog v-model="dialogFormVisible" title="订单评价">
            <el-form :model="form">
              <el-form-item label="商家评分" :label-width="formLabelWidth">
                <el-rate v-model="form.merchantRating" />
              </el-form-item>
              <el-form-item label="骑手评分" :label-width="formLabelWidth">
                <el-rate v-model="form.riderRating" />
              </el-form-item>
              <el-form-item label="评价内容" :label-width="formLabelWidth">
                <el-input v-model="form.reviewText" type="textarea" />
              </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                  <el-button @click="dialogFormVisible = false">取消</el-button>
                  <el-button type="primary" @click="submitReview">{{ reviewCompleted ? '完成评价' : '提交评价' }}</el-button>
                </span>
            </template>
          </el-dialog>
        </td>
      </tr>
      </tbody>
    </table>

    <el-pagination
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[10, 20, 30, 40]"
        :page-size="pageSize"
        :total="finishedOrders.length"
    />
  </el-card>
</template>

<script>
import { ref, computed } from 'vue';

export default {
  setup() {
    const dialogFormVisible = ref(false);
    const reviewCompleted = ref(false);
    const formLabelWidth = '140px';
    const form = ref({
      merchantRating: null,
      riderRating: null,
      reviewText: '',
    });

    const finishedOrders = ref([
      {
        orderId: 1,
        merchantName: 'Merchant A',
        deliveryPersonId: 'Rider123',
        deliveryTime: '2023-01-02 12:30:00',
      },
      // Add more finished orders as needed
    ]);

    const currentPage = ref(1);
    const pageSize = ref(10);

    const displayedOrders = computed(() => {
      const startIndex = (currentPage.value - 1) * pageSize.value;
      const endIndex = startIndex + pageSize.value;
      return finishedOrders.value.slice(startIndex, endIndex);
    });

    const openReviewDialog = (index) => {
      form.merchantRating = null;
      form.riderRating = null;
      form.reviewText = '';
      dialogFormVisible.value = true;
    };

    const submitReview = () => {
      // Perform any action with the form values, e.g., send them to the server
      const { merchantRating, riderRating, reviewText } = form.value;
      console.log('Merchant Rating:', merchantRating);
      console.log('Rider Rating:', riderRating);
      console.log('Review Text:', reviewText);

      // Close the review dialog
      dialogFormVisible.value = false;
      reviewCompleted.value = true;
      // You can update the finishedOrders or perform any other necessary actions
    };

    const handleCurrentChange = (newPage) => {
      currentPage.value = newPage;
    };

    return {
      finishedOrders,
      dialogFormVisible,
      reviewCompleted,
      form,
      formLabelWidth,
      openReviewDialog,
      submitReview,
      currentPage,
      pageSize,
      displayedOrders,
      handleCurrentChange,
    };
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

/* Add your custom styles for the review dialog */
.el-dialog textarea {
  width: 100%;
  height: 100px;
  margin-bottom: 10px;
}
.order-card {
  border-radius: 8px;
  margin: 20px 0;
}
</style>
