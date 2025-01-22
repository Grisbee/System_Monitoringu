import pytest

def test_suite():
    """
    Dynamiczne uruchamianie zestawów testowych w oparciu o tagi.
    """
    # Uruchom testy oznaczone jako "fast"
    pytest.main([ "-m", "fast", "FasadaTest.py"])

    # Uruchom testy oznaczone jako "complex and slow"
    pytest.main(["--no-header", "-q", "-m", "complex and slow", "FasadaTest.py"])

    # Wyklucz testy oznaczone jako "slow"
    pytest.main(["--no-header", "-q", "-m", "not slow", "FasadaTest.py"])

if __name__ == "__main__":
    test_suite()
