import { useState } from "react";
import axios from "axios";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const sendQuery = async () => {
    const res = await axios.post("http://127.0.0.1:5000/query", { message: query });
    setResponse(res.data.response);
  };

  return (
    <div>
      <h1>AlgoBotX</h1>
      <input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Ask me anything" />
      <button onClick={sendQuery}>Ask</button>
      <p>Response: {response}</p>
    </div>
  );
}

export default App;
