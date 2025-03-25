from algosdk.v2client import algod

# Algorand Node Configuration
ALGOD_TOKEN = "your-algod-token"
ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"

client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

def get_balance(address: str):
    """Fetches the balance of an Algorand account."""
    account_info = client.account_info(address)
    return account_info.get('amount') / 1e6  # Convert microAlgos to Algos
