import tkinter as tk
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_restful import marshal
from flask_cors import CORS
from datetime import datetime as dt
import os.path, threading, requests, sys, signal, time, socket

app = Flask(__name__)                                                       #Initialize the flask application for the API
api = Api(app)
CORS(app)

'''Define request parser values and their properties for ADD, PUT, POST, DELETE requests'''
rqp = reqparse.RequestParser()                                          
rqp.add_argument("filingStatus", type=str, choices=["single", "marriedJoint", "marriedSeparate"], required=True, help="Filing status is required")
rqp.add_argument("employmentIncome", type=float, default=0.0)
rqp.add_argument("pensionIncome", type=float, default=0.0)
rqp.add_argument("businessProfits", type=float, default=0.0)
rqp.add_argument("rentalIncome", type=float, default=0.0)
rqp.add_argument("investmentIncome", type=float, default=0.0)
rqp.add_argument("medicalExpenses", type=float, default=0.0)
rqp.add_argument("educationExpenses", type=float, default=0.0)
rqp.add_argument("donations", type=float, default=0.0)
rqp.add_argument("taxWithheld", type=float, default=0.0)
rqp.add_argument("dependents", type=int, default=0)

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
        args = rqp.parse_args()

        # Extract input data
        # Income data
        employment_income = args.get('employmentIncome', 0)
        pension_income = args.get('pensionIncome', 0)
        business_profits = args.get('businessProfits', 0)
        rental_income = args.get('rentalIncome', 0)
        investment_income = args.get('investmentIncome', 0)
        # Expenses data
        medical_expenses = args.get('medicalExpenses', 0)
        education_expenses = args.get('educationExpenses', 0)
        donations = args.get('donations', 0)
        # Tax withheld data
        tax_withheld = args.get('taxWithheld', 0)
        # Dependents data
        dependents = args.get('dependents', 0)

        # Calculate total income
        total_income = (
            employment_income +
            pension_income +
            business_profits +
            rental_income +
            investment_income
        )

        # Deductible expenses
        deductions = medical_expenses + education_expenses + donations
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

    def dispatch_request(self, *args, **kwargs):
        # Override dispatch_request to route to the appropriate method
        if request.method == 'POST':
            return self.cal_tax()                                    # Call custom method for DELETE requests
        else:
            return super(TaxCalculator, self).dispatch_request(*args, **kwargs)

api.add_resource(TaxCalculator, "/calculate-tax",
                methods=['POST']) 


if __name__ == "__main__":

    print("Server starting up!")
    print(f"Ip: {'0.0.0.0'}, Port: 5000")
    from waitress import serve                                              
    serve(app, port=5000)    