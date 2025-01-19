import pytest

def test_suite():
    """
    Uruchomienie dynamicznego zestawu testów.
    """
    # Uruchom testy oznaczone jako 'fast'
    pytest.main(["-m", "fast"])

    # Uruchom testy oznaczone jako 'complex' i 'slow'
    pytest.main(["-m", "complex and slow"])

    # Wyklucz testy oznaczone jako 'slow'
    pytest.main(["-m", "not slow"])
