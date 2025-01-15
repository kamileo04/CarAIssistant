from Car import Car
from Driver import Driver
import google.generativeai as genai

class AiAssistant:
    def __init__(self, name: str, version: str, model: genai.GenerativeModel, system_instruction: str):
        self.name = name
        self.version = version
        self.model = model
        self.system_instruction = system_instruction

    def provideCarStatus(self, car: Car) -> str:
        status = (
            f"Obroty silnika: {car.rpm}\n"
            f"Ciœnienie turbo: {car.turbo}\n"
            f"Przep³yw powietrza: {car.maf}\n"
            f"Prêdkoœæ pojazdu: {car.speed}\n"
            f"Pozycja przepustnicy: {car.throttlePosition}\n"
            f"Poziom na³adowania baterii: {car.getBatteryCharge()}\n"
            f"Czy s¹ otwarte drzwi: {'Tak' if car.sensorSystem.checkDoorStatus() else 'Nie'}\n"
            f"Cel podró¿y: {car.navigationSystem.destination}\n"
            f"Aktualna lokalizacja: {car.navigationSystem.currentLocation}\n"
            f"Szacowany czas dotarcia do celu: {car.navigationSystem.provideETA()} minut"
        )
        return status

    def alertLowFuel(self) -> None:
        print("Uwaga! Niski poziom paliwa!")

    def setVersion(self, version: str) -> None:
        self.version = version

    def generate_response(self, prompt: str, car: Car) -> str:
        car_status = self.provideCarStatus(car)
        full_prompt = f"{self.system_instruction} {prompt}\n\nAktualny stan samochodu:\n{car_status}"
        response = self.model.generate_content(full_prompt)
        return response.text
