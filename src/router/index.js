// 路由文件
import { createRouter, createWebHistory } from "vue-router";

import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from "../views/Register.vue";
import ForgotPassword from "../views/ForgotPassword.vue";
import Merchant from "@/views/Merchant/index.vue";
import {localGet} from "@/utils";
import AddProduct from "../views/Merchant/AddProduct.vue";
import MerchantIntro from "@/views/Merchant/MerchantIntro.vue";
import User from "../views/User/index.vue"
import MerchantFood from "@/views/Merchant/Foods.vue";
import MerchantFoodCategory from "@/views/Merchant/FoodCategory.vue";
import MerchantAccount from "@/views/Merchant/MerchantAccount.vue";
import MerchantOrder from "@/views/Merchant/MerchantOrder.vue";
import MerchantOrderDetail from "@/views/Merchant/MerchantOrderDetail.vue";

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
        name: 'merchant',
        component: Merchant,
        redirect:'/merchant/intro',
        meta: { requiresAuth: true },
        children: [
            { path: '/merchant/add', component: AddProduct, meta: { requiresAuth: true } },
            { path: '/merchant/intro', component: MerchantIntro, meta: { requiresAuth: true } },
            { path: '/merchant/foods', component: MerchantFood, meta: { requiresAuth: true } },
            { path: '/merchant/category', component: MerchantFoodCategory, meta: { requiresAuth: true } },
            { path: '/merchant/account', component: MerchantAccount, meta: { requiresAuth: true } },
            { path: '/merchant/order', component: MerchantOrder, meta: { requiresAuth: true } },
            { path: '/merchant/order_detail', component: MerchantOrderDetail, meta: { requiresAuth: true } }
        ]
    },
    {
        path: '/user',
        name: 'User',
        component: User
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

// router.beforeEach((to, from, next) => {
//     if (to.path === '/login') {
//         // 如果路径是 /login 则正常执行
//         next()
//     } else {
//         // 如果不是 /login，判断是否有 token
//         if (!localGet('token')) {
//             // 如果没有，则跳至登录页面
//             next({ path: '/login' })
//         } else {
//             // 否则继续执行
//             next()
//         }
//     }
//     state.currentPath = to.path
//     document.title = pathMap[to.name]
// })
export default router;
