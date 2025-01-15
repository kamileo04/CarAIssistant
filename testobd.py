import unittest
from unittest.mock import patch, MagicMock
import obslugaobd

class TestObslugaOBD(unittest.TestCase):

    @patch('obslugaobd.obd')
    def test_get_car_data(self, mock_obd):
        mock_connection = MagicMock()
        mock_connection.is_connected.return_value = True
        mock_obd.OBD.return_value = mock_connection

        mock_response = MagicMock()
        mock_response.is_null.return_value = False
        mock_response.value = 100

        mock_connection.query.return_value = mock_response

        car_data = obslugaobd.get_car_data()
        self.assertIsNotNone(car_data)
        self.assertEqual(car_data["rpm"], 100)
        self.assertEqual(car_data["turbo"], 100)
        self.assertEqual(car_data["maf"], 100)
        self.assertEqual(car_data["oilTemp"], 100)
        self.assertEqual(car_data["speed"], 100)
        self.assertEqual(car_data["fuel"], 100)
        self.assertEqual(car_data["throttlePosition"], 100)


    @patch('obslugaobd.obd')
    def test_get_car_data_no_connection(self, mock_obd):
        mock_connection = MagicMock()
        mock_connection.is_connected.return_value = False
        mock_obd.OBD.return_value = mock_connection

        car_data = obslugaobd.get_car_data()
        self.assertIsNone(car_data)

    @patch('obslugaobd.obd')
    def test_get_car_data_invalid_rpm(self, mock_obd):
        mock_connection = MagicMock()
        mock_connection.is_connected.return_value = True
        mock_obd.OBD.return_value = mock_connection

        mock_response = MagicMock()
        mock_response.is_null.return_value = False
        mock_response.value = -1
        
        mock_connection.query.return_value = mock_response

        car_data = obslugaobd.get_car_data()
        self.assertIsNone(car_data)


if __name__ == '__main__':
    unittest.main()