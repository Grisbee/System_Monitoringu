# Klasa Kamera dziedziczy po Urzadzenie
class Kamera(Urzadzenie):
    def __init__(self, kod: int, pomieszczenie: str):
        super().__init__(kod, pomieszczenie)

    def set_pomieszczenie_kamery(self, pomieszczenie: str) -> None:
        self.set_pomieszczenie(pomieszczenie)

    def set_kod_kamery(self, kod: int) -> None:
        self.set_kod(kod)
