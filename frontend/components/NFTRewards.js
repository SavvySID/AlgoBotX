import React, { useState } from "react";

const NFTRewards = () => {
    const [userId, setUserId] = useState("");
    const [reward, setReward] = useState(null);

    const fetchReward = async () => {
        const res = await fetch(`/nft/rewards/${userId}`);
        const data = await res.json();
        setReward(data);
    };

    return (
        <div>
            <h2>NFT Rewards</h2>
            <input value={userId} onChange={(e) => setUserId(e.target.value)} placeholder="Enter User ID" />
            <button onClick={fetchReward}>Check Rewards</button>
            {reward && <pre>{JSON.stringify(reward, null, 2)}</pre>}
        </div>
    );
};

export default NFTRewards;
