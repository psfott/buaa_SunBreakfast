import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import Router from "./router/index.js";
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import {localGet} from "@/utils";
const app = createApp(App)
const pinia = createPinia()
// 注册持久化插件
pinia.use(piniaPluginPersistedstate)
app.use(pinia)
app.use(ElementPlus)
app.use(Router)
app.mount('#app')
//全局注册Element Icon
for (let iconName in ElementPlusIconsVue) {
    app.component(iconName, ElementPlusIconsVue[iconName])
}
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
