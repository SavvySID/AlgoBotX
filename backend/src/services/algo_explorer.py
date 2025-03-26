import requests

# AlgoExplorer API Base URL
ALGO_EXPLORER_API = "https://algoexplorerapi.io/v2"

# Function to fetch block details
def fetch_block_details(block_number):
    try:
        response = requests.get(f"{ALGO_EXPLORER_API}/blocks/{block_number}")
        response.raise_for_status()  # Raise an error if status code is not 200
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
