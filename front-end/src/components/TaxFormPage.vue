<template>
  <div class="tax-form-page">
    <h1>Tax Information Form</h1>
    <form @submit.prevent="handleSubmit" class="form-container">
      <div class="form-group" v-for="(label, field) in formLabels" :key="field">
        <label :for="field">{{ label }}:</label>
        <input
          v-if="field !== 'filingStatus'"
          type="number"
          :id="field"
          v-model="formData[field]"
          :required="field !== 'otherIncome' && field !== 'taxCredits'"
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

    <!-- Modal -->
    <div v-if="showModal" class="modal-overlay">
      <div class="modal-content">
        <h2>Submission Summary</h2>
        <p v-for="(label, field) in formLabels" :key="field">
          <strong>{{ label }}:</strong> {{ formData[field] }}
        </p>
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
    handleSubmit() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    goHome() {
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
.tax-form-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 20px;
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
  background-color: #007bff;
  color: white;
  font-size: 1.2em;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}

.back-button {
  margin-top: 20px;
  position: fixed;
  top: 25px;
  left: 50px;
  background-color: #6c757d;
  font-size: 1em;
}
.back-button:hover {
  background-color: #5a6268;
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
