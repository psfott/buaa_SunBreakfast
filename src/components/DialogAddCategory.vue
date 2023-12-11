<template>
  <el-dialog
    :title="props.type == 'add' ? '添加分类' : '修改分类'"
    v-model="state.visible"
    width="400px"
  >
    <el-form :model="state.ruleForm" :rules="state.rules" ref="formRef" label-width="100px" class="good-form">
      <el-form-item label="分类名称" prop="name">
        <el-input type="text" v-model="state.ruleForm.name"></el-input>
      </el-form-item>
<!--      <el-form-item label="排序值" prop="rank">-->
<!--        <el-input type="number" v-model="state.ruleForm.rank"></el-input>-->
<!--      </el-form-item>-->
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="state.visible = false">取 消</el-button>
        <el-button type="primary" @click="submitForm">确 定</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRoute } from 'vue-router'
import httpInstance from '@/utils/axios'
import { ElMessage } from 'element-plus'

import { useMerchantStore } from '@/stores/merchantStore'
import table from "wangeditor/src/menus/table";
const merchantStore = useMerchantStore()

const props = defineProps({
  type: String, // 用于判断是添加还是编辑
  reload: Function // 添加或修改完后，刷新列表页
})

const formRef = ref(null)
const route = useRoute()
const state = reactive({
  visible: false,
  ruleForm: {
    name: '',
    merchant_id:''
  },
  rules: {
    name: [
      { required: 'true', message: '名称不能为空', trigger: ['change'] }
    ]
  },
  item:{
    name:'',
    type_id:'',
  }
})
// 获取详情
const getDetail = () => {
    state.ruleForm = {
      name: state.item.name
    }
}
// 开启弹窗
const open = (id,name) => {
  state.visible = true
  console.log(id)
  if (id) {
    state.item.type_id = id
    state.item.name = name
    // 如果是有 id 传入，证明是修改模式
    console.log(state.item)
    getDetail()
  }
}
// 关闭弹窗
const close = () => {
  state.visible = false
}
const submitForm = () => {
      if (props.type == 'add') {
        // 添加方法
        httpInstance.post('Merchant/add_type', {
          name: state.ruleForm.name,
          merchant_id: merchantStore.merchantInfo.userid
        }).then(() => {
          ElMessage.success('添加成功')
          state.visible = false
          // 接口回调之后，运行重新获取列表方法 reload
          if (props.reload) props.reload()
        })
      } else {
        // 修改方法
        httpInstance.post('/Merchant/change_type', {
          name: state.ruleForm.name,
          type_id: state.item.type_id
        }).then(() => {
          ElMessage.success('修改成功')
          state.visible = false
          // 接口回调之后，运行重新获取列表方法 reload
          if (props.reload) props.reload()
        })
      }
}
defineExpose({ open, close })
</script>