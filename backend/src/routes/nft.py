from flask import Blueprint, request, jsonify
from services.nft_rewards import claim_nft

nft_bp = Blueprint('nft', __name__)

@ nft_bp.route('/claim', methods=['POST'])
def claim():
    user_id = request.json.get("user_id")
    nft = claim_nft(user_id)
    return jsonify({"nft": nft})
