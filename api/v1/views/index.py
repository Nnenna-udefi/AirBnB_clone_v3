#!/usr/bin/python3
"""app_views index file"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    """method to get status and return a JSON file"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def get_count():
    """retrieves the number of each objects by type"""
    stats = {
        "Amenity": "amenities",
        "City": "cities",
        "Place": "places",
        "Review": "reviews",
        "State": "states",
        "User": "users"
    }
    return jsonify({name: storage.count(cls) for cls, name in stats.items()})


if __name__ == "__main__":
    pass
