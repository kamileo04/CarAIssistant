import speech_recognition as sr
print(sr.__version__)
import pyttsx3 

def read_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Proszę mówić...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="pl-PL")
        print("Rozpoznany tekst: " + text)
        return text
    except sr.UnknownValueError:
        print("Nie udało się rozpoznać mowy")
        return None
    except sr.RequestError:
        print("Błąd połączenia z serwerem rozpoznawania mowy")
        return None

if __name__ == "main":
    text = recognize_speech_from_mic()
    if text:
        read_text(text)