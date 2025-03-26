import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ALGORAND_INDEXER_API = os.getenv("ALGORAND_INDEXER_API")
WALLET_PROVIDER = os.getenv("WALLET_PROVIDER")
