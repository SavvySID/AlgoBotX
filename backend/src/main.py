from flask import Flask
from flask_cors import CORS

# Import all blueprints (Route Modules)
from routes.ai import ai_bp
from routes.algo_explorer import algo_explorer_bp
from routes.wallet import wallet_bp
from routes.smart_contract import smart_contract_bp
from routes.sdk import sdk_bp
from routes.nft import nft_bp
from routes.faucet import faucet_bp

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}})

# ✅ Register Blueprints (Modular Route Integration)
app.register_blueprint(ai_bp, url_prefix="/ai")  # AI Assistant
app.register_blueprint(algo_explorer_bp, url_prefix="/algo_explorer")  # Algorand Explorer
app.register_blueprint(wallet_bp, url_prefix="/wallet")  # Wallet Connection
app.register_blueprint(smart_contract_bp, url_prefix="/smart_contract")  # Smart Contract Debugger
app.register_blueprint(sdk_bp, url_prefix="/sdk")  # SDK Support
app.register_blueprint(nft_bp, url_prefix="/nft")  # NFT & ASA Management
app.register_blueprint(faucet_bp, url_prefix="/faucet")  # Testnet Faucet

@app.route("/")
def home():
    return "🚀 AlgoBotX Backend is Running!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
