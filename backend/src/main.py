from flask import Flask, request, jsonify
from langchain.llms import Ollama
from algosdk.v2client import algod
from services.ai_assistant import process_message
from services.algo_explorer import get_balance

app = Flask(__name__)

# Load AI model
llm = Ollama(model="mistral")

# Algorand Node Configuration
ALGOD_TOKEN = "your-algod-token"
ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

@app.route("/query", methods=["POST"])
def query():
    """Handles AI chatbot queries."""
    data = request.json
    user_input = data.get("message", "")
    ai_response = process_message(user_input)
    return jsonify({"response": ai_response})

@app.route("/balance/<address>", methods=["GET"])
def balance(address):
    """Fetches the balance of an Algorand account."""
    balance = get_balance(address)
    return jsonify({"balance": balance})

if __name__ == "__main__":
    app.run(debug=True)
