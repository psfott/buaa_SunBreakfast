import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import Router from "./router/index.js";
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const app = createApp(App)

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

router.beforeEach((to, from, next) => {
    const isAuthenticated = false;

    if (to.meta.requiresAuth && !isAuthenticated) {
        // 如果用户未登录且访问需要登录的页面，则重定向到登录页面
        next('/login');
    } else {
        // 允许访问
        next();
    }
});
