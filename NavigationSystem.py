class NavigationSystem:
    def __init__(self, destination: str, currentLocation: str):
        self.destination = destination
        self.currentLocation = currentLocation

    def calculateRoute(self, destination: str) -> str:
        # Tutaj logika do obliczania trasy
        return "Trasa obliczona"

    def provideETA(self) -> int:
        # Tutaj logika do obliczania ETA
        return 60  # Przyk³adowe ETA w minutach

    def setCurrentLocation(self, currentLocation: str) -> None:
        self.currentLocation = currentLocation