from brain.tools import calculator
from datetime import datetime

def check_command(user, memory):
    text = user.lower().strip()

    # Time
    if any(x in text for x in [
        "time",
        "samay",
        "kitna baje",
        "kitne baje"
    ]):
        return True, f"🌸 Ananya: Abhi {datetime.now().strftime('%I:%M %p')} baj rahe hain."

    # Date
    if any(x in text for x in [
        "date",
        "aaj ki date",
        "aaj kya date hai"
    ]):
        return True, f"🌸 Ananya: Aaj {datetime.now().strftime('%d %B %Y')} hai."

    # Favourite Game
    if text == "mera favourite game kya hai":
        game = memory.get_preference("favourite_game")

        if game:
            return True, f"🌸 Ananya: Tumhara favourite game {game} hai."

        return True, "🌸 Ananya: Mujhe abhi tak tumhara favourite game nahi pata."

   # Calculator
    answer = calculator(text)

    if answer is not None:
        return True, f"🌸 Ananya: Answer = {answer}"
    return False, ""