class Engine:
    def __init__(self, isEngineRunning: bool, name: str, code: str, hp: float, speed: float, consumption: float):
        self.isEngineRunning = isEngineRunning
        self.name = name
        self.code = code
        self.hp = hp
        self.speed = speed
        self.consumption = consumption

    def getName(self) -> str:
        return self.name

    def getCode(self) -> str:
        return self.code

    def getHp(self) -> float:
        return self.hp

    def getSpeed(self) -> float:
        return self.speed

    def setConsumption(self, consumption: float) -> None:
        self.consumption = consumption