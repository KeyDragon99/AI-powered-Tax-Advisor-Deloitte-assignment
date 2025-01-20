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
          :required="
            field !== 'otherIncome' &&
            field !== 'taxCredits' &&
            !(
              field === 'employmentIcome' ||
              field === 'pensionIncome' ||
              field === 'businessProfits'
            ) &&
            field !== 'rentalIncome' &&
            field !== 'investmentIncome' &&
            field !== 'medicalExpenses' &&
            field !== 'educationExpenses' &&
            field !== 'donations' &&
            field !== 'taxWithheld'
          "
        />
        <input
          v-else-if="field === 'dependents'"
          type="number"
          :id="field"
          :step="1"
          :min="0"
          v-model.number="formData[field]"
        />
        <select v-else :id="field" v-model="formData[field]" required>
          <option value="">Select</option>
          <option value="single">Single</option>
          <option value="marriedJoint">Married</option>
          <option value="marriedSeparate">Head of Household</option>
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
        filingStatus: "",
        employmentIncome: 0.0,
        pensionIncome: 0.0,
        businessProfits: 0.0,
        rentalIncome: 0.0,
        investmentIncome: 0.0,
        medicalExpenses: 0.0,
        educationExpenses: 0.0,
        donations: 0.0,
        taxWithheld: 0.0,
        dependents: 0,
      },
      // showModal: false,
      showResultsModal: false,
      results: {},
      formLabels: {
        filingStatus: "Filing Status",
        employmentIncome: "Employment Income",
        pensionIncome: "Pension Income",
        businessProfits: "Buniness Profits",
        rentalIncome: "Rental Income",
        investmentIncome: "Investment Income",
        medicalExpenses: "Medical Expenses",
        educationExpenses: "Education Expenses",
        donations: "Donations",
        taxWithheld: "Tax Withheld",
        dependents: "Dependents",
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
  width: 100%;
  height: 100%;
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
  gap: 15px;
  width: 100%;
  max-width: 500px;
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
  margin-bottom: 50px;
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
