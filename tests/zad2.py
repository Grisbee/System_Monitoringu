import unittest
from parameterized import parameterized
from model.Kamera import Kamera  # Zmodyfikuj import na właściwy dla Twojego projektu


class TestKamery(unittest.TestCase):
    # Metoda odpowiedzialna za setup przed każdym testem (odpowiednik @BeforeEach)
    def setUp(self):
        self.kamera = Kamera(1, "schody")  # Przykładowa inicjalizacja obiektu

    # Testy
    # Test jednostkowy
    def test_kamery_1(self):
        result = self.kamera.get_pomieszczenie()  # Dopasuj do metody testowanej w klasie Kamera
        self.assertEqual(result, "schody", "Pomieszczenie to 'schody'")

    # Test parametryzowany z CsvSource
    @parameterized.expand([
        ("korytarz", 1, "1korytarz"),
        ("lobby", 3, "3lobby"),
    ])
    def test_kamery_parameterized_1(self, nazwa, id, expected_result):
        self.kamera.set_pomieszczenie(nazwa)
        self.kamera.set_kod(id)
        result = str(self.kamera.get_kod())+self.kamera.get_pomieszczenie()
        self.assertEqual(result, expected_result)

    def test_kamery_z_wyjatkami(self):

        with self.assertRaises(TypeError):
            self.kamera.set_pomieszczenie_kamery(pomieszczenie=False)


        with self.assertRaises(TypeError):
            self.kamera.set_kod_kamery("abc")


if __name__ == "__main__":
    unittest.main()
