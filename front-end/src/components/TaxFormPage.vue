<template>
  <div class="tax-form-page">
    <h1>Tax Information Form</h1>
    <form @submit.prevent="handleSubmit" class="form-container">
      <div class="form-group" v-for="(label, field) in formLabels" :key="field">
        <label :for="field">{{ label }}:</label>
        <input
          v-if="field !== 'filingStatus' && field !== 'dependents'"
          type="number"
          :id="field"
          :step="0.01"
          :min="0"
          v-model.number="formData[field]"
          :required="field !== 'otherIncome' && field !== 'taxCredits'"
        />
        <input
          v-else-if="field == 'dependents'"
          type="number"
          :id="field"
          :step="1"
          :min="0"
          v-model.number="formData[field]"
        />
        <select v-else :id="field" v-model="formData[field]" required>
          <option value="">Select</option>
          <option value="single">Single</option>
          <option value="married">Married</option>
          <option value="headOfHousehold">Head of Household</option>
        </select>
      </div>
      <button type="submit">Submit</button>
    </form>

    <button class="back-button" @click="goHome">Back to Home</button>

    <!-- Modal 1-->
    <!-- <div v-if="showModal" class="modal-overlay">
      <div class="modal-content">
        <h2>Submission Summary</h2>
        <p v-for="(label, field) in formLabels" :key="field">
          <strong>{{ label }}:</strong> {{ formData[field] }}
        </p>
        <button @click="closeModal">Close</button>
      </div>
    </div> -->
    <!-- Modal 2-->
    <div v-if="showResultsModal" class="modal-overlay">
      <div class="modal-content">
        <h2>Tax Calculation Results</h2>
        <p><strong>Taxable Income:</strong> {{ results.taxableIncome }}</p>
        <p><strong>Tax:</strong> {{ results.tax }}</p>
        <p><strong>Tax Owed:</strong> {{ results.taxOwed }}</p>
        <p><strong>Refund:</strong> {{ results.refund }}</p>
        <button @click="closeResultsModal">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "TaxFormPage",
  data() {
    return {
      formData: {
        income: 0.0,
        expenses: 0.0,
        filingStatus: "",
        dependents: 0,
        withholding: 0.0,
        otherIncome: 0.0,
        taxCredits: 0.0,
      },
      // showModal: false,
      showResultsModal: false,
      results: {},
      formLabels: {
        income: "Income",
        expenses: "Expenses",
        filingStatus: "Filing Status",
        dependents: "Number of Dependents",
        withholding: "Tax Withholding",
        otherIncome: "Other Income",
        taxCredits: "Tax Credits",
      },
    };
  },
  methods: {
    async handleSubmit() {
      // this.showModal = true;
      this.calculateTaxes();
    },
    calculateTaxes() {
      const apiUrl = "http://localhost:5000/calculate-tax"; // Replace with your backend URL
      axios
        .post(apiUrl, this.formData)
        .then((response) => {
          this.results = response.data; // Store the API results
          this.showResultsModal = true; // Open the second modal
        })
        .catch((error) => {
          console.error("Error calculating taxes:", error);
          alert("Failed to calculate taxes. Please try again later.");
        });
    },
    // closeModal() {
    //   this.showModal = false;
    // },
    closeResultsModal() {
      this.showResultsModal = false;
    },
    goHome() {
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
.tax-form-page {
  margin: auto;
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  background-color: aquamarine;
}
h1 {
  font-size: 2.5em;
  margin-bottom: 30px;
}
.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  width: 100%;
  max-width: 600px;
}
.form-group {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 100%;
}
label {
  font-size: 1.2em;
  margin-bottom: 5px;
}
input,
select {
  font-size: 1.2em;
  padding: 10px;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 5px;
}
button {
  background-color: #55a713;
  color: white;
  font-size: 1.2em;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
button:hover {
  background-color: #0a6d17;
}

.back-button {
  margin-top: 20px;
  position: fixed;
  top: 25px;
  left: 50px;
  color: black;
  background-color: #accebe;
  font-size: 1em;
}
.back-button:hover {
  background-color: #8eaa9d;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}
.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 90%;
  max-width: 500px;
  text-align: center;
}
.modal-content h2 {
  margin-bottom: 15px;
}
.modal-content button {
  margin-top: 15px;
}
</style>
