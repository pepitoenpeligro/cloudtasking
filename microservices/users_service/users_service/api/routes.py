from flask import Flask, request, jsonify, url_for, Blueprint
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from datetime import datetime, timedelta

api = Blueprint('api', __name__)




@api.route('/test', methods=['GET'])
def handle_hello():
    response_body = {
        "message": "Microservice User Authentication Response"
    }

    return jsonify(response_body), 200


@api.route('/token', methods=['POST'])
def create_token_jwt():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    token = create_access_token(identity=email,expires_delta=timedelta(minutes=30))
    return jsonify(access_token=token)
