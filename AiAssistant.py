from Car import Car
from Driver import Driver

class AiAssistant:
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version

    def provideCarStatus(self, car: Car) -> str:
        # Tutaj logika do pobierania statusu samochodu, np. z obiektu Car
        status = f"Fuel Level: {car.getFuelLevel()}, Speed: {car.getSpeed()}, Battery Charge: {car.getBatteryCharge()}"
        return status

    def alertLowFuel(self) -> None:
        # Tutaj logika do powiadamiania o niskim poziomie paliwa
        print("Uwaga! Niski poziom paliwa!")

    def setVersion(self, version: str) -> None:
        self.version = version



