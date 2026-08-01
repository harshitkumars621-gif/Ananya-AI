import subprocess

def speak(text):
    try:
        subprocess.run(["say", text])
    except:
        pass