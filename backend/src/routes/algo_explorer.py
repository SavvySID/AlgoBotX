from flask import Blueprint, request, jsonify
from services.algo_explorer import fetch_block_details  # ✅ Ensure correct import

algo_explorer_bp = Blueprint("algo_explorer", __name__)

@algo_explorer_bp.route("/algo_explorer/block/<int:block_number>", methods=["GET"])
def get_block(block_number):
    data = fetch_block_details(block_number)
    return jsonify(data)
