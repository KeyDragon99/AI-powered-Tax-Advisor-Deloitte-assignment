<template>
  <div>
    <h1>Tax Information Form</h1>
    <form @submit.prevent="handleSubmit">
      <div>
        <label for="income">Income:</label>
        <input type="number" id="income" v-model="formData.income" required />
      </div>
      <div>
        <label for="expenses">Expenses:</label>
        <input
          type="number"
          id="expenses"
          v-model="formData.expenses"
          required
        />
      </div>
      <div>
        <label for="filingStatus">Filing Status:</label>
        <select id="filingStatus" v-model="formData.filingStatus" required>
          <option value="">Select</option>
          <option value="single">Single</option>
          <option value="married">Married</option>
          <option value="headOfHousehold">Head of Household</option>
        </select>
      </div>
      <div>
        <label for="dependents">Number of Dependents:</label>
        <input
          type="number"
          id="dependents"
          v-model="formData.dependents"
          min="0"
          required
        />
      </div>
      <div>
        <label for="withholding">Tax Withholding:</label>
        <input
          type="number"
          id="withholding"
          v-model="formData.withholding"
          required
        />
      </div>
      <div>
        <label for="otherIncome">Other Income:</label>
        <input type="number" id="otherIncome" v-model="formData.otherIncome" />
      </div>
      <div>
        <label for="taxCredits">Tax Credits:</label>
        <input type="number" id="taxCredits" v-model="formData.taxCredits" />
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "TaxFormPage",
  data() {
    return {
      formData: {
        income: "",
        expenses: "",
        filingStatus: "",
        dependents: 0,
        withholding: "",
        otherIncome: "",
        taxCredits: "",
      },
    };
  },
  methods: {
    handleSubmit() {
      console.log("Form Data:", this.formData);
      alert(
        `Income: ${this.formData.income}\nExpenses: ${this.formData.expenses}\nFiling Status: ${this.formData.filingStatus}\nDependents: ${this.formData.dependents}\nWithholding: ${this.formData.withholding}\nOther Income: ${this.formData.otherIncome}\nTax Credits: ${this.formData.taxCredits}`
      );
    },
  },
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}
label {
  font-weight: bold;
}
button {
  background-color: #007bff;
  color: white;
  padding: 10px;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
</style>
