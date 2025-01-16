# Klasa Dao (Data Access Object)
class Dao:
    def __init__(self):
        self.__uzytkownicy = []
        self.__czujniki = []
        self.__kamery = []

    def get_uzytkownicy(self) -> list[Uzytkownik]:
        return self.__uzytkownicy

    def get_czujniki(self) -> list[Czujnik]:
        return self.__czujniki

    def get_kamery(self) -> list[Kamera]:
        return self.__kamery

    def update_uzytkownik(self, uzytkownik: Uzytkownik) -> None:
        self.__uzytkownicy.append(uzytkownik)

    def update_czujnik(self, czujnik: Czujnik) -> None:
        self.__czujniki.append(czujnik)

    def update_kamera(self, kamera: Kamera) -> None:
        self.__kamery.append(kamera)

    def delete_uzytkownik(self, uzytkownik: Uzytkownik) -> None:
        self.__uzytkownicy.remove(uzytkownik)

    def delete_czujnik(self, czujnik: Czujnik) -> None:
        self.__czujniki.remove(czujnik)

    def delete_kamera(self, kamera: Kamera) -> None:
        self.__kamery.remove(kamera)

