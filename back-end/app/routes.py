from app.parsers import tax_parser, advice_parser
from app.models import tax_fields
from app.utils import generate_prompt
from services.tax_calculator import calculate_tax

from flask_restful import Resource, marshal_with
from flask import jsonify
from openai import OpenAI, APIError, Timeout, InvalidRequestError
import os, logging

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
            if not args:  # Basic input validation
                logging.error("Empty args received")
                return {'error': 'Missing input parameters'}, 400
            response = calculate_tax(args)
            return response, 200
        
        except ValueError as e:
            logging.exception("Input validation failed")
            return {'error': 'Invalid input parameters'}, 400
        
        except Exception as e:
            logging.exception("Unexpected error in tax calculator endpoint")
            return {'error': 'Internal server error'}, 500

class OpenAIAdvisor(Resource):
    def post(self):
        try:
            args = advice_parser.parse_args()
            if not args:  # Basic input validation
                logging.error("Empty args received")
                return {'error': 'Missing input parameters'}, 400
                
            user_comments = args.pop('userComments', '')
            prompt = generate_prompt(args, user_comments)
            
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a tax advisor. Provide practical suggestions."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=750,
                timeout=15  # Add timeout
            )
            advice = response.choices[0].message.content
            return {'advice': advice}, 200
        
        except ValueError as e:
            logging.exception("Input validation failed")
            return {'error': 'Invalid input parameters'}, 400
                
        except (APIError, Timeout) as e:
            logging.exception("OpenAI API request failed")
            return {'error': 'Service temporarily unavailable'}, 503
        
        except InvalidRequestError as e:
            logging.exception(f"Invalid OpenAI request: {str(e)[:200]}")
            return {'error': 'Invalid request'}, 400        
        
        except Exception as e:
            logging.exception("Unexpected error in ai advice endpoint")
            return {'error': 'Internal server error'}, 500