<!--todo: 确认订单之后的逻辑-->

<template>
  <div>
    <el-container class="container">
      <!-- Top Bar -->
      <el-header class="top-bar">
        <router-link to="/user/main">
          <el-icon class="back-to-home" style="color: black;">
            <ArrowLeft/>
          </el-icon>
          <span class="back-to-home-text">返回首页</span>
        </router-link>
        <h1 class="page-title">{{ restaurantName }} Menu</h1>
      </el-header>

      <el-container>
        <el-aside class="side-bar">
          <el-menu
              default-active="recommend"
              background-color="#f4f4f5"
              text-color="#5e5e5e"
              active-text-color="#67c23a"
          >
            <el-menu-item
                index="recommend"
                @click="changeCategory('recommend')"
            >
              菜品推荐
            </el-menu-item>
            <el-menu-item
                index="mainDish"
                @click="changeCategory('mainDish')"
            >
              主食
            </el-menu-item>
            <el-menu-item
                index="sideDish"
                @click="changeCategory('sideDish')"
            >
              配菜
            </el-menu-item>
            <el-menu-item
                index="drink"
                @click="changeCategory('drink')"
            >
              饮品
            </el-menu-item>
          </el-menu>
        </el-aside>

        <el-container class="content">
          <el-main class="main-content">
            <ul class="dish-list">
              <li v-for="(dish, index) in filteredMenu" :key="index" class="dish-item">
                <!-- Dish Image -->
                <img :src="dish.image" alt="Dish Image" class="dish-image">

                <!-- Dish Details -->
                <div class="dish-details">
                  <h3>{{ dish.name }}</h3>
                  <ul>
                    <li>价格: {{ dish.price }}</li>
                    <li>类别: {{ dish.category }}</li>
                  </ul>

                  <!-- Input for selecting quantity -->
                  <div class="quantity-input">
                    <input v-model="quantities[index]" type="number" min="0" placeholder="数量">
                    <!-- "加入购物车" button -->
                    <button @click="addToCart(index)">加入购物车</button>
                  </div>
                </div>
              </li>
            </ul>
          </el-main>

          <!-- Circular button for shopping cart -->
          <div class="cart-button" @click="toggleCart">
            <el-icon class="cart-icon">
              <ShoppingCart/>
            </el-icon>
          </div>

          <!-- Modal/Dialog for shopping cart items -->
          <div v-if="showCart" class="cart-modal">
            <!-- Cart items go here -->
            <div v-for="(item, index) in cart" :key="index" class="cart-item">
              <p>{{ item.restaurantName }} - {{ item.name }} - 数量: {{ item.quantity }} - 小计: {{
                  item.totalPrice
                }}</p>
            </div>

            <!-- Confirm Order button -->
            <button @click="confirmOrder">确认订单</button>
            <button @click="clearCart" class="clear-cart-button">清空购物车</button>
          </div>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import {ArrowLeft, ShoppingCart} from "@element-plus/icons-vue";
import {ref, watch} from "vue";
import {useRouter} from 'vue-router';
import {ElMessage} from "element-plus";
import baoziImage from '../../../assets/images/dishes/baozi.png';
import youtiaoImage from '../../../assets/images/dishes/youtiao.png';

export default {
  components: {ShoppingCart, ArrowLeft},
  data() {
    return {
      isFullWidth: false,
      restaurantName: 'Merchant A',
      menu: [
        {name: '菜品1', price: 10, image: baoziImage, category: 'mainDish'},
        {name: '菜品2', price: 15, image: youtiaoImage, category: 'mainDish'},
        // Add more dishes as needed
      ],
      quantities: Array.from({length: 10}, () => 0), // Initialize quantities array
      orderConfirmed: false,
      cart: [],
      showCart: false, // Toggle to show/hide cart modal
      filteredMenu: [],
    };
  },
  methods: {
    confirmOrder() {
      this.orderConfirmed = true;
      this.showCart = !this.showCart;
      ElMessage({type: 'success',message: '订单已发送<br><br>五秒后自动返回首页', dangerouslyUseHTMLString: true })
      setTimeout(() => {
        this.$router.push('/user/main');
      }, 5000);
    },
    addToCart(index) {
      const quantity = this.quantities[index];
      if (quantity > 0) {
        const selectedDish = {
          restaurantName: this.restaurantName, // Add restaurant name to the cart item
          ...this.menu[index],
          quantity,
          totalPrice: quantity * this.menu[index].price,
        };
        this.cart.push(selectedDish);
        // Optional: You can clear the quantity input after adding to the cart
        this.quantities[index] = 0;
      }
    },
    toggleCart() {
      this.showCart = !this.showCart;
    },
    clearCart() {
      this.cart = [];
      this.showCart = !this.showCart;
    },
    changeCategory(category) {
      this.activeMenu = category;
      this.filterMenu(category);
    },
    filterMenu(category) {
      // Assuming you have a 'category' property in each dish object
      this.filteredMenu = this.menu.filter((dish) => dish.category === category);
    },
  },
};
</script>

<style scoped>
.page-title {
  text-align: center;
  flex-grow: 1; /* Allow the page title to take up remaining space */
  margin: 0; /* Remove default margin */
}

.back-to-home {
  margin: 10px;
}

.top-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  border-bottom: 1px solid #ccc;
}

.side-bar {
  width: 200px;
  height: 100%;
  background-color: #f2f2f2;
}

.main-content {
  flex-grow: 1;
  display: flex;
  align-items: stretch; /* Update this line to stretch */
  justify-content: flex-start;
  padding: 20px;
}

.dish-item {
  margin-bottom: 20px;
}

.dish-image {
  width: 150px;
  height: 150px;
  border-radius: 8px;
  object-fit: cover;
  //height: auto; /* 保持图像的纵横比 */
}

.clear-cart-button {
  margin-left: 150px;
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.main-content {
  height: calc(100vh - 100px);
  overflow: auto;
  padding: 10px;
}

.content {
  display: flex;
  flex-direction: column;
  max-height: 100vh;
  overflow: hidden;
}


.cart-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #3498db; /* Button background color */
  border-radius: 50%; /* Make it circular */
  padding: 10px;
  cursor: pointer;
}

.cart-icon {
  width: 30px;
  height: 30px;
}

.cart-modal {
  justify-content: space-between;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  z-index: 1000;
}

.cart-item {
  margin-bottom: 10px;
}

button {
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.container {
  height: 100vh;
}

.quantity-input {
  width: 150px;
}
</style>
