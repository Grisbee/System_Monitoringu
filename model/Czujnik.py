# Klasa Czujnik dziedziczy po Urzadzenie
class Czujnik(Urzadzenie):
    def __init__(self, kod: int, pomieszczenie: str, typ: str):
        super().__init__(kod, pomieszczenie)
        self.__typ = typ

    def get_rodzaj_czujnika(self) -> str:
        return self.__typ

    def set_rodzaj_czujnika(self, rodzaj: str) -> None:
        self.__typ = rodzaj
