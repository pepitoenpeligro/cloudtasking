
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.url_map.strict_slashes = False

from api.routes import api

app.register_blueprint(api, url_prefix='/api/auth')
app.config['JWT_SECRET_KEY'] = "misecreto"

jwt = JWTManager(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)