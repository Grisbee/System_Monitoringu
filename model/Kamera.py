from model.Urzadzenie import Urzadzenie

class Kamera(Urzadzenie):
    def __init__(self, kod: int, pomieszczenie: str):
        super().__init__(kod, pomieszczenie)

    def set_pomieszczenie_kamery(self, pomieszczenie: str) -> None:
        try:
            pomieszczenie.strip()
            self.set_pomieszczenie(pomieszczenie)
        except Exception as e:
            print("Blad! " + str(e))

    def set_kod_kamery(self, kod: int) -> None:
        try:
            if kod >= 0:
                self.set_kod(kod)
        except Exception as e:
            print("Blad! " + str(e))


