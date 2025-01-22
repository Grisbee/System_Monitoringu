import unittest
import model.Fasada
from model.Czujnik import Czujnik

class TestFasada(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Przygotowanie instancji fasady dla wszystkich testów w klasie."""
        cls.fasada = model.Fasada.Fasada()

    def test_get_stan_alarmu_podstawowy(self):
        """Test podstawowy sprawdzający stan alarmu."""
        result = self.fasada.get_stan_alarmu()
        self.assertFalse(result)

    def test_operacja_podstawowa_poprawna(self):
        """Test podstawowy sprawdzający ustawienie stanu alarmu."""
        self.fasada.set_stan_alarmu(True)
        result = self.fasada.get_stan_alarmu()
        self.assertTrue(result)

    def test_operacja_zlozona_poprawna(self):
        """Test złożony sprawdzający pobranie użytkownika."""
        result = self.fasada.get_uzytkownik("barnaba")
        self.assertEqual(result.get_haslo(), "maslo")

    def test_operacja_zlozona_parametr_bledny(self):
        """Test złożony sprawdzający obsługę błędnego parametru."""
        with self.assertRaisesRegex(AttributeError, "Użytkownik o loginie 'user' nie został znaleziony."):
            self.fasada.get_uzytkownik("user")

if __name__ == '__main__':
    unittest.main()