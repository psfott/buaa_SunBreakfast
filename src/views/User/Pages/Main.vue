<template>
  <el-card class="main">
    <!-- Centered and Styled Search Bar -->
    <div class="search-bar">
      <el-input
          v-model="searchKeyword"
          placeholder="搜索商家"
          class="small-search"
      ></el-input>
      <el-button type="primary" @click="search">搜索</el-button>
    </div>

    <div style="margin-left:1%;margin-right:1%">
      <el-row>
        <el-col :span="4" v-for="merchant in state.dataList " :key="merchant.id"  :offset="1">
          <div style="margin-top:15px">
            <el-card :body-style="{ padding: '0px'}" shadow="hover">
              <router-link :to="{ name: 'menu', params: { id: merchant.id } }">-->
                <img :src="merchant.image"/>
                <div class="txt1"> {{ merchant.name }}</div>
                <div class="txt2"> {{ merchant.address }}</div>
                <div class="txt3">{{ merchant.rating }}</div>
              </router-link>
            </el-card>
          </div>
        </el-col>
      </el-row>
      <div style="margin-left:35%">
        <div class="block">
          <el-pagination
              @current-change="changePage"
              :current-page ="state.current_page"
              :page-size="state.page_size"
              layout="total, prev, pager, next"
              :total="state.total" >
          </el-pagination>
        </div>
      </div>
    </div>
  </el-card>
</template>

<script setup>
import {onMounted, reactive} from "vue"

const state= reactive({
  searchKeyword: "", // Search keyword
  page_size: 10, // Number of merchants per page
  current_page: 1, // Current page number
  dataList: [
    {
      id: 1,
      name: "Merchant A",
      image: "merchant_a.jpg", // Replace with actual image path
      address: "123 Main St, City",
      rating: 4.2,
    },
    {
      id: 2,
      name: "Merchant B",
      image: "/merchant_b.jpg", // Replace with actual image path
      address: "456 Oak St, Town",
      rating: 4.8,
    },
    {
      id: 3,
      name: "Merchant C",
      image: "/merchant_c.jpg", // Replace with actual image path
      address: "789 Pine St, Village",
      rating: 4.5,
    },
    {
      id: 4,
      name: "Merchant D",
      image: "/merchant_d.jpg", // Replace with actual image path
      address: "101 Elm St, Hamlet",
      rating: 3.9,
    },
    {
      id: 5,
      name: "Merchant E",
      image: "/merchant_e.jpg", // Replace with actual image path
      address: "202 Maple St, Borough",
      rating: 4.1,
    },
    {
      id: 6,
      name: "Merchant F",
      image: "/merchant_f.jpg", // Replace with actual image path
      address: "303 Birch St, District",
      rating: 4.6,
    },
    {
      id: 7,
      name: "Merchant G",
      image: "/merchant_g.jpg", // Replace with actual image path
      address: "404 Cedar St, Township",
      rating: 4.3,
    },
    {
      id: 8,
      name: "Merchant H",
      image: "/merchant_h.jpg", // Replace with actual image path
      address: "505 Walnut St, County",
      rating: 4.7,
    },
  ],
  total:3
})

// onMounted(() => {
//   getCategory()
// })


// export default {
//   data() {
//     return {
//       searchKeyword: "", // Search keyword
//       pageSize: 4, // Number of merchants per page
//       currentPage: 1, // Current page number
//       dataList: [
//         {
//           id: 1,
//           name: "Merchant A",
//           image: "merchant_a.jpg", // Replace with actual image path
//           address: "123 Main St, City",
//           rating: 4.2,
//         },
//         {
//           id: 2,
//           name: "Merchant B",
//           image: "/merchant_b.jpg", // Replace with actual image path
//           address: "456 Oak St, Town",
//           rating: 4.8,
//         },
//         {
//           id: 3,
//           name: "Merchant C",
//           image: "/merchant_c.jpg", // Replace with actual image path
//           address: "789 Pine St, Village",
//           rating: 4.5,
//         },
//         {
//           id: 4,
//           name: "Merchant D",
//           image: "/merchant_d.jpg", // Replace with actual image path
//           address: "101 Elm St, Hamlet",
//           rating: 3.9,
//         },
//         {
//           id: 5,
//           name: "Merchant E",
//           image: "/merchant_e.jpg", // Replace with actual image path
//           address: "202 Maple St, Borough",
//           rating: 4.1,
//         },
//         {
//           id: 6,
//           name: "Merchant F",
//           image: "/merchant_f.jpg", // Replace with actual image path
//           address: "303 Birch St, District",
//           rating: 4.6,
//         },
//         {
//           id: 7,
//           name: "Merchant G",
//           image: "/merchant_g.jpg", // Replace with actual image path
//           address: "404 Cedar St, Township",
//           rating: 4.3,
//         },
//         {
//           id: 8,
//           name: "Merchant H",
//           image: "/merchant_h.jpg", // Replace with actual image path
//           address: "505 Walnut St, County",
//           rating: 4.7,
//         },
//         {
//           id: 9,
//           name: "Merchant I",
//           image: "/merchant_i.jpg", // Replace with actual image path
//           address: "606 Fir St, Municipality",
//           rating: 4.4,
//         },
//         {
//           id: 10,
//           name: "Merchant J",
//           image: "/merchant_j.jpg",
//           address: "503 Ps St, NewYork",
//           rating: 5.0,
//         }
//       ],
//
//       filteredMerchants: [],
//     };
//   },
//   created() {
//     this.search();
//   },
//   methods: {
//     search() {
//       // Handle search logic, e.g., navigate to search results page
//       const keyword = this.searchKeyword.toLowerCase();
//       this.filteredMerchants = this.recommendedMerchants_top.filter(
//           merchant => merchant.name.toLowerCase().includes(keyword));
//       console.log("Search Keyword:", this.searchKeyword);
//     },handlePageChange(newPage) {
//       this.currentPage = newPage;
//     },paginatedMerchants() {
//       const startIndex = (this.currentPage - 1) * this.pageSize;
//       const endIndex = startIndex + this.pageSize;
//       return this.filteredMerchants.slice(startIndex, endIndex);
//     },
//   },
// };
</script>

<style scoped>
.search-bar {
  margin: 20px auto; /* Center the search bar */
  text-align: center;
}

.small-search {
  width: 150px; /* Adjust the width as needed */
}

.merchant-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.merchant-merchant {
  margin: 10px;
  cursor: pointer;
  width: 100%; /* Adjust the width as needed */
}

.merchant-image {
  width: 100%; /* Make the image fill the container */
  height: 150px; /* Adjust as needed */
  border-radius: 8px;
  object-fit: cover;
}

.merchant-info {
  text-align: center;
  margin-top: 10px;
}

.merchant-info h3 {
  margin-bottom: 5px;
}

.pageDown {
  float: left;
  width: 60%;
  height: 60%;

}

.pageDown ul {
  list-style: none;
  height: 200px;
  margin-top: 0;
}

.pageDown ul li {
  text-align: center;
  background-color: #ffffff;
  float: left;
  margin-left: 10px;
  width: 200px;
  font-size: 13px;
  height: 215px;
  margin-bottom: 5px;
}

.pageDown ul li img {
  width: 90px;
  height: 150px;
}

.txt1{
  font-weight: 600;
  font-size: 17px;
}
.txt2{
  color: darkgrey;
  font-size: 10px;
}
.txt3{
  color: orangered;
}
.main {
  border-radius: 8px;
  margin: auto;
  height: 100%;
}
</style>
