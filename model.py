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

    @abstractmethod
    def set_kod_czujnika(self, kod: int) -> None:
        pass

    @abstractmethod
    def set_rodzaj_czujnika(self, rodzaj: str) -> None:
        pass

    @abstractmethod
    def set_pomieszczenie_czujnika(self, pomieszczenie: str) -> None:
        pass

    @abstractmethod
    def get_kod_kamery(self) -> int:
        pass

    @abstractmethod
    def get_pomieszczenie_kamery(self) -> str:
        pass

    @abstractmethod
    def set_kod_kamery(self, kod: int) -> None:
        pass

    @abstractmethod
    def set_pomieszczenie_kamery(self, pomieszczenie: str) -> None:
        pass

    @abstractmethod
    def update_haslo(self) -> None:
        pass

    @abstractmethod
    def get_login(self) -> str:
        pass

    @abstractmethod
    def get_haslo(self) -> str:
        pass

    @abstractmethod
    def get_rola(self) -> str:
        pass


class Alarm:
    def __init__(self, stan: bool, tryb: str):
        self.stan = stan
        self.tryb = tryb

    def get_stan_alarmu(self) -> bool:
        pass

    def set_stan_alarmu(self, stan: bool) -> None:
        pass

    def get_tryb(self) -> str:
        pass

    def set_tryb(self, tryb: str) -> None:
        pass


class Czujnik:
    def __init__(self, kod: int, typ: str, pomieszczenie: str):
        self.kod = kod
        self.typ = typ
        self.pomieszczenie = pomieszczenie

    def get_kod_czujnika(self) -> int:
        pass

    def get_rodzaj_czujnika(self) -> str:
        pass

    def get_pomieszczenie_czujnika(self) -> str:
        pass

    def set_kod_czujnika(self, kod: int) -> None:
        pass

    def set_rodzaj_czujnika(self, rodzaj: str) -> None:
        pass

    def set_pomieszczenie_czujnika(self, pomieszczenie: str) -> None:
        pass


class Kamera:
    def __init__(self, kod: int, pomieszczenie: str):
        self.kod = kod
        self.pomieszczenie = pomieszczenie

    def get_pomieszczenie_kamery(self) -> str:
        pass

    def get_kod_kamery(self) -> int:
        pass

    def set_pomieszczenie_kamery(self, pomieszczenie: str) -> None:
        pass

    def set_kod_kamery(self, kod: int) -> None:
        pass


class Uzytkownik:
    def __init__(self, login: str, haslo: str, rola: str):
        self.login = login
        self.haslo = haslo
        self.rola = rola

    def update_haslo(self) -> None:
        pass

    def get_login(self) -> str:
        pass

    def get_haslo(self) -> str:
        pass

    def get_rola(self) -> str:
        pass


class IDao(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def delete(self, obj):
        pass

    @abstractmethod
    def getAll(self) -> List:
        pass

    @abstractmethod
    def update(self, obj):
        pass


class DaoCzujnik(IDao):
    def get(self) -> Czujnik:
        pass

    def delete(self, czujnik: Czujnik) -> None:
        pass

    def getAll(self) -> List[Czujnik]:
        pass

    def update(self, czujnik: Czujnik) -> None:
        pass


class DaoKamera(IDao):
    def get(self) -> Kamera:
        pass

    def delete(self, kamera: Kamera) -> None:
        pass

    def getAll(self) -> List[Kamera]:
        pass

    def update(self, kamera: Kamera) -> None:
        pass


class DaoUzytkownik(IDao):
    def get(self) -> Uzytkownik:
        pass

    def delete(self, uzytkownik: Uzytkownik) -> None:
        pass

    def getAll(self) -> List[Uzytkownik]:
        pass

    def update(self, uzytkownik: Uzytkownik) -> None:
        pass


class Fasada(IModel):
    def get_stan_alarmu(self) -> bool:
        pass

    def get_tryb(self) -> str:
        pass

    def set_stan_alarmu(self, stan: bool) -> None:
        pass

    def set_tryb(self, tryb: str) -> None:
        pass

    def getRFID(self) -> str:
        pass

    def getDaneLogowania(self) -> str:
        pass

    def get_kod_czujnika(self) -> int:
        pass

    def get_rodzaj_czujnika(self) -> str:
        pass

    def get_pomieszczenie_czujnika(self) -> str:
        pass

    def set_kod_czujnika(self, kod: int) -> None:
        pass

    def set_rodzaj_czujnika(self, rodzaj: str) -> None:
        pass

    def set_pomieszczenie_czujnika(self, pomieszczenie: str) -> None:
        pass

    def get_kod_kamery(self) -> int:
        pass

    def get_pomieszczenie_kamery(self) -> str:
        pass

    def set_kod_kamery(self, kod: int) -> None:
        pass

    def set_pomieszczenie_kamery(self, pomieszczenie: str) -> None:
        pass

    def update_haslo(self) -> None:
        pass

    def get_login(self) -> str:
        pass

    def get_haslo(self) -> str:
        pass

    def get_rola(self) -> str:
        pass
