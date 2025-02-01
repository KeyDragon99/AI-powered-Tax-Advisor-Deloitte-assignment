from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "http://localhost:8000"}})
    # CORS(app)
    api = Api(app)

    # Import and register routes
    register_routes(api)

    return app