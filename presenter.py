from abc import ABC, abstractmethod
from typing import List, Optional
from model import Dao


# Definicja interfejsu IPresenter
class IPresenter(ABC):
    @abstractmethod
    def zmien_haslo(self, haslo: str, nowe_haslo: str) -> None:
        pass

    @abstractmethod
    def login(self, login: str, haslo: str) -> None:
        pass

    @abstractmethod
    def kalibracja_czujnika(self, kod: int, parametry: List[int]) -> None:
        pass

    @abstractmethod
    def usun_czujnik(self, kod: int) -> None:
        pass

    @abstractmethod
    def wlacz_alarm(self) -> None:
        pass

    @abstractmethod
    def wylacz_alarm(self) -> None:
        pass

    @abstractmethod
    def aktywuj_czuwanie(self) -> None:
        pass

    @abstractmethod
    def dezaktywuj_czuwanie(self) -> None:
        pass

    @abstractmethod
    def zarejestruj(self, login: str, haslo: str) -> 'Uzytkownik':
        pass

    @abstractmethod
    def autoryzacja_rfid(self, klucz: str, uzytkownik: 'User') -> bool:
        pass

    @abstractmethod
    def usun_kamere(self, kamera: 'Kamera') -> None:
        pass

    @abstractmethod
    def podglad_danych(self, czujniki: List[int]) -> None:
        pass

    @abstractmethod
    def podglad_obrazu(self, tryb: str, kamery: Optional[List[bool]]) -> None:
        pass


# Implementacja Presenter
class Presenter(IPresenter):
    def __init__(self, fasada: 'Fasada'):
        self.fasada = fasada

    def zmien_haslo(self, haslo: str, nowe_haslo: str) -> None:
        self.fasada.zmien_haslo(haslo, nowe_haslo)

    def login(self, login: str, haslo: str) -> None:
        self.fasada.login(login, haslo)

    def kalibracja_czujnika(self, kod: int, parametry: List[int]) -> None:
        self.fasada.kalibracja_czujnika(kod, parametry)

    def usun_czujnik(self, kod: int) -> None:
        self.fasada.usun_czujnik(kod)

    def wlacz_alarm(self) -> None:
        self.fasada.wlacz_alarm()

    def wylacz_alarm(self) -> None:
        self.fasada.wylacz_alarm()

    def aktywuj_czuwanie(self) -> None:
        self.fasada.aktywuj_czuwanie()

    def dezaktywuj_czuwanie(self) -> None:
        self.fasada.dezaktywuj_czuwanie()

    def zarejestruj(self, login: str, haslo: str) -> 'Uzytkownik':
        return self.fasada.zarejestruj(login, haslo)

    def autoryzacja_rfid(self, klucz: str, uzytkownik: 'User') -> bool:
        return self.fasada.autoryzacja_rfid(klucz, uzytkownik)

    def usun_kamere(self, kamera: 'Kamera') -> None:
        self.fasada.usun_kamere(kamera)

    def podglad_danych(self, czujniki: List[int]) -> None:
        self.fasada.podglad_danych(czujniki)

    def podglad_obrazu(self, tryb: str, kamery: Optional[List[bool]]) -> None:
        self.fasada.podglad_obrazu(tryb, kamery)


# Definicja Fasady
class Fasada:
    def __init__(self):
        self.alarm = ObslugaAlarmu()
        self.kamery = ObslugaKamer()
        self.czujniki = ObslugaCzujnikow()
        self.logowanie = ObslugaLogowania()

    def zmien_haslo(self, haslo: str, nowe_haslo: str) -> None:
        self.logowanie.zmien_haslo(haslo, nowe_haslo)

    def login(self, login: str, haslo: str) -> None:
        self.logowanie.login(login, haslo)

    def kalibracja_czujnika(self, kod: int, parametry: List[int]) -> None:
        self.czujniki.kalibracja_czujnika(czujnik=kod, parametry=parametry)

    def usun_czujnik(self, kod: int) -> None:
        self.czujniki.usun_czujniki(kod)

    def wlacz_alarm(self) -> None:
        self.alarm.wlacz_alarm()

    def wylacz_alarm(self) -> None:
        self.alarm.wylacz_alarm()

    def aktywuj_czuwanie(self) -> None:
        self.alarm.aktywuj_czuwanie()

    def dezaktywuj_czuwanie(self) -> None:
        self.alarm.dezaktywuj_czuwanie()

    def zarejestruj(self, login: str, haslo: str) -> 'Uzytkownik':
        return self.logowanie.zarejestruj(login, haslo)

    def autoryzacja_rfid(self, klucz: str, uzytkownik: 'User') -> bool:
        return self.logowanie.autoryzacja_rfid(klucz, uzytkownik)

    def usun_kamere(self, kamera: 'Kamera') -> None:
        self.kamery.usun_kamere(kamera)

    def podglad_danych(self, czujniki: List[int]) -> None:
        self.czujniki.podglad_danych(czujniki)

    def podglad_obrazu(self, tryb: str, kamery: Optional[List[bool]]) -> None:
        self.kamery.podglad_obrazu(tryb, kamery)


# Implementacje komponentów obsługi
class ObslugaAlarmu:
    def wlacz_alarm(self) -> None:
        print("Włączanie alarmu")

    def wylacz_alarm(self) -> None:
        print("Wyłączanie alarmu")

    def aktywuj_czuwanie(self) -> None:
        print("Aktywacja czuwania")

    def dezaktywuj_czuwanie(self) -> None:
        print("Dezaktywacja czuwania")


class ObslugaKamer:
    def usun_kamere(self, kamera: 'Kamera') -> None:
        print(f"Usuwanie kamery {kamera}")
        if autoryzacja_rfid(uzytkownik):
            delete_kamera(kamera)
            print(f"Usunięto kamerę {kamera}")
        else:
            print("Brak autoryzacji")
    def podglad_obrazu(self, tryb: str, kamery: Optional[List[bool]], pomieszczenie : Optional[str]) -> None:
        print(f"Podgląd obrazu w trybie {tryb}")
        if tryb == "pomieszczenie":
            lista_kamer = Dao.get_kamery()
            lista_czujnikow = Dao.get_czujniki()

            for index in range(len(lista_kamer)):
                if lista_kamer[index].get_pomieszczenie() != pomieszczenie:
                    lista_kamer.remove(lista_kamer[index])

            for index in range(len(lista_czujnikow)):
                if lista_czujnikow[index].get_pomieszczenie() != pomieszczenie:
                    lista_czujnikow.remove(lista_czujnikow[index])

        elif tryb == "kamery":
            lista_kamer = Dao.get_kamery()
            for index in range(len(kamery)):
                if kamery[index] == False:
                    lista_kamer.remove(lista_kamer[index])


class ObslugaCzujnikow:
    def kalibracja_czujnika(self, czujnik: int, parametry: List[int]) -> None:
        print(f"Kalibracja czujnika {czujnik} z parametrami {parametry}")

    def usun_czujniki(self, czujnik: int) -> None:
        print(f"Usuwanie czujnika {czujnik}")

    def podglad_danych(self, czujniki: List[int]) -> None:
        print(f"Podgląd danych z czujników: {czujniki}")


class ObslugaLogowania:
    def login(self, login: str, haslo: str) -> None:
        print(f"Logowanie użytkownika: {login}")

    def zmien_haslo(self, haslo: str, nowe_haslo: str) -> None:
        print("Zmiana hasła")

    def zarejestruj(self, login: str, haslo: str) -> 'Uzytkownik':
        print(f"Rejestracja użytkownika: {login}")

