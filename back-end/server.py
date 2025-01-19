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
CORS(app)

'''Define request parser values and their properties for ADD, PUT, POST, DELETE requests'''
add_rqp = reqparse.RequestParser()                                          
add_rqp.add_argument('name', type=str, required=True, help='Name is required in order to add an ingredient.')                       
add_rqp.add_argument('quantity', type=int)
add_rqp.add_argument('comment', type=str)

del_rqp = reqparse.RequestParser()                                          
del_rqp.add_argument('name', type=str, required=True, help='Name is required in order to delete an ingredient.')

update_rqp = reqparse.RequestParser()
update_rqp.add_argument('name', type=str)
update_rqp.add_argument('quantity', type=int)
update_rqp.add_argument('comment', type=str)
update_rqp.add_argument('iname', type=str, required=True)

api = Api(app)

resource_fields = {                                                         #Define the resource fields that will be returned
    'name': fields.String,
    'quantity': fields.Integer,
    'comment': fields.String
}

pagination_fields = {
    'page': fields.Integer,
    'itemsPerPage': fields.Integer,
    'totalItems': fields.Integer,
    'totalPages': fields.Integer
}

response_fields = {
    'data': fields.List(fields.Nested(resource_fields)),
    'pagination': fields.Nested(pagination_fields)
}

class Ingredients(Resource):

    @marshal_with(response_fields)
    def retrieve_quantities(self):
        
        args = request.args
        out = paginate(args)

        return out

    def dispatch_request(self, *args, **kwargs):
        # Override dispatch_request to route to the appropriate method
        if request.method == 'GET':
            return self.retrieve_quantities()                               # Call custom method for GET requests
        elif request.method == 'POST':
            return self.add_ingredient()                                    # Call custom method for DELETE requests
        elif request.method == 'DELETE':
            return self.delete_ingredient()                                 # Call custom method for DELETE requests
        elif request.method == 'PUT':                                        
            return self.update_ingredient()                                 # Call custom method for PUT requests
        else:
            return super(Ingredients, self).dispatch_request(*args, **kwargs)

api.add_resource(Ingredients, "/Ingredients/retrieve", "/Ingredients/add_new", "/Ingredients/remove", "/Ingredients/update",
                methods=['GET', 'POST', 'DELETE', 'PUT']) 


if __name__ == "__main__":

    print("Server starting up!")
    print(f"Ip: {'0.0.0.0'}, Port: 5000")
    from waitress import serve                                              
    serve(app, port=5000)    