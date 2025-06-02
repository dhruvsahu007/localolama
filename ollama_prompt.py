import requests

def chat_with_ollama(prompt, model='llama3'):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    result = response.json()
    return result['response']

if __name__ == "__main__":
    prompt = "What are the benefits of using local LLMs?"
    print(f"Prompt: {prompt}")
    response = chat_with_ollama(prompt)
    print(f"AI Response: {response}")
