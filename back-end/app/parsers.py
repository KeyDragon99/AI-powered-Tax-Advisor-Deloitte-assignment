from flask_restful import reqparse

# Shared items
parsing_items = [
    "employmentIncome",
    "pensionIncome",
    "businessProfits",
    "rentalIncome",
    "educationExpenses",
    "businessExpenses",
    "taxWithheld",
]

# Tax calculator parser
tax_parser = reqparse.RequestParser()
tax_parser.add_argument("filingStatus", type=str, choices=["single", "marriedJoint", "marriedSeparate"], required=True)
for item in parsing_items:
    tax_parser.add_argument(item, type=float, default=0.0)
tax_parser.add_argument("dependents", type=int, default=0)

# Advice parser
advice_parser = tax_parser.copy()
advice_parser.add_argument("userComments", type=str, default="")
