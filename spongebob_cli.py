#!/usr/bin/env python3
"""
Interactive chat with ai.sooners.us using gemma3:4b model.
Maintains a conversation history and truncates old turns.

Requires:
  pip install requests python-dotenv
"""

import os
import requests
from dotenv import load_dotenv

# Load API key and base URL from ~/.soonerai.env
load_dotenv(os.path.join(os.path.expanduser("~"), ".soonerai.env"))

API_KEY = os.getenv("SOONERAI_API_KEY")
BASE_URL = os.getenv("SOONERAI_BASE_URL", "https://ai.sooners.us").rstrip("/")
MODEL = os.getenv("SOONERAI_MODEL", "gemma3:4b")

if not API_KEY:
    raise RuntimeError("Missing SOONERAI_API_KEY in ~/.soonerai.env")

# Chat history with a fixed system prompt
history = [
    {"role": "system", "content": "You are SpongeBob SquarePants. Speak cheerfully and use ocean humor."}
]

MAX_TURNS = 5  # keep last N user-assistant pairs

def chat_with_api(messages):
    """Send a request to the Sooners AI API with the current message history."""
    url = f"{BASE_URL}/api/chat/completions"
    payload = {"model": MODEL, "messages": messages, "temperature": 0.6}

    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=60,
    )

    if response.status_code == 200:
        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        return reply
    else:
        raise RuntimeError(f"Error {response.status_code}: {response.text}")

def truncate_history():
    """Keep only the system message and last N turns."""
    # system + last N*2 messages (user + assistant)
    global history
    system_message = history[0]
    recent = history[-MAX_TURNS*2:]
    history = [system_message] + recent

def main():
    print("🧽 SpongeBob Chat (type 'exit' or 'quit' to stop)")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Bye-bye! 🫧")
            break

        # Append user message
        history.append({"role": "user", "content": user_input})

        # Optionally truncate older turns
        truncate_history()

        # Get assistant reply
        try:
            reply = chat_with_api(history)
        except Exception as e:
            print("Error:", e)
            continue

        # Append assistant reply
        history.append({"role": "assistant", "content": reply})
        print(f"SpongeBob: {reply}\n")

if __name__ == "__main__":
    main()
