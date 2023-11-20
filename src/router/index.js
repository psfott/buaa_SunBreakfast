// 路由文件
import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path: '/home',
        name: 'home',
        component: () => import(/* webpackChunkName: "login" */ '../views/Home.vue')
    },
    {
        path: '/login',
        name: 'login',
        component: () => import(/* webpackChunkName: "login" */ '../views/Login.vue')
    }

]

const router = createRouter({
    history: createWebHistory(),
    routes
})


router.beforeEach((to,from)=>{
    // if(to.meta.requireAuth) {
    //     let token = localStorage.getItem('auth-system-token');
    //     let isLogin = localStorage.getItem('auth-system-login');
    //     if(!token||!isLogin){
    //         return {
    //             path: '/login'
    //         }
    //     }
    // }
})

export default router;
