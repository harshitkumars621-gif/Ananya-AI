import subprocess
from voice.speak import speak
from voice.listen import listen

AI_NAME = "Ananya"
USER_NAME = "Harshit"

print("=" * 50)
print("🌸 Ananya AI Assistant")
print("=" * 50)

speak(f"Hello {USER_NAME}! Main Ananya hoon.")

while True:

    print("\nSay 'Hey Ananya'...")

    text = listen()

    if "hey ananya" not in text:
        continue

    speak("Yes Harshit, batao.")

    user = listen()

    if user == "":
        continue

    if "bye" in user:
        speak("Goodbye Harshit.")
        break

    prompt = f"""
You are Ananya.

The user's name is Harshit.

Always call the user Harshit.

Reply naturally.

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

    print(answer)

    speak(answer)