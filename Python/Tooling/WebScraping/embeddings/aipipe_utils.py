import requests

AIPIPE_EMBEDDING_URL = "https://aipipe.org/openai/v1/embeddings"
AIPIPE_API_KEY = "your_actual_api_key"

def get_embedding(text: str):
    headers = {
        "Authorization": f"Bearer {AIPIPE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "input": text[:3000]
    }

    res = requests.post(AIPIPE_EMBEDDING_URL, headers=headers, json=data)
    res.raise_for_status()

    return res.json()["embedding"]