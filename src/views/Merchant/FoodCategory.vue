<template>
  <el-card class="category-container">
    <template #header>
      <div class="header">
        <el-button type="primary" :icon="Plus" @click="handleAdd">增加</el-button>
        <el-popconfirm
            title="确定删除吗？"
            confirmButtonText='确定'
            cancelButtonText='取消'
            @confirm="handleDelete"
        >
          <template #reference>
            <el-button type="danger" :icon="Delete">批量删除</el-button>
          </template>
        </el-popconfirm>
      </div>
    </template>
    <el-table
        :load="state.loading"
        ref="multipleTable"
        :data="state.tableData"
        tooltip-effect="dark"
        style="width: 100%"
        @selection-change="handleSelectionChange">
      <el-table-column
          type="selection"
          width="55"
      >
      </el-table-column>
      <el-table-column
          prop="type_id"
          label="分类编号"
          width="200"
      >
      </el-table-column>
      <el-table-column
          prop="name"
          label="分类名称"
      >
      </el-table-column>
      <el-table-column
          prop="food_count"
          label="分类菜品数"
          width="200"
      >
      </el-table-column>
      <el-table-column
          label="操作"
          width="220"
      >
        <template #default="scope">
          <a style="cursor: pointer; margin-right: 10px" @click="handleEdit(scope.row.type_id,scope.row.name)">修改</a>
          <el-popconfirm
              title="确定删除吗？"
              confirmButtonText='确定'
              cancelButtonText='取消'
              @confirm="handleDeleteOne(scope.row.type_id)"
          >
            <template #reference>
              <a style="cursor: pointer">删除</a>
            </template>
          </el-popconfirm>
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
    <DialogAddCategory ref='addCate' :reload="getCategory" :type="state.type" />
  </el-card>
</template>

<script setup>
import { onMounted, onUnmounted, reactive, ref, toRefs, watchEffect } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { Plus, Delete } from '@element-plus/icons-vue'
import httpInstance from '@/utils/axios'
import DialogAddCategory from '@/components/DialogAddCategory.vue'
import { useMerchantStore } from '@/stores/merchantStore'
const merchantStore = useMerchantStore()

const addCate = ref(null)
const router = useRouter() // 声明路由实例
const route = useRoute() // 获取路由参数
const state = reactive({
  loading: false,
  tableData: [], // 数据列表
  multipleSelection: [], // 选中项
  total: 0, // 总条数
  currentPage: 1, // 当前页
  pageSize: 10, // 分页大小
  type: 'add', // 操作类型
  level: 1
})

onMounted(() => {
  getCategory()
})

watchEffect(() => {
  console.log(state.pageSize)
})
const unwatch = router.afterEach((to) => {
  // 每次路由变化的时候，都会触发监听时间，重新获取列表数据
  if (['category'].includes(to.name)) {
    getCategory()
  }
})

onUnmounted(() => {
  unwatch()
})

// 获取分类列表
const getCategory = () => {
  state.loading = true
  httpInstance.post('/Merchant/get_types', {
    merchant_id: merchantStore.merchantInfo.userid,
    page_num: state.currentPage,
    page_size: state.pageSize
  }).then(res => {
    state.tableData = res.data.current_page.map(item => item.fields)
    console.log(state.tableData)
    state.total = res.data.total_page
    // state.currentPage = s
    state.loading = false
  })
}

// 添加分类
const handleAdd = () => {
  state.type = 'add'
  addCate.value.open()
}
// 修改分类
const handleEdit = (id,name) => {
  state.type = 'edit'
  addCate.value.open(id,name)
}
// 选择项
const handleSelectionChange = (val) => {
  state.multipleSelection = val
}
// 批量删除
const handleDelete = () => {
  if (!state.multipleSelection.length) {
    ElMessage.error('请选择项')
    return
  }
  httpInstance.post('/Merchant/delete_type', {
    data: {
      ids: state.multipleSelection.map(i => i.categoryId)
    }
  }).then(() => {
    ElMessage.success('删除成功')
    getCategory()
  })
}
// 单个删除
const handleDeleteOne = (id) => {
  // console.log(id)
  httpInstance.post('/Merchant/delete_type', {
      id: id
  }
    ).then(() => {
    ElMessage.success('删除成功')
    getCategory()
  })
}
</script>

<style>

</style>