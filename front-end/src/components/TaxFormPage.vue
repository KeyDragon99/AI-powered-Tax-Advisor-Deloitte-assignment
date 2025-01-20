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
      </div>
      <button type="submit">Submit</button>
    </form>

    <!-- Right Side OpenAI Advisor Section -->
    <div class="openai-advisor">
      <h3>Would you like some assistance from our OpenAI advisor?</h3>
      <textarea
        v-model="myData.userComments"
        placeholder="Add your comments or specific concerns here..."
      ></textarea>
      <button @click="askOpenAI">Ask Advisor</button>
    </div>

    <button class="back-button" @click="goHome">Back to Home</button>

    <!-- Modal 1-->
    <!-- <div v-if="showModal" class="modal-overlay">
      <div class="modal-content">
        <h2>Submission Summary</h2>
        <p v-for="(label, field) in formLabels" :key="field">
          <strong>{{ label }}:</strong> {{ myData[field] }}
        </p>
        <button @click="closeModal">Close</button>
      </div>
    </div> -->
    <!-- Modal 2-->
    <div v-if="showResultsModal" class="modal">
      <div class="modal-content">
        <h2>Tax Calculation Results</h2>
        <p><strong>Total Income:</strong> {{ results.totalIncome }}</p>
        <p><strong>Deductions:</strong> {{ results.deductions }}</p>
        <p><strong>Taxable Income:</strong> {{ results.taxableIncome }}</p>
        <p><strong>Tax:</strong> {{ results.tax }}</p>
        <p><strong>Tax Credit:</strong> {{ results.taxCredit }}</p>
        <p><strong>Total Tax:</strong> {{ results.totalTax }}</p>
        <p><strong>Tax Withheld:</strong> {{ results.taxWithheld }}</p>
        <p><strong>Net Tax:</strong> {{ results.netTaxDue }}</p>
        <button @click="closeResultsModal">Close</button>
      </div>
    </div>

    <!-- Modal for OpenAI Response -->
    <div v-if="showAIModal" class="modal">
      <div class="modal-content">
        <h2>OpenAI Advisor's Suggestions</h2>
        <p v-html="formattedAdvice"></p>
        <button @click="closeAIModal">Close</button>
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
      myData: {
        userComments: "",
        filingStatus: "",
        employmentIncome: 0.0,
        pensionIncome: 0.0,
        businessProfits: 0.0,
        rentalIncome: 0.0,
        investmentIncome: 0.0,
        medicalExpenses: 0.0,
        educationExpenses: 0.0,
        businessExpenses: 0.0,
        donations: 0.0,
        taxWithheld: 0.0,
        dependents: 0,
      },
      // showModal: false,
      showAIModal: false,
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
        businessExpenses: "Business Expenses",
        donations: "Donations",
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
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>"); // Replace **text** with bold
    },
  },
  methods: {
    async handleSubmit() {
      // this.showModal = true;
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

    // closeModal() {
    //   this.showModal = false;
    // },
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

.openai-advisor {
  width: 30%;
  margin-left: 20px;
}
textarea {
  width: 100%;
  height: 100px;
  margin: 10px 0;
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
  font-size: 20px;
  line-height: 1.6;
  color: #333;
}
.modal-content h2 {
  margin-bottom: 15px;
}
.modal-content button {
  margin-top: 15px;
}
</style>
