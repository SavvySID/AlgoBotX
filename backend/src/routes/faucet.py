from flask import Blueprint, request, jsonify
from services.testnet_faucet import request_faucet

faucet_bp = Blueprint('faucet', __name__)

@faucet_bp.route('/get', methods=['POST'])
def get_faucet():
    address = request.json.get("address")
    tx_hash = request_faucet(address)
    return jsonify({"transaction_hash": tx_hash})
