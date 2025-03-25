from langchain_community.llms import Ollama

# Load Ollama model (Mistral)
llm = Ollama(model="mistral")

def process_message(question: str):
    """Processes a question using the LangChain-powered AI model."""
    response = llm(question)
    return response
