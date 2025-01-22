<template>
  <div class="tax-form-page">
    <form @submit.prevent="handleSubmit" class="form-container">
      <h1>Tax Information Form</h1>
      <p>
        Enter your gross income, possible expenses and other information
        regarding your tax situation.
      </p>
      <div class="form-group" v-for="(label, field) in formLabels" :key="field">
        <label :for="field">{{ label }}:</label>
        <div class="input-wrapper">
          <input
            v-if="field !== 'filingStatus' && field !== 'dependents'"
            type="number"
            :id="field"
            :step="0.01"
            :min="0"
            v-model.number="myData[field]"
          />
          <input
            v-else-if="field === 'dependents'"
            type="number"
            :id="field"
            :step="1"
            :min="0"
            v-model.number="myData[field]"
          />
          <select v-else :id="field" v-model="myData[field]" required>
            <option value="">Select</option>
            <option value="single">Single</option>
            <option value="marriedJoint">Married Joint</option>
            <option value="marriedSeparate">Married Separate</option>
          </select>
          <span
            v-if="field !== 'filingStatus' && field !== 'dependents'"
            class="currency-symbol"
            >€</span
          >
        </div>
      </div>
      <button type="submit">Submit</button>
    </form>

    <!-- Right Side OpenAI Advisor Section -->
    <div class="openai-advisor">
      <h2>Would you like some assistance from our OpenAI advisor?</h2>
      <textarea
        v-model="myData.userComments"
        placeholder="Add your comments or specific concerns here..."
      ></textarea>
      <button @click="askOpenAI">Ask Advisor</button>
    </div>

    <button class="back-button" @click="goHome">Back to Home</button>

    <!-- Modal -->
    <div v-if="showResultsModal" class="modal">
      <div class="modal-content">
        <h2>Tax Calculation Results</h2>
        <p><strong>Total Income:</strong> {{ results.totalIncome }} €</p>
        <p><strong>Deductions:</strong> {{ results.deductions }} €</p>
        <p><strong>Taxable Income:</strong> {{ results.taxableIncome }} €</p>
        <p><strong>Gross Tax:</strong> {{ results.grossTax }} €</p>
        <p><strong>Tax Withheld:</strong> {{ results.taxWithheld }} €</p>
        <p><strong>Tax Credit:</strong> {{ results.taxCredit }} €</p>
        <p><strong>Net Tax:</strong> {{ results.netTaxDue }} €</p>
        <button @click="closeResultsModal">Close</button>
      </div>
    </div>

    <!-- Modal for OpenAI Response -->
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
        businessProfits: "Buniness Profits",
        rentalIncome: "Rental Income",
        educationExpenses: "Education Expenses",
        businessExpenses: "Business Expenses",
        taxWithheld: "Tax Withheld",
        dependents: "Dependents",
      },
    };
  },
  computed: {
    // Process the advice for HTML rendering
    formattedAdvice() {
      return this.results.advice
        .replace(/\n/g, "<br>") // Replace newlines with <br>
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>") // Replace **text** with bold
        .replace(/: /g, ": <br>");
    },
  },
  methods: {
    async handleSubmit() {
      this.calculateTaxes();
    },
    async askOpenAI() {
      const apiUrl = "http://localhost:5000/tax-advice"; // Replace with your backend URL
      axios
        .post(apiUrl, this.myData)
        .then((response) => {
          this.results = response.data; // Store the API results
          this.showAIModal = true; // Open the second modal
        })
        .catch((error) => {
          console.error("Error generating AI answer:", error);
          alert("Failed to generate an answer. Please try again later.");
        });
    },
    calculateTaxes() {
      const apiUrl = "http://localhost:5000/calculate-tax"; // Replace with your backend URL
      axios
        .post(apiUrl, this.myData)
        .then((response) => {
          this.results = response.data; // Store the API results
          this.showResultsModal = true; // Open the second modal
        })
        .catch((error) => {
          console.error("Error calculating taxes:", error);
          alert("Failed to calculate taxes. Please try again later.");
        });
    },

    closeResultsModal() {
      this.showResultsModal = false;
    },
    closeAIModal() {
      this.showAIModal = false;
    },
    goHome() {
      this.$router.push("/");
    },
  },
};
</script>

<style>
html,
body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background-color: aquamarine; /* Ensure the background color covers the entire viewport */
}

#app {
  width: 100%;
  height: 100%;
}
</style>

<style scoped>
.tax-form-page {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin: 0 auto;
  width: 100%;
  min-height: 100%;
  flex-direction: column;
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
  margin-bottom: 0px;
}

.input-wrapper {
  position: relative;
  width: 100%;
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
select {
  align-self: center;
  font-size: 1.2em;
  padding: 10px;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  align-self: center;
  width: 150px;
  background-color: #55a713;
  color: white;
  font-size: 1.2em;
  padding: 10px 20px;
  margin-top: 10px;
  margin-bottom: 20px;
  border: none;
  border-radius: 25px;
  cursor: pointer;
}
button:hover {
  background-color: #0a6d17;
}
textarea {
  width: 100%;
  height: 100px;
  margin: 10px 0;
}
.form-container {
  display: flex;
  flex-direction: column;
  align-items: stretch;
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
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  align-items: center;
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
textarea {
  width: 100%;
  height: 200px;
  font-size: 1.5em;
}
textarea::placeholder {
  font-size: 1.1em; /* Adjust placeholder text size */
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
.modal {
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
.modal h2 {
  font-size: 1.6em;
}
.modal-content {
  background: white;
  margin: 7% auto;
  padding: 20px;
  border-radius: 8px;
  width: 90%;
  max-width: 500px;
  text-align: center;
}
.modal-content p {
  font-family: "Arial", sans-serif;
  font-size: 1.2em;
  line-height: 1.6;
  color: #333;
}
.modal-content h2 {
  margin-bottom: 15px;
}
.modal-content button {
  margin-top: 15px;
}
.signature {
  font-size: 0.8em;
  font-style: italic;
  position: fixed;
  right: 50px;
  bottom: 20px;
  color: #0e3606;
}
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
.ai-modal-content {
  background: white;
  margin: 7% auto;
  padding: 20px;
  border-radius: 8px;
  width: 90%;
  max-width: 1200px;
  text-align: justify;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.ai-modal-content p {
  font-family: "Arial", sans-serif;
  font-size: 1.2em;
  line-height: 1.6;
  color: #333;
}
.ai-modal-content h2 {
  text-align: center;
  margin-bottom: 15px;
}
.ai-modal-content button {
  margin-top: 15px;
}
</style>
