<template>
  <div class="search-bar">
    <el-input
        v-model="searchKeyword"
        placeholder="搜索商家"
        class="small-search"
    ></el-input>
    <el-button type="primary" @click="search">搜索</el-button>
  </div>
  <el-row>
    <el-col v-for="(item, index) in state.filterMerchants" :key="index" :span="6">
      <router-link :to="{ name: 'menu', params: { id: item.id } }">
      <el-card :body-style="{ padding: '0px' }" class="card">
        <img :src="item.image" class="image"/>
        <div style="padding: 14px">
          <span>{{ item.name }}</span>
          <div class="bottom">
            <time class="time">{{ item.date }}</time>
            <el-button text class="button">Operating</el-button>
          </div>
        </div>
      </el-card>
      </router-link>
    </el-col>

    <!-- 分页器 -->
    <el-pagination
        class="pagination"
        v-model=state.current_page
        :page-size=state.page_size
        :total=state.total
        @current-change="handlePageChange"
    ></el-pagination>
  </el-row>
</template>

<script lang="ts" setup>
import {ref,reactive} from 'vue';


const currentDate = ref(new Date());
const itemsPerPage = 8; // 每页显示的项目数
const allItems = [
  {name: 'Yummy hamburger 1', id:1,date: currentDate.value, image: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png'},
  {name: 'Yummy hamburger 2', id:2,date: currentDate.value, image: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png'},
  {name: 'Yummy hamburger 3', id:3,date: currentDate.value, image: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png'},
  {name: 'Yummy hamburger 4', id:4,date: currentDate.value, image: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png'},
  {name: 'Yummy hamburger 5', id:5,date: currentDate.value, image: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png'},
  {name: 'Yummy hamburger 6', id:6,date: currentDate.value, image: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png'},
  {name: 'Yummy hamburger 7', id:7,date: currentDate.value, image: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png'},
  {name: 'Yummy hamburger 8', id:8,date: currentDate.value, image: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png'},
  {name: 'Yummy hamburger 9', id:9,date: currentDate.value, image: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png'},
  // 其他项目...
];
const state = reactive({
  searchKeyword: '',
  page_size: itemsPerPage,
  current_page: 1,
  dataList: allItems,
  total: allItems.length,
  filterMerchants: allItems,
});

const totalItems = ref(allItems.length);


const updatePaginatedItems = () => {
  const startIndex = (state.current_page - 1) * state.page_size;
  const endIndex = startIndex + state.page_size;
  state.filterMerchants = state.dataList.slice(startIndex, endIndex);
};

// 初始化调用一次
updatePaginatedItems();

// 监听currentPage的变化，更新paginatedItems
const handlePageChange = () => {
  updatePaginatedItems();
};

</script>

<style>
.search-bar {
  margin: 20px auto;
  text-align: center;
}

.time {
  font-size: 12px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 0;
  min-height: auto;
}

.image {
  width: 100%; /* 或者设置一个合适的宽度，高度为auto */
  display: block;
}

.card {
  width: 200px; /* 调整卡片的宽度 */
  margin: 10px; /* 添加一些边距 */
}

.pagination {
  margin-top: 20px;
  margin-left: 450px;
  display: flex;
  justify-content: center;
}

.small-search {
  width: 150px;
}
</style>





<!--<template>-->
<!--  <el-card class="main">-->
<!--    &lt;!&ndash; Centered and Styled Search Bar &ndash;&gt;-->
<!--    <div class="search-bar">-->
<!--      <el-input-->
<!--          v-model="searchKeyword"-->
<!--          placeholder="搜索商家"-->
<!--          class="small-search"-->
<!--      ></el-input>-->
<!--      <el-button type="primary" @click="search">搜索</el-button>-->
<!--    </div>-->

<!--    <el-row>-->
<!--      <el-col :span="4" v-for="merchant in state.filterMerchants" :key="merchant.id" :offset="1">-->
<!--        <div style="margin-top:15px">-->
<!--          <el-card :body-style="{ padding: '0px' }">-->
<!--            <router-link :to="{ name: 'menu', params: { id: merchant.id } }">-->
<!--              <img src="/logo.png" class="merchant-image"/>-->
<!--              <div class="txt1"> {{ merchant.name }}</div>-->
<!--              <div class="txt2"> {{ merchant.address }}</div>-->
<!--              <div class="txt3">{{ merchant.rating }}</div>-->
<!--            </router-link>-->
<!--          </el-card>-->
<!--        </div>-->
<!--      </el-col>-->
<!--    </el-row>-->

<!--    <div class="block">-->
<!--      <el-pagination-->
<!--          @current-change="changePage"-->
<!--          :current-page="state.current_page"-->
<!--          :page-size="state.page_size"-->
<!--          layout="total, prev, pager, next"-->
<!--          :total="state.total">-->
<!--      </el-pagination>-->
<!--    </div>-->
<!--  </el-card>-->
<!--</template>-->

<!--<script setup>-->
<!--import {ref,onMounted, reactive} from "vue"-->

<!--const searchKeyword = ref(""); // Search keyword-->
<!--const page_size = 8; // Number of merchants per page-->
<!--const current_page = ref(1); // Current page number-->

<!--const dataList = [-->
<!--  {-->
<!--    id: 1,-->
<!--    name: "Merchant A",-->
<!--    image: "merchant_a.jpg", // Replace with actual image path-->
<!--    address: "123 Main St, City",-->
<!--    rating: 4.2,-->
<!--  },-->
<!--  {-->
<!--    id: 2,-->
<!--    name: "Merchant B",-->
<!--    image: "/merchant_b.jpg", // Replace with actual image path-->
<!--    address: "456 Oak St, Town",-->
<!--    rating: 4.8,-->
<!--  },-->
<!--  {-->
<!--    id: 3,-->
<!--    name: "Merchant C",-->
<!--    image: "/merchant_c.jpg", // Replace with actual image path-->
<!--    address: "789 Pine St, Village",-->
<!--    rating: 4.5,-->
<!--  },-->
<!--  {-->
<!--    id: 4,-->
<!--    name: "Merchant D",-->
<!--    image: "/merchant_d.jpg", // Replace with actual image path-->
<!--    address: "101 Elm St, Hamlet",-->
<!--    rating: 3.9,-->
<!--  },-->
<!--  {-->
<!--    id: 5,-->
<!--    name: "Merchant E",-->
<!--    image: "/merchant_e.jpg", // Replace with actual image path-->
<!--    address: "202 Maple St, Borough",-->
<!--    rating: 4.1,-->
<!--  },-->
<!--  {-->
<!--    id: 6,-->
<!--    name: "Merchant F",-->
<!--    image: "/merchant_f.jpg", // Replace with actual image path-->
<!--    address: "303 Birch St, District",-->
<!--    rating: 4.6,-->
<!--  },-->
<!--  {-->
<!--    id: 7,-->
<!--    name: "Merchant G",-->
<!--    image: "/merchant_g.jpg", // Replace with actual image path-->
<!--    address: "404 Cedar St, Township",-->
<!--    rating: 4.3,-->
<!--  },-->
<!--  {-->
<!--    id: 8,-->
<!--    name: "Merchant H",-->
<!--    image: "/merchant_h.jpg", // Replace with actual image path-->
<!--    address: "505 Walnut St, County",-->
<!--    rating: 4.7,-->
<!--  },-->
<!--];-->


<!--const total = ref(3);-->

<!--const state = reactive({-->
<!--  searchKeyword,-->
<!--  page_size,-->
<!--  current_page,-->
<!--  dataList,-->
<!--  total,-->
<!--  filterMerchants: dataList,-->
<!--});-->

<!--onMounted(() => {-->
<!--  console.log("Data list on mounted:", dataList);-->
<!--  state.filterMerchants = dataList;-->
<!--  search();-->
<!--})-->

<!--const search = () => {-->
<!--  // Handle search logic, e.g., navigate to search results page-->
<!--  const keyword = searchKeyword.value.toLowerCase();-->
<!--  state.filterMerchants = state.dataList.filter(-->
<!--      (merchant) => merchant.name.toLowerCase().includes(keyword)-->
<!--  );-->
<!--  console.log("Search Keyword:", searchKeyword.value);-->
<!--  console.log("filterMerchant:", state.filterMerchants);-->
<!--  console.log("dataList:", state.dataList);-->
<!--  console.log("paginatedMerchants", paginatedMerchants());-->
<!--  console.log("Filter Merchants on Search:", state.filterMerchants);-->
<!--};-->

<!--const changePage = (newPage) => {-->
<!--  current_page.value = newPage;-->
<!--};-->

<!--const paginatedMerchants = () => {-->
<!--  const startIndex = (current_page.value - 1) * page_size;-->
<!--  const endIndex = startIndex + page_size;-->
<!--  return state.filterMerchants.slice(startIndex, endIndex);-->
<!--};-->

<!--</script>-->

<!--<style scoped>-->
<!--.search-bar {-->
<!--  margin: 20px auto; /* Center the search bar */-->
<!--  text-align: center;-->
<!--}-->

<!--.small-search {-->
<!--  width: 150px; /* Adjust the width as needed */-->
<!--}-->

<!--.merchant-list {-->
<!--  display: flex;-->
<!--  flex-wrap: wrap;-->
<!--  justify-content: space-around;-->
<!--}-->

<!--.merchant-merchant {-->
<!--  margin: 10px;-->
<!--  cursor: pointer;-->
<!--  width: 100%; /* Adjust the width as needed */-->
<!--}-->

<!--.merchant-image {-->
<!--  width: 100%; /* Make the image fill the container */-->
<!--  display: block;-->

<!--}-->

<!--.merchant-info {-->
<!--  text-align: center;-->
<!--  margin-top: 10px;-->
<!--}-->

<!--.merchant-info h3 {-->
<!--  margin-bottom: 5px;-->
<!--}-->

<!--.pageDown {-->
<!--  float: left;-->
<!--  width: 60%;-->
<!--  height: 60%;-->

<!--}-->

<!--.pageDown ul {-->
<!--  list-style: none;-->
<!--  height: 200px;-->
<!--  margin-top: 0;-->
<!--}-->

<!--.pageDown ul li {-->
<!--  text-align: center;-->
<!--  background-color: #ffffff;-->
<!--  float: left;-->
<!--  margin-left: 10px;-->
<!--  width: 200px;-->
<!--  font-size: 13px;-->
<!--  height: 215px;-->
<!--  margin-bottom: 5px;-->
<!--}-->

<!--.pageDown ul li img {-->
<!--  width: 90px;-->
<!--  height: 150px;-->
<!--}-->

<!--.block {-->
<!--  align-content: center;-->
<!--  margin-left: 35%;-->
<!--}-->

<!--.txt1 {-->
<!--  font-weight: 600;-->
<!--  font-size: 17px;-->
<!--}-->

<!--.txt2 {-->
<!--  color: darkgrey;-->
<!--  font-size: 10px;-->
<!--}-->

<!--.txt3 {-->
<!--  color: orangered;-->
<!--}-->

<!--.main {-->
<!--  border-radius: 8px;-->
<!--  margin: auto;-->
<!--  height: 120%;-->
<!--}-->

<!--.merchant-item {-->
<!--  height: 80px;-->
<!--  width: 80px;-->
<!--}-->
<!--</style>-->
