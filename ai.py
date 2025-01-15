import google.generativeai as genai
import obslugaobd
from Car import Car
from Driver import Driver
from Engine import Engine
from NavigationSystem import NavigationSystem
from SensorSystem import SensorSystem
from AiAssistant import AiAssistant
import speech_recognition as sr
import pyttsx3

with open("C:/api.txt", "r") as file: #podmien na swoj klucz api
    api_key = file.read().strip()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
system_instruction = ("")

engine = Engine(True, "Silnik 1", "ABC", 150.0, 0.0, 7.5)
navigationSystem = NavigationSystem("Wadowice", "Bielsko-Biała")
sensorSystem = SensorSystem(False, 1.5)
car = Car(50.0, 0.0, "VIN123", 80.0, [], engine, navigationSystem, sensorSystem)
driver = Driver("Kierowca") # zmien imie na swoje
aiAssistant = AiAssistant("Asystent 1", "1.0", model, system_instruction)

def read_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
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

while True:
    try:
        car_data = obslugaobd.get_car_data()
        if car_data:
            car.set_obd_data(car_data)
            print("Dane z OBD-II zostały zaktualizowane.")
    except Exception as e:
        print(f"Wystąpił‚ błąd podczas pobierania danych z OBD-II: {e}")

    user_input = recognize_speech_from_mic()

    if user_input:
        response = aiAssistant.generate_response(user_input, car) 
        print("Odpowiedź AI: " + response)
        read_text(response)

    if obslugaobd.connection and obslugaobd.connection.is_connected():
        obslugaobd.connection.close()