<template>
  <div class="home-page">
    <h1>My Tax Calculator</h1>
    <p class="text1">
      Calculate your taxes fast and efficiently. Get suggestions and advice from
      our AI powered advisor.
    </p>
    <h2>Explanation of Each Input Item for the Tax Calculator</h2>
    <ul class="ul1">
      <li>
        Income Sources:
        <ul class="ul2">
          <li>Employment Income: Salaries and wages.</li>
          <li>Pension Income: Retirement benefits.</li>
          <li>
            Business Profits: Income from self-employment or business
            activities.
          </li>
          <li>Rental Income: Earnings from property rentals.</li>
          <li>Investment Income: Dividends, interest, etc.</li>
        </ul>
      </li>
      <li>
        Deductions and Allowances:
        <ul class="ul3">
          <li>Medical Expenses: Certain medical costs may be deductible.</li>
          <li>Education Expenses: Tuition fees for dependent children.</li>
          <li>
            Donations: Charitable contributions to approved organizations.
          </li>
        </ul>
      </li>
      <li>
        Filing Status: Options include Single, Married Filing Jointly, or
        Married Filing Separately.
      </li>
      <li>Tax Withheld: Total tax already withheld from income sources.</li>
      <li>
        Dependents: Number of dependents, such as children, which can affect tax
        calculations.
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
.home-page {
  background-color: #accebe;
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
  margin-top: 50px;
  margin-bottom: 0px;
  color: #333;
}
.text1 {
  margin-top: 70px;
  font-size: 1.5em;
  color: #000000;
}
h2 {
  margin-top: 10px;
  margin-bottom: 0px;
  color: #333;
}
.ul1 {
  margin-top: 30px;
  margin-bottom: 0px;
  font-size: 1.5em;
  color: #000000;
}
.ul2 {
  margin-top: 10px;
  margin-bottom: 0px;
  font-size: 1.1em;
  color: #000000;
}
.ul3 {
  margin-top: 10px;
  margin-bottom: 0px;
  font-size: 1.1em;
  color: #000000;
}
li {
  margin-top: 0px;
  margin-bottom: 10px;
  font-size: 0.9em;
  text-align: left;
  color: #000000;
}
.help-text {
  margin-top: 20px;
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
