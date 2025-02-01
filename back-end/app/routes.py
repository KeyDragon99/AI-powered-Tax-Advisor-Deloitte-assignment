from app.parsers import tax_parser, advice_parser
from app.models import tax_fields
from app.utils import generate_prompt
from services.tax_calculator import calculate_tax

from flask_restful import Resource, marshal_with
from flask import jsonify
from openai import OpenAI
import os

# OpenAI client setup
key = os.getenv("OPENAI_API_KEY")
if not key:
    raise ValueError("OpenAI API key is missing")

client = OpenAI(api_key=key)

def register_routes(api):
    api.add_resource(TaxCalculator, "/calculate-tax")
    api.add_resource(OpenAIAdvisor, "/tax-advice")

class TaxCalculator(Resource):
    @marshal_with(tax_fields)
    def post(self):
        try:
            args = tax_parser.parse_args()
            response = calculate_tax(args)
            return response, 200
        except Exception:
            return {'error': 'There was an error calculating the taxes, please try again later.'}, 500

class OpenAIAdvisor(Resource):
    def post(self):
        try:
            args = advice_parser.parse_args()
            user_comments = args.pop('userComments', '')
            prompt = generate_prompt(args, user_comments)
            
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a tax advisor. Provide practical suggestions."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=750
            )
            advice = response.choices[0].message.content
            return {'advice': advice}, 200
        except Exception:
            return {'error': 'There was an error fetching an answer from the LLM, please try again later.'}, 500
