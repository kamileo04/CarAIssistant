from AiAssistant import AiAssistant
from Driver import Driver
from Car import Car
from Engine import Engine
from NavigationSystem import NavigationSystem
from SensorSystem import SensorSystem

# Tworzenie obiektów
engine = Engine(True, "Silnik 1", "ABC", 150.0, 0.0, 7.5)
navigationSystem = NavigationSystem("Warszawa", "Kraków")
sensorSystem = SensorSystem(False, 1.5)
car = Car(50.0, 0.0, "VIN123", 80.0, [], engine, navigationSystem, sensorSystem)
driver = Driver("Jan Kowalski")
aiAssistant = AiAssistant("Asystent 1", "1.0")

# Interakcje między obiektami:

# AiAssistant monitoruje Drivera
if driver.isSleepy:
    print(f"Uwaga! Kierowca {driver.name} jest śpiący!")

# AiAssistant monitoruje Car
if car.getFuelLevel() < 10:
    aiAssistant.alertLowFuel()

# Driver prowadzi Car
car.setSpeed(60.0)
print(f"Samochód jedzie z prędkością {car.getSpeed()} km/h")

# Car korzysta z Engine
print(f"Moc silnika: {car.engine.getHp()} KM")

# Car korzysta z NavigationSystem
print(f"ETA do {car.navigationSystem.destination}: {car.navigationSystem.provideETA()} minut")

# Car korzysta z SensorSystem
if car.sensorSystem.checkDoorStatus():
    print("Drzwi są otwarte!")

# AiAssistant pobiera status samochodu
car_status = aiAssistant.provideCarStatus(car)
print(f"Status samochodu: {car_status}")



