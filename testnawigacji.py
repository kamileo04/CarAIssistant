import unittest
from NavigationSystem import NavigationSystem

class TestNavigationSystem(unittest.TestCase):

    def setUp(self):
        self.navigation_system = NavigationSystem("Warszawa", "Kraków")

    def test_calculate_route(self):
        self.assertEqual(self.navigation_system.calculateRoute("Gdańsk"), "Trasa obliczona")

    def test_provide_eta(self):
        self.assertEqual(self.navigation_system.provideETA(), 60)

    def test_set_current_location(self):
        self.navigation_system.setCurrentLocation("Poznań")
        self.assertEqual(self.navigation_system.currentLocation, "Poznań")

if __name__ == '__main__':
    unittest.main()




