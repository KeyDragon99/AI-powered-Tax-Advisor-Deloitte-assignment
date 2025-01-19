<template>
  <div class="home-page">
    <h1>My Tax Calculator</h1>
    <p class="text1">
      Calculate your taxes fast and efficiently. Get suggestions and advice from
      our AI powered advisor.
    </p>
    <p class="help-text">Navigate to the tax form to get started.</p>
    <button><router-link to="/tax-form">Go to Tax Form</router-link></button>
    <p class="signature">Made by Giazitzis Symeon</p>
  </div>
</template>

<script>
export default {
  name: "HomePage",
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
  position: fixed;
  top: 70px;
  color: #333;
  margin: 50px;
}
.text1 {
  position: fixed;
  font-size: 1.5em;
  top: 300px;
  color: #000000;
}
.help-text {
  position: fixed;
  font-size: 1.5em;
  top: 400px;
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
button {
  background-color: #55a713;
  position: fixed;
  color: white;
  font-size: 1.2em;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  top: 480px;
  cursor: pointer;
}
button:hover {
  background-color: #0a6d17;
}
</style>
