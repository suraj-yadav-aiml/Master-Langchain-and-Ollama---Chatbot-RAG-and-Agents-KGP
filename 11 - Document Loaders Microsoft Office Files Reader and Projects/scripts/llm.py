from langchain_ollama import ChatOllama

base_url = "http://localhost:11434"
model = 'llama3.2'


def get_llama(base_url=base_url, model=model):
    return ChatOllama(
        base_url=base_url,
        model=model
    )

