<!--todo: 确认订单之后的逻辑-->

<template>
  <el-container>
    <!-- Top Bar -->
    <el-header class="top-bar">
      <router-link to="/user/main">
        <el-icon class="back-to-home" style="color: black;"><ArrowLeft /></el-icon>
        <span class="back-to-home-text">返回首页</span>
      </router-link>
      <h1 class="page-title">{{ restaurantName }} Menu</h1>
    </el-header>


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

    <el-container>
    <el-main class="main-content">
      <div v-for="(dish, index) in filteredMenu" :key="index" class="dish-item">
        <!-- Dish Image -->
        <img :src="dish.image" alt="Dish Image" class="dish-image">

        <!-- Dish Details -->
        <div class="dish-details">
          <h3>{{ dish.name }}</h3>
          <p>价格: {{ dish.price }}</p>
          <p>类别: {{ dish.category }}</p>

          <!-- Input for selecting quantity -->
          <div class="quantity-input">
            <input v-model="quantities[index]" type="number" min="0" placeholder="数量">
            <!-- "加入购物车" button -->
            <button @click="addToCart(index)">加入购物车</button>
          </div>
        </div>
      </div>
    </el-main>

    <!-- Circular button for shopping cart -->
      <div class="cart-button" @click="toggleCart">
        <el-icon  class="cart-icon"><ShoppingCart /></el-icon>
      </div>

    <!-- Modal/Dialog for shopping cart items -->
      <div v-if="showCart" class="cart-modal">
      <!-- Cart items go here -->
        <div v-for="(item, index) in cart" :key="index" class="cart-item">
          <p>{{ item.restaurantName }} - {{ item.name }} - 数量: {{ item.quantity }} - 小计: {{ item.totalPrice }}</p>
        </div>

        <el-dialog v-if="orderConfirmed" title="Order Confirmation" :visible.sync="orderConfirmed">
          <p>下单成功！</p>
        </el-dialog>
      <!-- Confirm Order button -->
        <button @click="confirmOrder">确认订单</button>
        <button @click="clearCart" class="clear-cart-button">清空购物车</button>
      </div>
    </el-container>
  </el-container>

</template>

<script>
import {ArrowLeft, ShoppingCart} from "@element-plus/icons-vue";
import { useStore } from 'vuex';
import {ref, watch} from "vue";
import { useRouter } from 'vue-router';

export default {
  components: {ShoppingCart, ArrowLeft },
  setup() {
    const store = useStore();

    // Reactivity for order confirmation
    const orderConfirmed = ref(false);

    // Watch for changes in order confirmation and reset it
    watch(orderConfirmed, (newVal) => {
      if (newVal) {
        // Reset the confirmation state after a delay (e.g., 3 seconds)
        setTimeout(() => {
          orderConfirmed.value = false;
        }, 3000);
      }
    });

    // ... existing setup code ...

    return {
      // ... existing returned values ...
      orderConfirmed,
    };
  },
  data() {
    return {
      isFullWidth: false,
      restaurantName: 'Merchant A',
      menu: [
        { name: '菜品1', price: 10,image: '../../../assets/images/dishes/baozi.png',category: 'mainDish'},
        { name: '菜品2', price: 15,image: '../../../assets/images/dishes/youtiao.png',category: 'mainDish' },
        // Add more dishes as needed
      ],
      quantities: Array.from({ length: 10 }, () => 0), // Initialize quantities array
      cart: [],
      showCart: false, // Toggle to show/hide cart modal
      filteredMenu: [],
    };
  },
  methods: {
    async confirmOrder() {
      // ... existing code ...

      // Mocking a successful order confirmation
      this.orderConfirmed = true;

      // Clear the cart or perform any other necessary actions

      // Redirect to Order Details page
      const router = useRouter();
      router.push({ name: 'order-details', params: { orderId: '123' } });

      // Dispatch an action to add the order to ongoing orders in Vuex store
      await this.$store.dispatch('addOngoingOrder', {
        orderId: '123',
        // other order details
      });
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
  padding: 10px;
  border-bottom: 1px solid #ccc;
}
.side-bar {
  width: 200px;
  padding: 20px;
}

.main-content {
  flex-grow: 1;
  display: flex;
  align-items: stretch; /* Update this line to stretch */
  justify-content: center;
  padding: 20px;
}
.dish-item {
  margin-bottom: 20px;
}

.clear-cart-button {
  margin-left: 150px;
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.main-content {
  flex-grow: 1;
  padding: 20px;
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
</style>
