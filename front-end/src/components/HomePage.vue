<template>
  <div class="home-page">
    <h1>My Tax Calculator</h1>
    <p class="text1">
      Calculate your taxes fast and efficiently. Get suggestions and advice from
      our AI powered advisor.
    </p>
    <h2>Explanation of Each Input Item for the Tax Calculator</h2>
    <ul>
      <li>
        Income: The total gross income earned by the user, including salaries,
        wages, bonuses, etc.
      </li>
      <li>
        Expenses: Allowable deductions or business expenses that reduce taxable
        income, such as rent, utilities, or supplies.
      </li>
      <li>
        Filing Status: The user’s tax filing status (e.g., single, married, head
        of household). This impacts tax brackets and standard deductions.
      </li>
      <li>
        Number of Dependents: The number of dependents (e.g., children or
        relatives) the user claims, which can affect tax credits or deductions.
      </li>
      <li>
        Tax Withholding: The amount of income tax already withheld from the
        user’s paychecks throughout the year.
      </li>
      <li>
        Other Income: Additional income not included in gross income, such as
        interest, dividends, or rental income.
      </li>
      <li>
        Tax Credits: Direct reductions of tax liability, such as credits for
        education or child care.
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
  margin-top: 50px;
  margin-bottom: 0px;
  color: #333;
}
ul {
  margin-top: 30px;
  margin-bottom: 0px;
  font-size: 1.2em;
  color: #000000;
}
li {
  margin-top: 0px;
  margin-bottom: 10px;
  font-size: 1em;
  text-align: left;
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
