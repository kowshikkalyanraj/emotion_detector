import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("🗣️ You said:", text)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand your voice."
    except sr.RequestError:
        return "Sorry, there was an issue with the speech recognition service."
