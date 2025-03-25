from http import client
from algosdk.future.transaction import PaymentTxn # type: ignore
from algosdk import account

def send_algo(sender, private_key, receiver, amount):
    """Sends ALGO from one account to another."""
    params = client.suggested_params()
    txn = PaymentTxn(sender, params, receiver, int(amount * 1e6))
    signed_txn = txn.sign(private_key)
    txid = client.send_transaction(signed_txn)
    return f"Transaction ID: {txid}"
