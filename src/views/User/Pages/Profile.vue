<template>
  <div>
    <!-- Move the title to the left top corner -->
    <h1 class="page-title">个人中心</h1>

    <!-- Create a container for user profile with an avatar -->
    <div class="profile-container">

      <!-- User Details -->
      <div class="profile-details">
        <!-- Add your user avatar image source -->
        <img src="userProfile.image"  class="avatar-image"/>
        <div class="profile-item">
          <div class="label">姓名:</div>
          <div class="value">{{ userProfile.name }}</div>
        </div>

        <div class="profile-item">
          <div class="label">学号:</div>
          <div class="value">{{ userProfile.studentId }}</div>
        </div>

        <div class="profile-item">
          <div class="label">居住地址:</div>
          <div class="value">{{ userProfile.address }}</div>
        </div>

        <div class="profile-item">
          <div class="label">电话号:</div>
          <div class="value">{{ userProfile.phoneNumber }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Avatar from "../../../assets/images/user_avatar.jpg"
export default {
  data() {
    return {
      userProfile: {
        img: Avatar,
        name: "Psfott",
        studentId: "21371158",
        address: "大运村5号楼, 0410C",
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
