import subprocess
from voice.speak import speak


def chat(user):

    print("DEBUG: chat() called")
    print("User:", user)

    prompt = f"""
You are Ananya.

You are Harshit's personal AI assistant.

Always reply in the same language as the user.

Rules:
- If the user speaks Hindi, reply in Hindi.
- If the user speaks English, reply in English.
- If the user speaks Hinglish, reply in Hinglish.
- If the user speaks Maithili, reply in Maithili.
- If the user speaks Bengali, reply in Bengali.
- If the user speaks Punjabi, reply in Punjabi.
- If the user speaks Gujarati, reply in Gujarati.
- If the user speaks Haryanvi, reply in Haryanvi.
- If the user mixes languages, reply naturally in the same style.

Keep replies short, friendly and natural.

User:
{user}

Assistant:
"""

    result = subprocess.run(
        ["ollama", "run", "llama3.2"],
        input=prompt,
        capture_output=True,
        text=True
    )

    answer = result.stdout.strip()

    print("DEBUG Answer:", answer)

    if answer:
        speak(answer)

    return answer