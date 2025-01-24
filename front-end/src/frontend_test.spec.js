import { createRouter, createWebHistory } from "vue-router";
import { render, screen, fireEvent } from "@testing-library/vue";
import { describe, expect } from "vitest";
import "@testing-library/jest-dom";
import TaxFormPage from "@/components/TaxFormPage.vue";
import HomePage from "@/components/HomePage.vue";

// Mock Router
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "Home", component: HomePage },
    { path: "/tax-form", name: "TaxForm", component: TaxFormPage },
  ],
});

describe("HomePage.vue", () => {
  test("renders static content correctly", () => {
    render(HomePage, { global: { plugins: [router] } });

    // Check main heading
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent(
      "My Tax Calculator"
    );

    // Check explanation of tax inputs
    expect(screen.getByRole("heading", { level: 2 })).toHaveTextContent(
      "Explanation of Each Input Item for the Tax Calculator"
    );

    // Check help text
    expect(
      screen.getByText("Navigate to the tax form to get started.")
    ).toBeInTheDocument();

    // Check signature
    expect(screen.getByText("Made by Giazitzis Symeon")).toBeInTheDocument();
  });

  test("displays input explanations in a list", () => {
    render(HomePage, { global: { plugins: [router] } });

    // Check for list items in the explanation
    expect(screen.getByText("Employment Income:")).toBeInTheDocument();
    expect(
      screen.getByText("Tuition fees for dependent children.")
    ).toBeInTheDocument();
    expect(
      screen.getByText("Number of dependents, such as children.")
    ).toBeInTheDocument();
  });

  test("navigates to the tax form when the button is clicked", async () => {
    render(HomePage, { global: { plugins: [router] } });

    const button = screen.getByRole("button", { name: "Go to Tax Form" });
    await fireEvent.click(button);

    // Wait for navigation to complete
    await router.isReady();

    // Verify navigation to the /tax-form route
    expect(router.currentRoute.value.path).toBe("/tax-form");
  });
});

describe("TaxFormPage.vue", () => {
  test("initial state is correct", () => {
    render(TaxFormPage);

    expect(
      screen.queryByText("Tax Calculation Results")
    ).not.toBeInTheDocument();
    expect(
      screen.queryByText("OpenAI Advisor's Suggestions")
    ).not.toBeInTheDocument();

    const employmentInput = screen.getByLabelText("Employment Income:");
    expect(employmentInput).toHaveValue(0);
  });

  test("updates myData when form fields are changed", async () => {
    render(TaxFormPage);

    const employmentInput = screen.getByLabelText("Employment Income:");
    await fireEvent.update(employmentInput, "1234.56");

    expect(employmentInput).toHaveValue(1234.56);
  });

  test("closeResultsModal sets showResultsModal to false", async () => {
    // Render the component with initial data
    const { getByRole, queryByText } = render(TaxFormPage, {
      data() {
        return {
          showResultsModal: true,
          results: {
            totalIncome: 10000.0,
            deductions: 2000.0,
            taxableIncome: 8000.0,
            grossTax: 1500.0,
            taxWithheld: 1300.0,
            taxCredit: 200.0,
            netTaxDue: 0.0,
          },
        };
      },
    });

    // Check that the modal is initially in the document
    expect(screen.getByText("Tax Calculation Results")).toBeInTheDocument();

    // Find and click the close button
    const closeButton = getByRole("button", { name: "Close" });
    await fireEvent.click(closeButton);

    // Check that the modal is no longer in the document
    expect(queryByText("Tax Calculation Results")).not.toBeInTheDocument();
  });

  test("Setting calculation modal to true makes it appear", async () => {
    // Render the component with initial data
    render(TaxFormPage, {
      data() {
        return {
          showResultsModal: true,
          results: {
            totalIncome: 10000.0,
            deductions: 2000.0,
            taxableIncome: 8000.0,
            grossTax: 1500.0,
            taxWithheld: 1300.0,
            taxCredit: 200.0,
            netTaxDue: 0.0,
          },
        };
      },
    });

    // Check that the modal is initially in the document
    expect(screen.getByText("Tax Calculation Results")).toBeInTheDocument();
  });
});
