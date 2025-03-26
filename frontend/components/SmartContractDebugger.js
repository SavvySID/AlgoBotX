import React, { useState } from "react";

const SmartContractDebugger = () => {
    const [contract, setContract] = useState("");
    const [debugResult, setDebugResult] = useState(null);

    const debugContract = async () => {
        const res = await fetch("/smart_contract/debug", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ contract_code: contract }),
        });
        const data = await res.json();
        setDebugResult(data);
    };

    return (
        <div>
            <h2>Smart Contract Debugger</h2>
            <textarea value={contract} onChange={(e) => setContract(e.target.value)} placeholder="Enter Smart Contract Code" />
            <button onClick={debugContract}>Debug</button>
            {debugResult && <pre>{JSON.stringify(debugResult, null, 2)}</pre>}
        </div>
    );
};

export default SmartContractDebugger;
