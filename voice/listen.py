import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("DEBUG:", text)
        print("Harshit:", text)
        return text.lower()

    except Exception:
        return ""