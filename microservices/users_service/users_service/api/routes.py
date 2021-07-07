from flask import Flask, request, jsonify, url_for, Blueprint

api = Blueprint('api', __name__)

@api.route('/test', methods=['GET'])
def handle_hello():
    response_body = {
        "message": "Microservice User Authentication Response"
    }

    return jsonify(response_body), 200