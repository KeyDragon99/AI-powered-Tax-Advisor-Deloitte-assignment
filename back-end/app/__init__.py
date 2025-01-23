from flask import Flask
from flask_restful import Api
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)

    # Import and register routes
    from app.routes import register_routes
    register_routes(api)

    return app