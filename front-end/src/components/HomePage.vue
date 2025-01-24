<template>
  <div class="home-page">
    <h1>My Tax Calculator</h1>
    <p class="text1">
      Calculate your taxes fast and efficiently. Get suggestions and advice from
      our AI-powered advisor.
    </p>

    <h2>Explanation of Each Input Item for the Tax Calculator</h2>
    <ul class="input-explanation">
      <li>
        <strong>Income Sources:</strong>
        <ul class="nested-list">
          <li><strong>Employment Income:</strong> Salaries and wages.</li>
          <li><strong>Pension Income:</strong> Retirement benefits.</li>
          <li>
            <strong>Business Profits:</strong> Income from self-employment or
            business activities.
          </li>
          <li>
            <strong>Rental Income:</strong> Earnings from property rentals.
          </li>
        </ul>
      </li>
      <li>
        <strong>Deductions and Allowances:</strong>
        <ul class="nested-list">
          <li>
            <strong>Education Expenses:</strong> Tuition fees for dependent
            children.
          </li>
          <li>
            <strong>Business Expenses:</strong> Expenses made in benefit of a
            self-employed business are deductible.
          </li>
        </ul>
      </li>
      <li>
        <strong>Filing Status:</strong> Options include Single, Married Filing
        Jointly, or Married Filing Separately.
      </li>
      <li>
        <strong>Tax Withheld:</strong> Total tax already withheld from income
        sources.
      </li>
      <li>
        <strong>Dependents:</strong> Number of dependents, such as children.
      </li>
    </ul>

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
/* General Page Layout */
.home-page {
  background-color: #accebe;
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 0;
}

/* Header Styles */
h1 {
  font-size: 2.5em;
  margin: 50px 0 0;
  color: #333;
}

.text1 {
  margin-top: 55px;
  font-size: 1.8em;
  color: #000;
}

/* Explanation Section */
h2 {
  margin-top: 10px;
  color: #333;
}

.input-explanation {
  margin-top: 10px;
  margin-bottom: 0;
  font-size: 1.6em;
  color: #000;
  text-align: left;
}

.nested-list {
  margin-top: 10px;
  margin-bottom: 0;
  font-size: 1.1em;
  color: #000;
}

li {
  font-size: 0.95em;
  margin-bottom: 10px;
}

/* Footer and Button */
.help-text {
  margin-top: 20px;
  margin-bottom: 0px;
  font-size: 1.5em;
  color: #000;
}

.tax-form-button {
  background-color: #55a713;
  color: white;
  font-size: 1.2em;
  padding: 10px 20px;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  margin-top: 20px;
}

.tax-form-button:hover {
  background-color: #0a6d17;
}

.signature {
  font-size: 0.8em;
  font-style: italic;
  position: absolute;
  right: 50px;
  bottom: 20px;
  color: #0e3606;
}
</style>
