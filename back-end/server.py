from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_cors import CORS
from openai import OpenAI

with open('C:/Users/simos/Documents/GitHub/Deloitte_Assignment/back-end/key.txt', 'r') as file:
    key = file.read()

client = OpenAI(
    api_key = key  # This is the default and can be omitted
)

app = Flask(__name__)                                                       #Initialize the flask application for the API
api = Api(app)
CORS(app)

'''Define request parser values and their properties for ADD, PUT, POST, DELETE requests'''
parsing_items = [
    "employmentIncome", 
    "pensionIncome", 
    "businessProfits", 
    "rentalIncome", 
    "investmentIncome", 
    "medicalExpenses", 
    "educationExpenses", 
    "businessExpenses", 
    "donations", 
    "taxWithheld"
]

rqp = reqparse.RequestParser()   
for item in parsing_items:                                       
    rqp.add_argument(item, type=float, default=0.0) 
rqp.add_argument("dependents", type=int, default=0)

advrqp = reqparse.RequestParser()               
advrqp.add_argument("userComments", type=str, default="")                           
advrqp.add_argument("filingStatus", type=str, choices=["single", "marriedJoint", "marriedSeparate"], required=True, help="Filing status is required")
for item in parsing_items:                                      
    advrqp.add_argument(item, type=float, default=0.0) 
advrqp.add_argument("dependents", type=int, default=0)

# Define the structure of the response using fields
tax_fields = {
    "totalIncome": fields.Float,
    "deductions": fields.Float,
    "taxableIncome": fields.Float,
    "tax": fields.Float,
    "taxCredit": fields.Float,
    "totalTax": fields.Float,
    "taxWithheld": fields.Float,
    "netTaxDue": fields.Float,
}

class TaxCalculator(Resource):

    @marshal_with(tax_fields)
    def cal_tax(self):
        try:
            args = rqp.parse_args()

            # Extract input data
            # Income data
            employment_income = args.get('employmentIncome')
            pension_income = args.get('pensionIncome')
            business_profits = args.get('businessProfits')
            rental_income = args.get('rentalIncome')
            investment_income = args.get('investmentIncome')
            # Expenses data
            medical_expenses = args.get('medicalExpenses')
            education_expenses = args.get('educationExpenses')
            business_expenses = args.get('businessExpenses')
            donations = args.get('donations')
            # Tax withheld data
            tax_withheld = args.get('taxWithheld')
            # Dependents data
            dependents = args.get('dependents')

            # Calculate total income
            total_income = (
                employment_income +
                pension_income +
                business_profits +
                rental_income +
                investment_income
            )

            # Deductible expenses
            deductions = (
                medical_expenses + 
                education_expenses + 
                business_expenses + 
                donations
            )
            taxable_income = max(0, total_income - deductions)

            # Calculate income tax
            if taxable_income <= 10000:
                tax = taxable_income * 0.09
            elif taxable_income <= 20000:
                tax = 10000 * 0.09 + (taxable_income - 10000) * 0.22
            elif taxable_income <= 30000:
                tax = 10000 * 0.09 + 10000 * 0.22 + (taxable_income - 20000) * 0.28
            else:
                tax = 10000 * 0.09 + 10000 * 0.22 + 10000 * 0.28 + (taxable_income - 30000) * 0.36

            # Apply tax credits
            base_credit = 1900
            if taxable_income > 12000:
                base_credit = max(0, base_credit - (taxable_income - 12000) * 0.1)
            credit_per_dependent = 50
            tax_credit = base_credit + (credit_per_dependent * dependents)

            # Final tax calculation
            total_tax = max(0, tax - tax_credit)

            # Calculate net tax due
            net_tax_due = max(0, total_tax - tax_withheld)
            
            # Response
            response = {
                "totalIncome": total_income,
                "deductions": deductions,
                "taxableIncome": taxable_income,
                "tax": tax,
                "taxCredit": tax_credit,
                "totalTax": total_tax,
                "taxWithheld": tax_withheld,
                "netTaxDue": net_tax_due
            }

            return response, 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def dispatch_request(self, *args, **kwargs):
        # Override dispatch_request to route to the appropriate method
        if request.method == 'POST':
            return self.cal_tax()                                    # Call custom method for DELETE requests
        else:
            return super(TaxCalculator, self).dispatch_request(*args, **kwargs)

class openAIAdvisor(Resource):

    def advgenerator(self):
        try:
            
            # Extract input data and comments
            tax_data = {k: v for k, v in advrqp.parse_args().items()}
            user_comments = tax_data.pop('userComments')
            # Format input for OpenAI
            prompt = generate_prompt(tax_data, user_comments)
            # Query OpenAI API
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a tax advisor. Provide practical suggestions."},     # The role gpt will play (tax advisor)
                    {"role": "user", "content": prompt}     # The user's input
                ],
                temperature=0.7,
                max_tokens=500
            )
            # Extract and return OpenAI response
            advice = response.choices[0].message.content   # Navigate through gpt's json response and get the content we need
            
            return {'advice': advice}, 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def dispatch_request(self, *args, **kwargs):
        # Override dispatch_request to route to the appropriate method
        if request.method == 'POST':
            return self.advgenerator()                                    # Call custom method for DELETE requests
        else:
            return super(openAIAdvisor, self).dispatch_request(*args, **kwargs)

api.add_resource(TaxCalculator, "/calculate-tax",
                methods=['POST']) 

api.add_resource(openAIAdvisor, "/tax-advice",
                methods=['POST']) 

def generate_prompt(tax_data, comments):
    """
    Formats the user input into a cohesive prompt for OpenAI.
    """
    tax_data_str = "\n".join([f"{k}: {v}" for k, v in tax_data.items()])
    if comments:
        return (
            f"Here is the user's tax-related data:\n{tax_data_str}\n\n"
            f"The user has also shared the following comments:\n{comments}\n\n"
            "Based on this information, please provide personalized suggestions and advice regarding their taxes."
        )
    return (
        f"Here is the user's tax-related data:\n{tax_data_str}\n\n"
        "Based on this information, please provide personalized suggestions and advice regarding their taxes."
    ) 

if __name__ == "__main__":

    print("Server starting up!")
    print(f"Ip: {'0.0.0.0'}, Port: 5000")
    from waitress import serve                                              
    serve(app, port=5000)    