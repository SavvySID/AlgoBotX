from flask import Blueprint, jsonify, request
from services.wallet_connect import get_wallet_balance

wallet_bp = Blueprint('wallet', __name__)

@wallet_bp.route('/balance', methods=['GET'])
def balance():
    address = request.args.get('address')
    balance = get_wallet_balance(address)
    return jsonify({"balance": balance})
