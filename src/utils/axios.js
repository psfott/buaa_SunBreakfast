import axios from 'axios'
import {ElMessage, ElMessageBox} from 'element-plus'
import router from '@/router/index'
import { localGet } from './index'


const httpInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  timeout: 5000
})

httpInstance.defaults.headers['Content-Type'] = 'multipart/form-data'
// 请求头，headers 信息
// axios.defaults.headers['X-Requested-With'] = 'XMLHttpRequest'
// // axios.defaults.headers['token'] = localGet('token') || ''
// // 默认 post 请求，使用 application/json 形式
// axios.defaults.headers.post['Content-Type'] = 'multipart/form-data'

httpInstance.interceptors.request.use(config => {
  // 设置请求头
  // config.headers['Content-Type'] = 'application/x-www-form-urlencoded'

  // 1. 从 pinia 获取 token 数据
  // const userStore = useUserStore()
  // const username = userStore.userInfo.username
  // const token = userStore.userInfo.authorization
  // if (username && token) {
  //   config.data = config.data || {}
  //   config.data.username = username
  //   config.data.authorization = token
  // }
  return config
}, e => Promise.reject(e))


// 请求拦截器，内部根据返回值，重新组装，统一管理。
httpInstance.interceptors.response.use(function (res){
  if (res.data.error !== 0) {
    // 统一错误提示

    if (res.data.error === 401 || res.data.error === 402) {
      console.log(1)
      ElMessageBox.confirm(
          '该操作需要先完成登录~',
          '提示',
          {
            confirmButtonText: '去登录',
            cancelButtonText: '取消',
            type: 'warning',
          }
      )
          .then(() => {
            console.log(1)
            router.push({ path: 'merchant/login' })
          })
          .catch(() => {
            ElMessage({
              type: 'info',
              message: '取消',
            })
          })
    }
    ElMessage({
      type: 'warning',
      message: res.data.msg
    })

    return Promise.reject(res)
  }
  else {
    console.log("请求成功")
    // ElMessage({
    //   type: 'success',
    //   message: res.data.msg
    // })
    return res.data
  }
})

export default httpInstance