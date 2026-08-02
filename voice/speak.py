import subprocess
import re

def speak(text):
    try:
        # Hindi script ko Roman me convert nahi, sirf emojis hatao
        clean = re.sub(r'[^\w\s.,?!\u0900-\u097F]', '', text)

        subprocess.run([
            "say",
            "-v",
            "Samantha",   # ya "Daniel"
            clean
        ])
    except Exception as e:
        print(e)