import re
import subprocess
from memory.memory import Memory

memory = Memory()

print("🌸 Ananya AI Ready!")
print("Type 'exit' to quit.\n")

while True:

    user = input("Harshit: ").strip()

    if user.lower() == "exit":
        print("\n🌸 Ananya: Bye Harshit ❤️")
        break

    # ----------------------------
    # Favourite Game Save
    # ----------------------------
    match = re.match(r"^mera favourite game (.+) hai\.?$", user.lower())

    if match:

        game = match.group(1).strip().title()

        memory.save_preference("favourite_game", game)

        print("\n🌸 Ananya: Thik hai Harshit ❤️")
        print("Maine yaad rakh liya ki tumhara favourite game " + game + " hai.\n")

        continue

    # ----------------------------
    # Favourite Game Recall
    # ----------------------------
    if user.lower() in [
        "mera favourite game kya hai",
        "mera favourite game kya hai?",
        "mera favorite game kya hai",
        "mera favorite game kya hai?"
    ]:

        game = memory.get_preference("favourite_game")

        if game:
            print("\n🌸 Ananya: Harshit, tumhara favourite game " + game + " hai.\n")
        else:
            print("\n🌸 Ananya: Mujhe abhi tak tumhara favourite game nahi pata.\n")

        continue

    # ----------------------------
    # Add Task
    # ----------------------------

    if user.lower().startswith("task add:"):

        task = user[9:].strip()

        memory.add_task(task)

        print("\n🌸 Ananya: Thik hai Harshit ❤️")
        print("Task save ho gaya.\n")

        continue

    # ----------------------------
    # Show Tasks
    # ----------------------------

    if user.lower() in [
        "mere tasks",
        "mere tasks kya hain",
        "show tasks"
    ]:

        task_list = memory.get_tasks()

        if not task_list:

            print("\n🌸 Ananya: Tumhare paas abhi koi task nahi hai.\n")

        else:

            print("\n🌸 Ananya: Tumhare pending tasks:\n")

            for i, task in enumerate(task_list, start=1):

                print(f"{i}. {task}")

            print()

        continue
    # ----------------------------
    # Normal AI Chat
    # ----------------------------

    prompt = f"""
You are Ananya.

The user's name is Harshit.

Reply naturally in Hindi.

If the user asks about favourite game, tasks or personal information that is already handled by the program, don't invent anything.

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

    print("\n🌸 Ananya:")
    print(answer)