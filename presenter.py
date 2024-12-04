from abc import ABC, abstractmethod
from typing import List


class IModel(ABC):
    @abstractmethod
    def get_stan_alarmu(self) -> bool:
        pass

    @abstractmethod
    def get_tryb(self) -> str:
        pass

    @abstractmethod
    def set_stan_alarmu(self, stan: bool) -> None:
        pass

    @abstractmethod
    def set_tryb(self, tryb: str) -> None:
        pass

    @abstractmethod
    def getRFID(self) -> str:
        pass

    @abstractmethod
    def getDaneLogowania(self) -> str:
        pass

    @abstractmethod
    def get_kod_czujnika(self) -> int:
        pass

    @abstractmethod
    def get_rodzaj_czujnika(self) -> str:
        pass

    @abstractmethod
    def get_pomieszczenie_czujnika(self) -> str:
        pass


class IPresenter(ABC):
    @abstractmethod
    def zmien_haslo(self, haslo: str, nowe_haslo: str) -> None:
        pass

    @abstractmethod
    def login(self, login: str, haslo: str) -> None:
        pass

    @abstractmethod
    def dodaj_czujnik(self, typ: str, kod: int) -> None:
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
    def autoryzacja_rfid(self, klucz: str) -> None:
        pass


class Fasada(IPresenter):
    def aktywuj_czuwanie(self) -> None:
        pass

    def autoryzacja_rfid(self, klucz: str) -> None:
        pass

    def dezaktywuj_czuwanie(self) -> None:
        pass

    def dodaj_czujnik(self, typ: str, kod: int) -> None:
        pass

    def kalibracja_czujnika(self, kod: int, parametry: List[int]) -> None:
        pass

    def usun_czujnik(self, kod: int) -> None:
        pass

    def wlacz_alarm(self) -> None:
        pass

    def wylacz_alarm(self) -> None:
        pass

    def login(self, login: str, haslo: str) -> None:
        pass

    def zmien_haslo(self, haslo: str, nowe_haslo: str) -> None:
        pass

    def zarejestruj(self, login: str, haslo: str) -> None:
        pass

    def dodaj_kamere(self, kod: int, pomieszczenie: str) -> None:
        pass

    def usun_kamere(self, kamera) -> None:
        pass


class ObslugaAlarmu:
    def wlacz_alarm(self) -> None:
        pass

    def wylacz_alarm(self) -> None:
        pass

    def aktywuj_czuwanie(self) -> None:
        pass

    def dezaktywuj_czuwanie(self) -> None:
        pass

    def setTryb(self, tryb: str) -> None:
        pass

    def getTryb(self) -> str:
        pass

    def getStan(self) -> bool:
        pass

    def setStan(self, stan: bool) -> None:
        pass


class ObslugaKamer:
    def dodaj_kamere(self, kod: int, pomieszczenie: str) -> None:
        pass

    def usun_kamere(self, kamera) -> None:
        pass


class ObslugaCzujnikow:
    def dodaj_czujnik(self, kod: int, typ: str, pomieszczenie: str):
        pass

    def kalibracja_czujnika(self, czujnik, parametry: List[int]):
        pass

    def usun_czujnik(self, czujnik):
        pass


class ObslugaLogowania:
    def login(self, login: str, haslo: str) -> None:
        pass

    def zmien_haslo(self, haslo: str, nowe_haslo: str) -> None:
        pass

    def zarejestruj(self, login: str, haslo: str) -> None:
        pass


class AutoryzacjaRFID:
    def autoryzacja_rfid(self, klucz: str, uzytkownik) -> bool:
        pass
