# Klasa Urzadzenie
class Urzadzenie:
    def __init__(self, kod: int, pomieszczenie: str):
        self.__kod = kod
        self.__pomieszczenie = pomieszczenie

    def get_kod(self) -> int:
        return self.__kod

    def set_kod(self, kod: int) -> None:
        self.__kod = kod

    def get_pomieszczenie(self) -> str:
        return self.__pomieszczenie

    def set_pomieszczenie(self, pomieszczenie: str) -> None:
        self.__pomieszczenie = pomieszczenie

