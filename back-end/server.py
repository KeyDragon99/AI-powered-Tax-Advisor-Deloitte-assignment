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
rqp.add_argument('income', type=float, required=True, help="Income is required and should be a float.")                       
rqp.add_argument('expenses', type=float, required=True, help="Expenses are required and should be a float.")
rqp.add_argument('filingStatus', type=str, required=True, choices=('single', 'married', 'headOfHousehold'), help="Filing Status must be one of 'single', 'married', or 'headOfHousehold'.")
rqp.add_argument('dependents', type=int, required=True, help="Dependents is required and should be an integer.")
rqp.add_argument('withholding', type=float, required=True, help="Withholding is required and should be a float.")
rqp.add_argument('otherIncome', type=float, default=0, help="Other Income should be a float.")
rqp.add_argument('taxCredits', type=float, default=0, help="Tax Credits should be a float.")

resource_fields = {                                                         #Define the resource fields that will be returned
    'taxableIncome': fields.Float,
    'tax': fields.Float,
    'taxOwed': fields.Float,
    'refund': fields.Float
}

class TaxCalculator(Resource):

    @marshal_with(resource_fields)
    def cal_tax(self):
        args = rqp.parse_args()
        print(args)
        standard_deductions = {
            'single': 12550,
            'married': 25100,
            'headOfHousehold': 18800,
        }

        tax_brackets = {
            'single': [0.1, 0.12, 0.22],
            'married': [0.1, 0.12, 0.22],
            'headOfHousehold': [0.1, 0.12, 0.22],
        }

        adjusted_income = args['income'] + args['otherIncome'] - args['expenses']
        standard_deduction = standard_deductions.get(args['filingStatus'], 12550)
        taxable_income = max(0, adjusted_income - standard_deduction)

        tax_rate = tax_brackets[args['filingStatus']][0]
        tax = taxable_income * tax_rate

        dependent_deduction = args['dependents'] * 2000
        tax = max(0, tax - dependent_deduction - args['taxCredits'])

        tax_owed = max(0, tax - args['withholding'])
        refund = max(0, args['withholding'] - tax)

        return {
            'taxableIncome': taxable_income,
            'tax': tax,
            'taxOwed': tax_owed,
            'refund': refund
        }, 200

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