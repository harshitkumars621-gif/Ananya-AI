import subprocess

def chat(user):

    prompt = f"""
You are Ananya.

You are Harshit's personal AI assistant.

Always reply naturally in Hindi.

Keep answers short and friendly.

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

    return result.stdout.strip()