import unittest
from unittest import mock
from model.Alarm import Alarm  # Zakładając, że Alarm to klasa, którą chcesz zamockować
from model.Fasada import Fasada  # Twoja klasa Fasada

class TestFasada(unittest.TestCase):

    # Testy dla metod get_stan_alarmu i set_stan_alarmu
    @mock.patch.object(Alarm, 'get_stan_alarmu', return_value=True)
    def test_get_stan_alarmu(self, mock_get_stan_alarmu):
        fasada = Fasada()
        stan_alarmu = fasada.get_stan_alarmu()
        self.assertTrue(stan_alarmu, "Stan alarmu powinien być True.")
        mock_get_stan_alarmu.assert_called_once()

    @mock.patch.object(Alarm, 'set_stan_alarmu')
    def test_set_stan_alarmu(self, mock_set_stan_alarmu):
        fasada = Fasada()
        fasada.set_stan_alarmu(False)
        mock_set_stan_alarmu.assert_called_once_with(False)

    @mock.patch.object(Alarm, 'set_stan_alarmu')
    @mock.patch.object(Alarm, 'get_stan_alarmu', return_value=False)
    def test_get_and_set_stan_alarmu(self, mock_get_stan_alarmu, mock_set_stan_alarmu):
        fasada = Fasada()
        fasada.set_stan_alarmu(True)
        mock_set_stan_alarmu.assert_called_once_with(True)
        stan_alarmu = fasada.get_stan_alarmu()
        self.assertFalse(stan_alarmu, "Stan alarmu powinien być False.")
        mock_get_stan_alarmu.assert_called_once()

    # Testy dla metod get_tryb i set_tryb
    @mock.patch.object(Alarm, 'get_tryb', return_value="manualny")
    def test_get_tryb(self, mock_get_tryb):
        fasada = Fasada()
        tryb = fasada.get_tryb()
        self.assertEqual(tryb, "manualny", "Tryb alarmu powinien być 'manualny'.")
        mock_get_tryb.assert_called_once()

    @mock.patch.object(Alarm, 'set_tryb')
    def test_set_tryb(self, mock_set_tryb):
        fasada = Fasada()
        fasada.set_tryb("automatyczny")
        mock_set_tryb.assert_called_once_with("automatyczny")

    @mock.patch.object(Alarm, 'set_tryb')
    @mock.patch.object(Alarm, 'get_tryb', return_value="automatyczny")
    def test_get_and_set_tryb(self, mock_get_tryb, mock_set_tryb):
        fasada = Fasada()
        fasada.set_tryb("manualny")
        mock_set_tryb.assert_called_once_with("manualny")
        tryb = fasada.get_tryb()
        self.assertEqual(tryb, "automatyczny", "Tryb alarmu powinien być 'automatyczny'.")
        mock_get_tryb.assert_called_once()

if __name__ == '__main__':
    unittest.main()
