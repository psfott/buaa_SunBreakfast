<template>
  <div>
    <!-- Move the title to the left top corner -->
    <h1 class="page-title">个人中心</h1>

    <!-- Create a container for user profile with an avatar -->
    <div class="profile-container">

      <!-- User Details -->
      <div class="profile-details">
        <!-- Add your user avatar image source -->
        <img :src="riderProfile.image"  class="avatar-image" alt="">
        <div class="profile-item">
          <div class="label">姓名:</div>
          <div class="value">{{ riderProfile.name }}</div>
        </div>

        <div class="profile-item">
          <div class="label">骑手ID:</div>
          <div class="value">{{ riderProfile.studentId }}</div>
        </div>


        <div class="profile-item">
          <div class="label">电话号:</div>
          <div class="value">{{ riderProfile.phoneNumber }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Avatar from '../../../assets/images/user_avatar.jpg'
export default {
  data() {
    return {
      riderProfile: {
        img: Avatar,
        name: "Psfott",
        studentId: "001",
        phoneNumber: "15526664444",
        // Add more user details as needed
      },
    };
  },
};
</script>

<style scoped>
.page-title {
  text-align: left;
  margin-top: 10px; /* Adjust the margin as needed */
  margin-left: 10px; /* Adjust the margin as needed */
}

.profile-container {
  display: flex;
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f8f8f8;
}


.avatar-image {
  width: 100px; /* Adjust the width as needed */
  height: 100px; /* Adjust the height as needed */
  margin-bottom: 25px;
  border-radius: 50%;
}

.profile-details {
  flex: 1;
}

.profile-item {
  display: flex;
  margin-bottom: 10px;
}

.profile-item .value {
  width: 100px;
}

.label {
  font-weight: bold;
  margin-right: 10px;
  flex: 1;
}

.value {
  flex: 2;
  border: 1px solid #ddd;
  padding: 8px;
  border-radius: 4px;
  background-color: #fff;
}
</style>
