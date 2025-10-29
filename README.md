# SpongeBob CLI Chatbot

A fun command-line chatbot powered by the SoonerAI platform — talk with SpongeBob directly in your terminal!

---

## Setup

### Python Version
Requires **Python 3.8+**

Make sure you are in the **project's root directory** (the same folder that contains `requirements.txt`), then run:

### Install Dependencies

    pip install -r requirements.txt

---

## SoonerAI API Setup

1. Visit https://ai.sooners.us
2. Click **Sign up** and register using your **OU email**.
3. After logging in, go to **Settings → Account → API Keys**
4. Click **Create a new API key** and copy it.

### Create your environment file

Create a file named `.soonerai.env` in your **home directory**.

**Linux / Mac:**

    nano ~/.soonerai.env

**Windows (PowerShell):**

    notepad $env:USERPROFILE\.soonerai.env

Paste this into the file:

    SOONERAI_API_KEY=your_key_here
    SOONERAI_BASE_URL=https://ai.sooners.us
    SOONERAI_MODEL=gemma3:4b

Replace `your_key_here` with your API key and save the file.

---

## Running the Chatbot

Open a terminal in the **project's root directory** and use the following command

    python spongebob_cli.py

To stop the chat:
- Type `exit` or `quit`
- Or press `Ctrl + C` to force close the process

---

## Example Conversation

```
🧽 SpongeBob Chat (type 'exit' or 'quit' to stop)

You: Hello SpongeBob

SpongeBob: Hiiiiiiiiii! Hello there, friend! It's a glorious day under the sea, don’t you think?
Like, *really* glorious! The sun is shinin’, the bubbles are bubblin’, and I just finished makin’
a Krabby Patty that’s so delicious, it’ll make you wanna do the jellyfishing jig!

What’s shakin’, patty-maker? 😊
```
