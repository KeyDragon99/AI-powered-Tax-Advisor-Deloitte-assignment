<template>
  <div class="tax-form-page">
    <!-- Tax Form Section -->
    <form @submit.prevent="handleSubmit" class="form-container">
      <h1>Tax Information Form</h1>
      <p>
        Enter your gross income, possible expenses, and other tax-related
        information.
      </p>

      <!-- Form Fields -->
      <div v-for="(label, field) in formLabels" :key="field" class="form-group">
        <label :for="field">{{ label }}:</label>
        <div class="input-wrapper">
          <template v-if="field === 'filingStatus'">
            <select :id="field" v-model="myData[field]" required>
              <option value="">Select</option>
              <option value="single">Single</option>
              <option value="marriedJoint">Married Joint</option>
              <option value="marriedSeparate">Married Separate</option>
            </select>
          </template>
          <template v-else>
            <input
              type="number"
              :id="field"
              :step="field === 'dependents' ? 1 : 0.01"
              :min="0"
              v-model.number="myData[field]"
            />
            <span v-if="field !== 'dependents'" class="currency-symbol">€</span>
          </template>
        </div>
      </div>

      <button type="submit">Submit</button>
    </form>

    <!-- OpenAI Advisor Section -->
    <div class="openai-advisor">
      <h2>Need assistance? Ask our AI tax advisor!</h2>
      <textarea
        v-model="myData.userComments"
        placeholder="Add your comments or concerns here..."
      ></textarea>
      <button @click="askOpenAI">Ask Advisor</button>
    </div>

    <!-- Navigation Button -->
    <button class="back-button" @click="goHome">
      <strong>Back to Home</strong>
    </button>

    <!-- Tax Calculation Results Modal -->
    <div v-if="showResultsModal" class="tax-modal">
      <div class="tax-modal-content">
        <h2>Tax Calculation Results</h2>
        <p>
          <strong>Total Income:</strong>
          {{ formatNumber(results.totalIncome) }} €
        </p>
        <p>
          <strong>Deductions:</strong> {{ formatNumber(results.deductions) }} €
        </p>
        <p>
          <strong>Taxable Income:</strong>
          {{ formatNumber(results.taxableIncome) }} €
        </p>
        <p>
          <strong>Gross Tax:</strong> {{ formatNumber(results.grossTax) }} €
        </p>
        <p>
          <strong>Tax Withheld:</strong>
          {{ formatNumber(results.taxWithheld) }} €
        </p>
        <p>
          <strong>Tax Credit:</strong> {{ formatNumber(results.taxCredit) }} €
        </p>
        <p>
          <strong>Net Tax Due:</strong> {{ formatNumber(results.netTaxDue) }} €
        </p>
        <button @click="closeResultsModal">Close</button>
      </div>
    </div>

    <!-- OpenAI Response Modal -->
    <div v-if="showAIModal" class="ai-modal">
      <div class="ai-modal-content">
        <h2>OpenAI Advisor's Suggestions</h2>
        <p v-html="formattedAdvice"></p>
        <button @click="closeAIModal">Close</button>
      </div>
    </div>

    <p class="signature">Made by Giazitzis Symeon</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "TaxFormPage",
  data() {
    return {
      myData: {
        userComments: "",
        filingStatus: "",
        employmentIncome: 0.0,
        pensionIncome: 0.0,
        businessProfits: 0.0,
        rentalIncome: 0.0,
        educationExpenses: 0.0,
        businessExpenses: 0.0,
        taxWithheld: 0.0,
        dependents: 0,
      },
      showAIModal: false,
      showResultsModal: false,
      results: {},
      formLabels: {
        filingStatus: "Filing Status",
        employmentIncome: "Employment Income",
        pensionIncome: "Pension Income",
        businessProfits: "Business Profits",
        rentalIncome: "Rental Income",
        educationExpenses: "Education Expenses",
        businessExpenses: "Business Expenses",
        taxWithheld: "Tax Withheld",
        dependents: "Dependents",
      },
    };
  },
  computed: {
    formattedAdvice() {
      return this.results.advice
        .replace(/\n/g, "<br>") // Replace newlines with <br>
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>") // Replace **text** with bold
        .replace(/: /g, ": <br>");
    },
  },
  methods: {
    handleSubmit() {
      this.calculateTaxes();
    },
    async askOpenAI() {
      try {
        const apiUrl = "http://localhost:5000/tax-advice";
        const response = await axios.post(apiUrl, this.myData);
        this.results = response.data;
        this.showAIModal = true;
      } catch (error) {
        console.error("Error generating AI answer:", error);
        alert("Failed to generate an answer. Please try again later.");
      }
    },
    async calculateTaxes() {
      try {
        const apiUrl = "http://localhost:5000/calculate-tax";
        const response = await axios.post(apiUrl, this.myData);
        this.results = response.data;
        this.showResultsModal = true;
      } catch (error) {
        console.error("Error calculating taxes:", error);
        alert("Failed to calculate taxes. Please try again later.");
      }
    },
    closeResultsModal() {
      this.showResultsModal = false;
    },
    closeAIModal() {
      this.showAIModal = false;
    },
    formatNumber(value) {
      return value.toFixed(2);
    },
    goHome() {
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
/* General Page Layout */
.tax-form-page {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin: 0 auto;
  width: 100%;
  min-height: 100vh;
  align-items: center;
  text-align: center;
  background-color: aquamarine; /* Ensure the background color covers the entire viewport */
}

h1 {
  font-size: 2.5em;
  margin-bottom: 5px;
}

label {
  text-align: left;
  font-size: 1.35em;
}

.form-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
  width: 100%;
  max-width: 450px;
  margin-left: 45%;
  margin-top: 5%;
}

.form-container p {
  font-size: 1.3em;
}

.form-group {
  display: grid;
  align-items: center;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: 100%;
}

.openai-advisor {
  display: flex;
  flex-direction: column;
  align-self: flex-start;
  align-items: stretch;
  width: 100%;
  max-width: 500px;
  margin-left: 20%;
  margin-top: 20%;
}

.input-wrapper {
  position: relative;
}

.currency-symbol {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.2em;
  color: #333;
}

input,
select,
textarea {
  align-self: center;
  font-size: 1.2em;
  padding: 10px;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 5px;
}

textarea {
  font-size: 1.5em;
  height: 200px;
  margin: 10px 0;
}

textarea::placeholder {
  font-size: 0.9em;
}

button {
  font-size: 1.2em;
  padding: 10px 20px;
  background-color: #55a713;
  color: white;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  align-self: center;
  width: 150px;
  margin-top: 10px;
  margin-bottom: 20px;
}

button:hover {
  background-color: #0a6d17;
}

.back-button {
  margin-top: 20px;
  position: fixed;
  height: auto;
  width: auto;
  top: 25px;
  left: 50px;
  color: black;
  background-color: #accebe;
  font-size: 1.1em;
}

.back-button:hover {
  background-color: #8eaa9d;
}

/* Modal Styles */
.tax-modal,
.ai-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1000;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
  display: block;
  justify-content: center;
  align-items: center;
}

.tax-modal h2 {
  font-size: 1.6em;
}

.tax-modal-content,
.ai-modal-content {
  background: white;
  margin: 7% auto;
  padding: 20px;
  border-radius: 8px;
  width: 90%;
  max-width: 500px;
  text-align: center;
}

.tax-modal-content p,
.ai-modal-content p {
  font-family: "Arial", sans-serif;
  font-size: 1.2em;
  line-height: 1.6;
  color: #333;
}

.tax-modal-content h2,
.ai-modal-content h2 {
  text-align: center;
  margin-bottom: 15px;
}

.tax-modal-content button,
.ai-modal-content button {
  margin-top: 15px;
}

.ai-modal-content {
  max-width: 1200px;
  text-align: justify;
  display: flex;
  flex-direction: column;
  align-items: center;
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
