import pytest
import model.Fasada

class FasadaTest():

    @pytest.fixture(scope="module")
    def fasada_instance(self):
        """Przygotowanie instancji fasady dla testów."""
        return model.Fasada.Fasada()

    # Testy podstawowe
    @pytest.mark.fast
    def test_get_stan_alarmu_podstawowy(fasada_instance):
        result = fasada_instance.get_stan_alarmu()
        assert result == False

    @pytest.mark.fast
    def test_operacja_podstawowa_poprawna(fasada_instance):
        fasada_instance.set_stan_alarmu(True)
        result = fasada_instance.get_stan_alarmu()
        assert result == True

    @pytest.mark.fast
    def test_operacja_podstawowa_bledna(fasada_instance):
        with pytest.raises(ValueError, match="Dane nie mogą być puste"):
            fasada_instance.set_stan_alarmu()
            result = fasada_instance.get_stan_alarmu()
            assert result == True

    # Testy złożone
    @pytest.mark.slow
    @pytest.mark.complex
    def test_operacja_zlozona_poprawna(fasada_instance):
        result = fasada_instance.operacja_złożona("dane", 10)
        assert result == "Przetworzono złożoną operację dla dane z parametrem 10"

    @pytest.mark.slow
    @pytest.mark.complex
    def test_operacja_zlozona_parametr_bledny(fasada_instance):
        with pytest.raises(ValueError, match="Parametr musi być dodatni"):
            fasada_instance.operacja_złożona("dane", -1)
