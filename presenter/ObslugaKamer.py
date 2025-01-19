from typing import Optional, List

from model.Kamera import Kamera
from model.Czujnik import Czujnik
from model.Uzytkownik import Uzytkownik
from data.dane import get_lista_kamer
from model.Urzadzenie import Urzadzenie
from model.Dao import Dao
from view.Aplikacja import uzytkownik


class ObslugaKamer:
    @staticmethod
    def usun_kamere(self, kamera: 'Kamera') -> None:
        print(f"Usuwanie kamery {kamera}")
        if self.autoryzacja_rfid(uzytkownik):
            Dao.delete_kamera(kamera)
            print(f"Usunięto kamerę {kamera}")
        else:
            print("Brak autoryzacji")

    @staticmethod
    def podglad_obrazu(tryb: str, kamery: List[bool]=None, pomieszczenie : Optional[str] = None) -> None:
        print(f"Podgląd obrazu w trybie {tryb}")
        if tryb == "pomieszczenie":
            lista_kamer = Dao.get_kamery()
            lista_czujnikow = Dao.get_czujniki()

            nowa_lista_kamer = []
            nowa_lista_czujnikow = []
            for kamera in lista_kamer:
                if kamera.get_pomieszczenie() == pomieszczenie:
                    nowa_lista_kamer.append(kamera)

            for czujnik in lista_czujnikow:
                if czujnik.get_pomieszczenie() == pomieszczenie:
                    nowa_lista_czujnikow.append(czujnik)

            return nowa_lista_kamer + nowa_lista_czujnikow

        elif tryb == "kamery":
            nowa_lista_kamer = []
            lista_kamer = Dao.get_kamery()
            for a in range(len(kamery)):
                if kamery[a]:
                    nowa_lista_kamer.append(lista_kamer[a])
            return nowa_lista_kamer

    @staticmethod
    def autoryzacja_rfid(self, uzytkownik: 'User') -> bool:

        if uzytkownik.get_rfid() == True:
            return True
        else:
            return False


czujniki_korytarz = ObslugaKamer.podglad_obrazu(tryb="pomieszczenie", pomieszczenie="korytarz")
print(czujniki_korytarz)

czujniki_lista = ObslugaKamer.podglad_obrazu(tryb="kamery", kamery=[True, True, False, False, False])
print(czujniki_lista)


