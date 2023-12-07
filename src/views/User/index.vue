<template>
  <Layout>
    <!-- Home 页面的内容 -->
    <template v-slot:default>
      <router-view></router-view>
    </template>

    <template v-slot:profile>
      <Profile />
    </template>

    <template v-slot:finished>
      <Finished />
    </template>

    <template v-slot:ongoing>
      <Ongoing />
    </template>
  </Layout>
</template>

<script>

import Main from "@/views/User/Pages/Main.vue";
import Profile from "@/views/User/Pages/Profile.vue";
import Layout from "@/views/User/Pages/Layout.vue";
import Finished from "@/views/User/Pages/Finished.vue";
import Ongoing from "@/views/User/Pages/Ongoing.vue";

export default {
  components: {
    Layout,
    Main,
    Profile,
    Finished,
    Ongoing
  },
};
</script>


<style scoped>


.logo img {
  height: 40px;
  width: auto;
}


.merchant-item img {
  width: 200px; /* Adjust as needed */
  height: 150px; /* Adjust as needed */
  border-radius: 8px;
  object-fit: cover;
}

.merchant-item h3 {
  margin-top: 10px;
}
/* 根据需要添加更多样式 */
</style>
