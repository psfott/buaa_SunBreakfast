// 路由文件
import { createRouter, createWebHistory } from "vue-router";

import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from "../views/Register.vue";
import ForgotPassword from "../views/ForgotPassword.vue";
import Merchant from "@/views/Merchant/index.vue";

const routes = [
    {
       path: '/',
       name: 'Home',
       component: Home
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/forgot-password',
        name: 'ForgotPassword',
        component: ForgotPassword
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
    {
        path: '/merchant',
        name: 'Merchant',
        component: Merchant,
        meta: { requiresAuth: true }
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
