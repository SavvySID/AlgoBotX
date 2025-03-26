from langchain_ollama import OllamaLLM  # Updated import
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory  # Updated import

# Initialize LLM
llm = OllamaLLM(model="mistral")

# Define prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "This is a conversation AI assistant."),
    ("human", "{input}")
])

# Use new memory management
memory = ChatMessageHistory()

# AI Chain using new API
conversation = RunnableWithMessageHistory(
    llm | prompt,
    input_messages_key="input",
    history_messages_key="history",
    get_session_history=lambda session_id: memory  # Simple session memory
)

# Function to get AI response
def get_ai_response(user_input, session_id="default"):
    response = conversation.invoke(
        {"input": user_input, "history": memory.messages},  
        config={"configurable": {"session_id": session_id}}
    )
    return response
