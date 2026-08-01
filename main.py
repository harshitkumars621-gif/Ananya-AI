import re
import subprocess
from brain.chat import chat
from brain.commands import check_command
from memory.memory import Memory

memory = Memory()

print("🌸 Ananya AI Ready!")
print("Type 'exit' to quit.\n")

while True:

    user = input("Harshit: ").strip()

    if user.lower() == "exit":
        print("\n🌸 Ananya: Bye Harshit ❤️")
        break

    handled, reply = check_command(user, memory)

    if handled:
        print("\n" + reply + "\n")
        continue

    # ==========================
    # Favourite Game Save
    # ==========================

    match = re.match(r"^mera favourite game (.+) hai\.?$", user.lower())

    if match:

        game = match.group(1).strip().title()

        memory.save_preference("favourite_game", game)

        print("\n🌸 Ananya: Thik hai Harshit ❤️")
        print("Maine yaad rakh liya ki tumhara favourite game " + game + " hai.\n")

        continue

    # ==========================
    # Favourite Game Recall
    # ==========================

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

    # ==========================
    # Add Task
    # ==========================

    if user.lower().startswith("task add:"):

        task = user[9:].strip()

        memory.add_task(task)

        print("\n🌸 Ananya: Thik hai Harshit ❤️")
        print("Task save ho gaya.\n")

        continue

    # ==========================
    # Show Tasks
    # ==========================

    if any(x in user.lower() for x in [
        "mera task",
        "mere task",
        "mera tasks",
        "mere tasks",
        "task"
    ]):

        task_list = memory.get_tasks()

        if not task_list:

            print("\n🌸 Ananya: Tumhare paas abhi koi task nahi hai.\n")

        else:

            print("\n🌸 Ananya: Tumhare pending tasks:\n")

            for i, task in enumerate(task_list, start=1):

                print(f"{i}. {task}")

            print()

        continue
    # ==========================
    # Time
    # ==========================

    if any(x in user.lower() for x in [
        "time",
        "samay",
        "kitna baje",
        "kitne baje"
    ]):

        from datetime import datetime

        print("\n🌸 Ananya: Abhi " +
              datetime.now().strftime("%I:%M %p") +
              " baj rahe hain.\n")

        continue


    # ==========================
    # Date
    # ==========================

    if any(x in user.lower() for x in [
        "date",
        "aaj ki date",
        "aaj kya date hai"
    ]):

        from datetime import datetime

        print("\n🌸 Ananya: Aaj " +
              datetime.now().strftime("%d %B %Y") +
              " hai.\n")

        continue


    # ==========================
    # Favourite Color Save
    # ==========================

    match = re.match(r"^mera favourite color (.+) hai\.?$", user.lower())

    if match:
        color = match.group(1).strip().title()
        memory.save_preference("favourite_color", color)

        print("\n🌸 Ananya: Thik hai Harshit ❤️")
        print("Maine yaad rakh liya ki tumhara favourite color " + color + " hai.\n")
        continue


    # ==========================
    # Favourite Color Recall
    # ==========================

    if user.lower() in [
        "mera favourite color kya hai",
        "mera favorite color kya hai"
    ]:

        color = memory.get_preference("favourite_color")

        if color:
            print("\n🌸 Ananya: Tumhara favourite color " + color + " hai.\n")
        else:
            print("\n🌸 Ananya: Mujhe tumhara favourite color nahi pata.\n")

        continue


    # ==========================
    # Favourite Food Save
    # ==========================

    match = re.match(r"^mera favourite food (.+) hai\.?$", user.lower())

    if match:
        food = match.group(1).strip().title()
        memory.save_preference("favourite_food", food)

        print("\n🌸 Ananya: Thik hai Harshit ❤️")
        print("Maine yaad rakh liya ki tumhara favourite food " + food + " hai.\n")
        continue


    # ==========================
    # Favourite Food Recall
    # ==========================

    if user.lower() in [
        "mera favourite food kya hai",
        "mera favorite food kya hai"
    ]:

        food = memory.get_preference("favourite_food")

        if food:
            print("\n🌸 Ananya: Tumhara favourite food " + food + " hai.\n")
        else:
            print("\n🌸 Ananya: Mujhe tumhara favourite food nahi pata.\n")

        continue
    # ==========================
    # Favourite Movie Save
    # ==========================

    match = re.match(r"^mera favourite movie (.+) hai\.?$", user.lower())

    if match:
        movie = match.group(1).strip().title()
        memory.save_preference("favourite_movie", movie)

        print("\n🌸 Ananya: Thik hai Harshit ❤️")
        print("Maine yaad rakh liya ki tumhari favourite movie " + movie + " hai.\n")
        continue


    # ==========================
    # Favourite Movie Recall
    # ==========================

    if user.lower() in [
        "mera favourite movie kya hai",
        "mera favorite movie kya hai"
    ]:

        movie = memory.get_preference("favourite_movie")

        if movie:
            print("\n🌸 Ananya: Tumhari favourite movie " + movie + " hai.\n")
        else:
            print("\n🌸 Ananya: Mujhe tumhari favourite movie nahi pata.\n")

        continue


    # ==========================
    # AI Chat
    # ==========================

    prompt = f"""
You are Ananya.

You are Harshit's personal AI assistant.

Reply naturally in Hindi.

Keep replies short.

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