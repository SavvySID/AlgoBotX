import React, { useState } from "react";

const WalletConnect = () => {
    const [address, setAddress] = useState("");
    const [balance, setBalance] = useState(null);

    const fetchBalance = async () => {
        const res = await fetch(`/wallet/${address}/balance`);
        const data = await res.json();
        setBalance(data.balance);
    };

    return (
        <div>
            <h2>Wallet Connect</h2>
            <input value={address} onChange={(e) => setAddress(e.target.value)} placeholder="Enter Wallet Address" />
            <button onClick={fetchBalance}>Get Balance</button>
            {balance && <p>Balance: {balance} ALGO</p>}
        </div>
    );
};

export default WalletConnect;
