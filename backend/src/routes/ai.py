from flask import Blueprint, request, jsonify
from services.ai_assistant import get_ai_response

ai_bp = Blueprint("ai", __name__)

@ai_bp.route("/query", methods=["POST"])
def query():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"error": "Missing 'message' field"}), 400

        user_input = data["message"]
        response = get_ai_response(user_input)

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
