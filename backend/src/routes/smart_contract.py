from flask import Blueprint, request, jsonify
from services.smart_contract_debugger import analyze_contract  # ✅ Ensure correct import

smart_contract_bp = Blueprint("smart_contract", __name__)

@smart_contract_bp.route("/smart_contract/analyze", methods=["POST"])
def analyze():
    data = request.json
    contract_code = data.get("contract_code", "")
    
    result = analyze_contract(contract_code)
    return jsonify(result)
