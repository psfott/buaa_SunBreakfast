import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import Router from "./router/index.js";
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const app = createApp(App)

app.use(ElementPlus)

app.use(Router)
app.mount('#app')

// 注册 Element Plus 图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
