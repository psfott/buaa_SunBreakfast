<template>
  <el-card class="food-container">
    <template #header>
      <div class="header">
        <el-button type="primary" :icon="Plus" @click="handleAdd">新增菜品</el-button>
      </div>
    </template>
    <el-table
        :load="state.loading"
        :data="state.tableData"
        tooltip-effect="dark"
        style="width: 100%"
    >
      <el-table-column
          prop="id"
          label="菜品编号"
      >
      </el-table-column>
      <el-table-column
          prop="name"
          label="菜品名"
      >
      </el-table-column>
      <el-table-column
          prop="type_id"
          label="菜品种类"
      >
      </el-table-column>
      <el-table-column
          prop="goodsIntro"
          label="菜品简介"
      >
      </el-table-column>
      <el-table-column
          label="菜品图片"
          width="150px"
      >
        <template #default="scope">
<!--          <img style="width: 100px; height: 100px;" :key="scope.row.goodsId" :src="$filters.prefix(scope.row.goodsCoverImg)" alt="菜品主图">-->
        </template>
      </el-table-column>
      <el-table-column
          prop="score"
          label="菜品评分"
      >
      </el-table-column>
      <el-table-column
          prop="price"
          label="菜品售价"
      >
      </el-table-column>
      <el-table-column
          label="上架状态"
      >
        <template #default="scope">
          <span style="color: green;" v-if="scope.row.goodsSellStatus == 0">销售中</span>
          <span style="color: red;" v-else>已下架</span>
        </template>
      </el-table-column>

      <el-table-column
          label="操作"
          width="100"
      >
        <template #default="scope">
          <a style="cursor: pointer; margin-right: 10px" @click="handleEdit(scope.row.goodsId)">修改</a>
          <a style="cursor: pointer; margin-right: 10px" v-if="scope.row.goodsSellStatus == 0" @click="handleStatus(scope.row.goodsId, 1)">下架</a>
          <a style="cursor: pointer; margin-right: 10px" v-else @click="handleStatus(scope.row.goodsId, 0)">上架</a>
        </template>
      </el-table-column>
    </el-table>
    <!--总数超过一页，再展示分页器-->
    <el-pagination
        background
        layout="prev, pager, next"
        :total="state.total"
        :page-size="state.pageSize"
        :current-page="state.currentPage"
        @current-change="changePage"
    />
  </el-card>
</template>

<script setup>
import { onMounted, reactive, getCurrentInstance } from 'vue'
import httpInstance from '@/utils/axios'
import { ElMessage } from 'element-plus'
import { Plus, Delete } from '@element-plus/icons-vue'
import { useRouter } from 'vue-router'
import { useMerchantStore } from '@/stores/merchantStore'
const merchantStore = useMerchantStore()

const app = getCurrentInstance()
const { goTop } = app.appContext.config.globalProperties
const router = useRouter()
const state = reactive({
  loading: false,
  tableData: [], // 数据列表
  total: 0, // 总条数
  currentPage: 1, // 当前页
  pageSize: 10 // 分页大小
})
onMounted(() => {
  getGoodList()
})
// 获取轮播图列表
const getGoodList = () => {
  state.loading = true
  httpInstance.post('/Merchant/get_foods', {
      merchant_id: merchantStore.merchantInfo.userid,
      page_num: state.currentPage,
      page_size: state.pageSize
  }).then(res => {
    state.tableData = res.data.current_page.map(item => item.fields)
    console.log(state.tableData)
    state.total = res.data.totalPage
    state.loading = false
    goTop && goTop()
  })
}
const handleAdd = () => {
  router.push({ path: '/merchant/add' })
}
const handleEdit = (id) => {
  router.push({ path: '/merchant/add', query: { id } })
}
const changePage = (val) => {
  state.currentPage = val
  getGoodList()
}
const handleStatus = (id, status) => {
  axios.put(`/goods/status/${status}`, {
    ids: id ? [id] : []
  }).then(() => {
    ElMessage.success('修改成功')
    getGoodList()
  })
}
</script>

<style scoped>
.good-container {
  min-height: 100%;
}
.el-card.is-always-shadow {
  min-height: 100%!important;
}
</style>
