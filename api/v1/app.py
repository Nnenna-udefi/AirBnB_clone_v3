#!/usr/bin/python3
"""V3 of  HBNB REST api"""
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def not_found(error):
    """Handle 404 not found errors and return json object"""
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def close_storage(*args, **kwargs):
    """Close app storage (FileStorage or DBStorage)"""
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=int(port), threaded=True)
