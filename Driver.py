class Driver:
    def __init__(self, name: str, isSleepy: bool = False):
        self.name = name
        self.isSleepy = isSleepy

    def setSleepy(self, isSleepy: bool) -> None:
        self.isSleepy = isSleepy