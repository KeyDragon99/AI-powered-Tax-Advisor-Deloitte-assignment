<template>
  <div class="home-page">
    <h1>My Tax Calculator</h1>
    <p class="text1">
      Calculate your taxes fast and efficiently. Get suggestions and advice from
      our AI powered advisor.
    </p>
    <p class="help-text">Navigate to the tax form to get started.</p>
    <p class="signature">Made by Giazitzis Symeon</p>
    <button class="tax-form-button" @click="gotaxform">Go to Tax Form</button>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  methods: {
    gotaxform() {
      this.$router.push("/tax-form");
    },
  },
};
</script>

<style scoped>
.home-page {
  background-color: rgb(172, 206, 190);
  margin: auto;
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 0px;
}
h1 {
  font-size: 2.5em;
  margin-top: 100px;
  color: #333;
}
.text1 {
  margin-top: 100px;
  font-size: 1.5em;
  color: #000000;
}
.help-text {
  margin-top: 70px;
  margin-bottom: 0px;
  font-size: 1.5em;
  color: #000000;
}
.signature {
  font-size: 0.8em;
  font-style: italic;
  position: fixed;
  right: 50px;
  bottom: 20px;
  color: #0e3606;
}
.tax-form-button {
  background-color: #55a713;
  color: white;
  font-size: 1.2em;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 13px;
}
.tax-form-button:hover {
  background-color: #0a6d17;
}
</style>
