<template>
  <div>
    <h1>Welcome to the Tax Calculator</h1>
    <p>
      This tool helps you calculate your taxes efficiently. Navigate to the tax
      form to get started.
    </p>
    <router-link to="/tax-form">Go to Tax Form</router-link>
  </div>
</template>

<script>
export default {
  name: "HomePage",
};
</script>

<style scoped>
h1 {
  color: #333;
}
p {
  font-size: 1.2em;
  margin: 10px 0;
}
</style>
