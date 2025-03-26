from flask import Blueprint, request, jsonify
from services.sdk_helper import get_sdk_help

sdk_bp = Blueprint('sdk', __name__)

@sdk_bp.route('/help', methods=['POST'])
def sdk_help():
    data = request.json
    query = data.get('query', '')
    response = get_sdk_help(query)
    return jsonify({"response": response})
