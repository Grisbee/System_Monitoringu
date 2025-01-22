import pytest
import model.Fasada
from model.Czujnik import Czujnik


@pytest.fixture(scope="module")
def fasada_instance():
    """Przygotowanie instancji fasady dla testów."""
    return model.Fasada.Fasada()

# Testy podstawowe
@pytest.mark.fast
def test_get_stan_alarmu_podstawowy(fasada_instance):
    result = fasada_instance.get_stan_alarmu()
    assert result == False

@pytest.mark.slow
def test_operacja_podstawowa_poprawna(fasada_instance):
    fasada_instance.set_stan_alarmu(True)
    result = fasada_instance.get_stan_alarmu()
    assert result == True

# Testy złożone

@pytest.mark.complex
def test_operacja_zlozona_poprawna(fasada_instance):
    result = fasada_instance.get_uzytkownik("barnaba")
    assert result.get_haslo() == "maslo"

@pytest.mark.slow
@pytest.mark.complex
def test_operacja_zlozona_parametr_bledny(fasada_instance):
    with pytest.raises(AttributeError, match="Użytkownik o loginie 'user' nie został znaleziony."):
        fasada_instance.get_uzytkownik("user")

