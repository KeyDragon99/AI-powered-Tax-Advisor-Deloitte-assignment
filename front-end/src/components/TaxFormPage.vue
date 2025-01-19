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

    <!-- Modal -->
    <div v-if="showModal" class="modal-overlay">
      <div class="modal-content">
        <h2>Submission Summary</h2>
        <p><strong>Income:</strong> {{ formData.income }}</p>
        <p><strong>Expenses:</strong> {{ formData.expenses }}</p>
        <p><strong>Filing Status:</strong> {{ formData.filingStatus }}</p>
        <p><strong>Dependents:</strong> {{ formData.dependents }}</p>
        <p><strong>Withholding:</strong> {{ formData.withholding }}</p>
        <p><strong>Other Income:</strong> {{ formData.otherIncome }}</p>
        <p><strong>Tax Credits:</strong> {{ formData.taxCredits }}</p>
        <button @click="closeModal">Close</button>
      </div>
    </div>
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
      showModal: false,
    };
  },
  methods: {
    handleSubmit() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
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
