# Klasa FabrykaCzujnikow implementuje FabrykaUrzadzen
class FabrykaCzujnikow(FabrykaUrzadzen):
    def dodaj_urzadzenie(self, kod: int, typ: str, pomieszczenie: str) -> Czujnik:
        return Czujnik(kod, pomieszczenie, typ)

