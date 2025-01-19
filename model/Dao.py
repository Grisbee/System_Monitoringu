# Klasa Dao (Data Access Object)
from model.Kamera import Kamera
from model.Czujnik import Czujnik
from model.Uzytkownik import Uzytkownik
from data.dane import get_lista_kamer, get_lista_czujnikow
from model.Urzadzenie import Urzadzenie
class Dao:
    def __init__(self):
        self.__uzytkownicy = []
        self.__czujniki = []

    def get_uzytkownicy(self) -> list[Uzytkownik]:
        return self.__uzytkownicy

    @staticmethod
    def get_czujniki():
        return get_lista_czujnikow()

    @staticmethod
    def get_kamery():
        return get_lista_kamer()

    def update_uzytkownik(self, uzytkownik: Uzytkownik) -> None:
        self.__uzytkownicy.append(uzytkownik)

    def update_czujnik(self, czujnik: Czujnik) -> None:
        self.__czujniki.append(czujnik)

    @staticmethod
    def update_kamera(kamera: Kamera) -> None:
        lista_kamer = get_lista_kamer()
        lista_kamer.append(kamera)



    def delete_uzytkownik(self, uzytkownik: Uzytkownik) -> None:
        self.__uzytkownicy.remove(uzytkownik)

    def delete_czujnik(self, czujnik: Czujnik) -> None:
        self.__czujniki.remove(czujnik)

    def delete_kamera(self, kamera: Kamera) -> None:
        lista_kamer = get_lista_kamer()
        lista_kamer.remove(kamera)



