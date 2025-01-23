from flask_restful import fields

tax_fields = {
    "totalIncome": fields.Float,
    "deductions": fields.Float,
    "taxableIncome": fields.Float,
    "grossTax": fields.Float,
    "taxWithheld": fields.Float,
    "taxCredit": fields.Float,
    "netTaxDue": fields.Float,
}
