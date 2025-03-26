import axios from "axios";

const API_URL = "http://localhost:8000";

export const askChatbot = async (question: string) => {
    const response = await axios.post(`${API_URL}/chatbot/ask`, { question });
    return response.data.response;
};
