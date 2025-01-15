import unittest
from unittest.mock import patch, MagicMock
import speech_recognition as sr
from TTS import read_text, recognize_speech_from_mic

class TestSpeechRecognition(unittest.TestCase):
    
    @patch("TTS.pyttsx3.init")
    def test_read_text(self, mock_init):
        # Mockowanie metody pyttsx3
        mock_engine = MagicMock()
        mock_init.return_value = mock_engine

        # Testowana funkcja
        read_text("Testowy tekst")

        # Sprawdzenie, czy metody zostały wywołane
        mock_engine.say.assert_called_once_with("Testowy tekst")
        mock_engine.runAndWait.assert_called_once()

    @patch("TTS.sr.Microphone")
    @patch("TTS.sr.Recognizer")
    def test_recognize_speech_from_mic_success(self, mock_recognizer_class, mock_microphone_class):
        # Mockowanie rozpoznawania mowy
        mock_recognizer = MagicMock()
        mock_recognizer_class.return_value = mock_recognizer
        mock_audio = MagicMock()
        mock_recognizer.listen.return_value = mock_audio
        mock_recognizer.recognize_google.return_value = "Testowy tekst"

        # Wywołanie funkcji
        text = recognize_speech_from_mic()

        # Sprawdzenie poprawnego wyniku
        self.assertEqual(text, "Testowy tekst")
        mock_recognizer.adjust_for_ambient_noise.assert_called_once()
        mock_recognizer.listen.assert_called_once()

    @patch("TTS.sr.Microphone")
    @patch("TTS.sr.Recognizer")
    def test_recognize_speech_from_mic_unknown_value_error(self, mock_recognizer_class, mock_microphone_class):
        # Symulowanie błędu rozpoznawania mowy
        mock_recognizer = MagicMock()
        mock_recognizer_class.return_value = mock_recognizer
        mock_recognizer.recognize_google.side_effect = sr.UnknownValueError()

        # Wywołanie funkcji
        text = recognize_speech_from_mic()

        # Sprawdzenie wyniku w przypadku błędu
        self.assertIsNone(text)

    @patch("TTS.sr.Microphone")
    @patch("TTS.sr.Recognizer")
    def test_recognize_speech_from_mic_request_error(self, mock_recognizer_class, mock_microphone_class):
        # Symulowanie błędu połączenia
        mock_recognizer = MagicMock()
        mock_recognizer_class.return_value = mock_recognizer
        mock_recognizer.recognize_google.side_effect = sr.RequestError()

        # Wywołanie funkcji
        text = recognize_speech_from_mic()

        # Sprawdzenie wyniku w przypadku błędu
        self.assertIsNone(text)

if __name__ == "__main__":
    unittest.main()
