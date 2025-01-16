# Klasa FabrykaKamer implementuje FabrykaUrzadzen
class FabrykaKamer(FabrykaUrzadzen):
    def dodaj_urzadzenie(self, kod: int, pomieszczenie: str) -> Kamera:
        return Kamera(kod, pomieszczenie)
