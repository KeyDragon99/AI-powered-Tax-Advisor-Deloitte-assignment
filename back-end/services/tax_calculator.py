def calculate_tax(args):
    # Extract input data
    filing_status = args.get('filingStatus')
    employment_income = args.get('employmentIncome', 0.0)
    pension_income = args.get('pensionIncome', 0.0)
    business_profits = args.get('businessProfits', 0.0)
    rental_income = args.get('rentalIncome', 0.0)
    education_expenses = args.get('educationExpenses', 0.0)
    business_expenses = args.get('businessExpenses', 0.0)
    tax_withheld = args.get('taxWithheld', 0.0)
    dependents = args.get('dependents', 0)

    # Calculations
    total_income = employment_income + pension_income + business_profits + rental_income
    deductions = education_expenses + business_expenses
    taxable_income = max(0, total_income - deductions)

    brackets = [(10000, 0.09), (10000, 0.22), (10000, 0.28), (10000, 0.36), (float('inf'), 0.44)]
    gross_tax = 0
    remaining_income = taxable_income
    for bracket, rate in brackets:
        if remaining_income > bracket:
            gross_tax += bracket * rate
            remaining_income -= bracket
        else:
            gross_tax += remaining_income * rate
            break

    tax_credit = 0
    if filing_status != "single" or dependents > 0:
        tax_credit = 777 + [33, 123, 243, 563, 0][min(4, dependents)-1]
        if dependents > 4:
            tax_credit += 220 * (dependents - 4)

    net_tax_due = max(0, gross_tax - tax_withheld - tax_credit)

    return {
        "totalIncome": total_income,
        "deductions": deductions,
        "taxableIncome": taxable_income,
        "grossTax": gross_tax,
        "taxWithheld": tax_withheld,
        "taxCredit": tax_credit,
        "netTaxDue": net_tax_due,
    }
