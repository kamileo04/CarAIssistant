class SensorSystem:
    def __init__(self, isDoorOpen: bool, turboPressure: float):
        self.isDoorOpen = isDoorOpen
        self.turboPressure = turboPressure

    def checkDoorStatus(self) -> bool:
        return self.isDoorOpen

    def setTurboPressure(self, turboPressure: float) -> None:
        self.turboPressure = turboPressure