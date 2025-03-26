import React, { useState } from "react";
import axios from "axios";
import API_BASE_URL from "../config"; // Import API base URL
import "./Explorer.css";

const AlgoExplorer = () => {
    const [blockNumber, setBlockNumber] = useState("");
    const [blockData, setBlockData] = useState(null);
    const [error, setError] = useState(null);

    const fetchBlockDetails = async () => {
        if (!blockNumber.trim()) return;

        try {
            const response = await axios.get(`${API_BASE_URL}/algo_explorer/block/${blockNumber}`);
            setBlockData(response.data);
            setError(null);
        } catch (err) {
            console.error("Error fetching block details:", err);
            setError("Unable to fetch block details.");
            setBlockData(null);
        }
    };

    return (
        <div className="explorer-container">
            <h2>Algo Explorer</h2>
            <input
                type="text"
                value={blockNumber}
                onChange={(e) => setBlockNumber(e.target.value)}
                placeholder="Enter block number..."
            />
            <button onClick={fetchBlockDetails}>Fetch Block</button>

            {error && <p className="error">{error}</p>}

            {blockData && (
                <div className="block-details">
                    <h3>Block #{blockData.blockNumber}</h3>
                    <p><strong>Hash:</strong> {blockData.hash}</p>
                    <p><strong>Timestamp:</strong> {new Date(blockData.timestamp * 1000).toLocaleString()}</p>
                    <p><strong>Transactions:</strong> {blockData.transactions.length}</p>
                </div>
            )}
        </div>
    );
};

export default AlgoExplorer;
