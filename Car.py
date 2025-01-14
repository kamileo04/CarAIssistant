from Engine import Engine
from NavigationSystem import NavigationSystem
from SensorSystem import SensorSystem

class Car:
    def __init__(self, fuelLevel: float, speed: float, vin: str, batteryCharge: float, errorList: list[str],
                 engine: Engine, navigationSystem: NavigationSystem, sensorSystem: SensorSystem):
        self.fuelLevel = fuelLevel
        self.speed = speed
        self.vin = vin
        self.batteryCharge = batteryCharge
        self.errorList = errorList
        self.engine = engine
        self.navigationSystem = navigationSystem
        self.sensorSystem = sensorSystem
        self.rpm = None
        self.turbo = None
        self.maf = None
        self.throttlePosition = None

    def getFuelLevel(self) -> float:
        return self.fuelLevel

    def getSpeed(self) -> float:
        return self.speed

    def getVin(self) -> str:
        return self.vin

    def getBatteryCharge(self) -> float:
        return self.batteryCharge

    def setSpeed(self, speed: float) -> None:
        self.speed = speed

    def setFuelLevel(self, fuelLevel: float) -> None:
        self.fuelLevel = fuelLevel

    def set_obd_data(self, data: dict):
        self.rpm = data.get("rpm")
        self.turbo = data.get("turbo")
        self.maf = data.get("maf")
        self.oilTemp = data.get("oilTemp")
        self.speed = data.get("speed")
        self.fuel = data.get("fuel")
        self.throttlePosition = data.get("throttlePosition")