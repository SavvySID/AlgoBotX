import React, { useState } from "react";

const SDKDocs = () => {
    const [language, setLanguage] = useState("python");
    const [docs, setDocs] = useState("");

    const fetchDocs = async () => {
        const res = await fetch(`/sdk/docs/${language}`);
        const data = await res.json();
        setDocs(data.docs);
    };

    return (
        <div>
            <h2>SDK Documentation</h2>
            <select value={language} onChange={(e) => setLanguage(e.target.value)}>
                <option value="python">Python</option>
                <option value="javascript">JavaScript</option>
                <option value="go">Go</option>
            </select>
            <button onClick={fetchDocs}>Get Docs</button>
            {docs && <p><a href={docs} target="_blank" rel="noopener noreferrer">View Documentation</a></p>}
        </div>
    );
};

export default SDKDocs;
