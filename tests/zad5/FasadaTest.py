import pytest
import model.Fasada

class FasadaTest(pytest.Pytest):

    @pytest.fixture(scope="module")
    def fasada_instance(self):
        """Przygotowanie instancji fasady dla testów."""
        return model.Fasada.Fasada()

    # Testy podstawowe
    @pytest.mark.fast
    def test_operacja_podstawowa_poprawna(fasada_instance):
        result = fasada_instance.get_stan_alarmu()
        assert result == True

    @pytest.mark.fast
    def test_operacja_podstawowa_błędna(fasada_instance):
        with pytest.raises(ValueError, match="Dane nie mogą być puste"):
            fasada_instance.operacja_podstawowa("")

    # Testy złożone
    @pytest.mark.slow
    @pytest.mark.complex
    def test_operacja_złożona_poprawna(fasada_instance):
        result = fasada_instance.operacja_złożona("dane", 10)
        assert result == "Przetworzono złożoną operację dla dane z parametrem 10"

    @pytest.mark.slow
    @pytest.mark.complex
    def test_operacja_złożona_parametr_błędny(fasada_instance):
        with pytest.raises(ValueError, match="Parametr musi być dodatni"):
            fasada_instance.operacja_złożona("dane", -1)
