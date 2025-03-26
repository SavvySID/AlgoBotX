import React, { useState } from "react";

const Faucet = () => {
    const [wallet, setWallet] = useState("");
    const [status, setStatus] = useState("");

    const requestFaucet = async () => {
        const res = await fetch("/faucet/request", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ wallet_address: wallet }),
        });
        const data = await res.json();
        setStatus(data.status);
    };

    return (
        <div>
            <h2>Testnet Faucet</h2>
            <input value={wallet} onChange={(e) => setWallet(e.target.value)} placeholder="Enter Wallet Address" />
            <button onClick={requestFaucet}>Request Algos</button>
            {status && <p>{status}</p>}
        </div>
    );
};

export default Faucet;
