import os

class Config:
    ALGOD_API = os.getenv("ALGOD_API")
    INDEXER_API = os.getenv("INDEXER_API")
