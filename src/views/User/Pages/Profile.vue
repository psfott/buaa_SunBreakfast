<template>
  <div>
    <h1 class="page-title">个人中心</h1>

    <div class="profile-container">
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
</template>

<script>
export default {
  data() {
    return {
      userProfile: {
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
  text-align: center;
}

.profile-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f8f8f8;
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
