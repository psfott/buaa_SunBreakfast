<template>
  <div class="rider-profile">
    <!-- Rider Avatar -->
    <div class="avatar-container">
      <img :src="riderProfile.avatar" alt="Rider Avatar" class="avatar-image">
    </div>

    <!-- Rider Information -->
    <div class="info-container">
      <div class="info-item">
        <div class="label">骑手ID:</div>
        <div class="value">{{ riderProfile.id }}</div>
      </div>

      <div class="info-item">
        <div class="label">电话号码:</div>
        <div class="value">{{ riderProfile.phoneNumber }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      riderProfile: {
        id: "123456", // Replace with actual rider ID
        phoneNumber: "15526664444", // Replace with actual phone number
        avatar: "rider_avatar.jpg", // Replace with actual image path
        // Add more rider details as needed
      },
    };
  },
};
</script>

<style scoped>
.rider-profile {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f8f8f8;
  display: flex;
}

.avatar-container {
  flex: 1;
}

.avatar-image {
  width: 100%; /* Make the image fill the container */
  border-radius: 50%;
}

.info-container {
  flex: 2;
  padding-left: 20px;
}

.info-item {
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
