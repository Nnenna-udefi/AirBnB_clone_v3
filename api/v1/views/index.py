#!/usr/bin/python3
"""API endpoint index file"""
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def get_status():
    """Returns HTTP Json status 200"""
    return jsonify({"status": "OK"}), 200


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
    return_dict = {}
    for name, cls in stats.items():
        return_dict[name] = storage.count(cls)
    return jsonify(return_dict)
