# 🧠 Local LLM Prompt Script (Ollama + Python)

This script sends a prompt to a locally running Large Language Model (LLM) like `llama3` using [Ollama](https://ollama.com), and prints the AI's response.

---

## ✅ Objective

- Run a local LLM (like `llama3`) using Ollama
- Send a prompt to it programmatically (not via CLI)
- Get a response and print it
- Deliver as a single Python file, ready to run

---

## 📦 Requirements

- [Ollama installed](https://ollama.com/download) and running on your machine
- Python 3.7+
- `llama3` model pulled via:
  ```bash
  ollama pull llama3
  ```
## ▶️ How to Run
#### Clone this repo:
```bash
git clone https://github.com/dhruvsahu007/localolama.git
cd localolama
```
#### Install Python dependency:
```bash
pip install requests
```
#### Run the script:
```bash
python ollama_prompt.py
```

### 🧪 What It Does
Sends the prompt:
```bash
What are the benefits of using local LLMs?
Gets a response via Ollama's HTTP API (localhost:11434)
Prints both the prompt and the model's response
```

### 🛑 Note
This uses Ollama’s HTTP API — no CLI (ollama run) involved.

