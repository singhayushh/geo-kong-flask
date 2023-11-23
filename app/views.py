# app/views.py
from flask import request, jsonify
from app import app
from app.utils import update_geo, extract_country_list, extract_allowed_country_list

@app.route('/update_geo', methods=['POST'])
def update_geo_route():
    data = request.get_json()
    mode = data.get('mode')
    selected_countries = data.get('selectedCountries', [])

    if not mode or mode not in ['whitelist', 'blacklist']:
        return jsonify({"error": "Invalid mode"}), 400

    update_geo(mode, selected_countries)

    return jsonify({"message": "Countries list updated successfully"})

@app.route('/get_country_list', methods=['GET'])
def get_country_list():
    country_list = extract_country_list()
    return jsonify({"countries": country_list})

@app.route('/get_allowed_country_list', methods=['GET'])
def get_allowed_country_list():
    country_list = extract_allowed_country_list()
    return jsonify({"countries": country_list})