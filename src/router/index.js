// 路由文件
import { createRouter, createWebHistory } from "vue-router";

import Home from '../views/Home.vue'
import MerchantLogin from '../views/Merchant/MerchantLogin.vue'
import MerchantRegister from "../views/Merchant/MerchantRegister.vue";
import ForgotPassword from "../views/ForgotPassword.vue";
import Merchant from "@/views/Merchant/index.vue";
import UserProfile from "../views/User/Pages/Profile.vue"
import Main from "@/views/User/Pages/Main.vue";
import Ongoing from "@/views/User/Pages/Ongoing.vue";
import Finished from "@/views/User/Pages/Finished.vue";
import Menu from "@/views/User/Pages/OrderMeal.vue"
import AddProduct from "../views/Merchant/AddProduct.vue";
import MerchantIntro from "@/views/Merchant/MerchantIntro.vue";
import MerchantFood from "@/views/Merchant/Foods.vue";
import MerchantFoodCategory from "@/views/Merchant/FoodCategory.vue";
import MerchantAccount from "@/views/Merchant/MerchantAccount.vue";
import MerchantOrder from "@/views/Merchant/MerchantOrder.vue";
import MerchantOrderDetail from "@/views/Merchant/MerchantOrderDetail.vue";
import user from "@/views/User/index.vue";
import UserLogin  from "@/views/User/UserLogin.vue";
import UserRegister from "@/views/User/UserRegister.vue";

const routes = [
    {
       path: '/',
       name: 'Home',
       component: Home
    },
    {
        path: '/merchantLogin',
        name: 'MerchantLogin',
        component: MerchantLogin
    },
    {
        path: '/merchantRegister',
        name: 'MerchantRegister',
        component: MerchantRegister
    },
    {
        path: '/userLogin',
        name: 'UserLogin',
        component: UserLogin
    },
    {
        path: '/userRegister',
        name: 'userRegister',
        component: UserRegister
    },
    {
        path: '/forgot-password',
        name: 'ForgotPassword',
        component: ForgotPassword
    },

    {
        path: '/merchant',
        name: 'Merchant',
        component: Merchant
    },
    {
        path: '/user',
        name: 'user',
        component: user, //使用布局组件
        redirect: '/user/main',
        meta: {requiresAuth: true},
        children: [
            {   path:'/user/profile', component: UserProfile, meta: { requiresAuth: true }  },
            {   path:'/user/main', component: Main, meta: { requiresAuth: true }    },
            {   path: '/user/ongoing', component: Ongoing, meta: { requiresAuth: true } },
            {   path: '/user/finished', component: Finished, meta: { requiresAuth: true } }
        ]
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
        path: '/menu/:id',
        name: 'menu',
        component: Menu,
        props: true,
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
