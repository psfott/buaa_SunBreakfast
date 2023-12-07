<template>
  <div>
    <!-- Centered and Styled Search Bar -->
    <div class="search-bar">
      <el-input
          v-model="searchKeyword"
          placeholder="搜索商家"
          class="small-search"
      ></el-input>
      <el-button type="primary" @click="search">搜索</el-button>
    </div>

    <!-- Recommended Merchants (Two Columns, Three Rows) -->
    <div class="merchant-list">
      <div v-for="merchant in recommendedMerchants" :key="merchant.id" class="merchant-item">
        <router-link :to="{ name: 'menu', params: { id: merchant.id } }">
        <img :src="merchant.image" alt="Merchant Image" class="merchant-image">
        <div class="merchant-info">
          <h3>{{ merchant.name }}</h3>
          <p>Address: {{ merchant.address }}</p>
          <p>Rating: {{ merchant.rating }}/5</p>
        </div>
        </router-link>
      </div>
    </div>

  </div>

</template>

<script>
export default {
  data() {
    return {
      searchKeyword: "", // Search keyword
      recommendedMerchants: [
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
        {
          id: 9,
          name: "Merchant I",
          image: "/merchant_i.jpg", // Replace with actual image path
          address: "606 Fir St, Municipality",
          rating: 4.4,
        },
        {
          id: 10,
          name: "Merchant J",
          image: "/merchant_j.jpg",
          address: "503 Ps St, NewYork",
          rating: 5.0,
        }
      ],

    };
  },
  methods: {
    search() {
      // Handle search logic, e.g., navigate to search results page
      console.log("Search Keyword:", this.searchKeyword);
    },
  },
};
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

.merchant-item {
  margin: 10px;
  cursor: pointer;
  width: 200px; /* Adjust the width as needed */
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

</style>
