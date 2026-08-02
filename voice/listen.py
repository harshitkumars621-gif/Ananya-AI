import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():

    with sr.Microphone() as source:

        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio, language="hi-IN")

        print("👤 Harshit:", text)

        return text

    except sr.UnknownValueError:

        return ""

    except Exception as e:

        print(e)
        return ""