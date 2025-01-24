import pytest
from app import create_app

data = {
    "userComments": "",
    "filingStatus": "single",
    "employmentIncome": 0.0,
    "pensionIncome": 0.0,
    "businessProfits": 0.0,
    "rentalIncome": 0.0,
    "educationExpenses": 0.0,
    "businessExpenses": 0.0,
    "taxWithheld": 0.0,
    "dependents": 0,
}

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_tax_cal(client):
    rv = client.post('/calculate-tax', json=data)
    assert rv.status_code == 200

def test_tax_advice(client):
    rv = client.post('/tax-advice', json=data)
    assert rv.status_code == 200
