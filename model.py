from typing import Optional


# Klasa Alarm
class Alarm:
    def __init__(self, stan: bool, tryb: str):
        self.__stan = stan
        self.__tryb = tryb

    def get_stan_alarmu(self) -> bool:
        return self.__stan

    def set_stan_alarmu(self, stan: bool) -> None:
        self.__stan = stan

    def get_tryb(self) -> str:
        return self.__tryb

    def set_tryb(self, tryb: str) -> None:
        self.__tryb = tryb


# Klasa Uzytkownik
class Uzytkownik:
    def __init__(self, login: str, haslo: str, rfid: str):
        self.__login = login
        self.__haslo = haslo
        self.__rfid = rfid

    def get_login(self) -> str:
        return self.__login

    def get_haslo(self) -> str:
        return self.__haslo

    def get_RFID(self) -> str:
        return self.__rfid

    def set_login(self, login: str) -> None:
        self.__login = login

    def set_haslo(self, haslo: str) -> None:
        self.__haslo = haslo

    def set_RFID(self, rfid: str) -> None:
        self.__rfid = rfid


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


# Klasa Czujnik dziedziczy po Urzadzenie
class Czujnik(Urzadzenie):
    def __init__(self, kod: int, pomieszczenie: str, typ: str, rodzaj: str):
        super().__init__(kod, pomieszczenie)
        self.__typ = typ
        self.__rodzaj = rodzaj

    def get_typ(self) -> str:
        return self.__typ

    def set_typ(self, typ: str) -> None:
        self.__typ = typ

    def get_rodzaj_czujnika(self) -> str:
        return self.__rodzaj

    def set_rodzaj_czujnika(self, rodzaj: str) -> None:
        self.__rodzaj = rodzaj


# Klasa Kamera dziedziczy po Urzadzenie
class Kamera(Urzadzenie):
    def __init__(self, kod: int, pomieszczenie: str):
        super().__init__(kod, pomieszczenie)

    def set_pomieszczenie_kamery(self, pomieszczenie: str) -> None:
        self.set_pomieszczenie(pomieszczenie)

    def set_kod_kamery(self, kod: int) -> None:
        self.set_kod(kod)


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

    def zapisz_uzytkownika(self, uzytkownik: Uzytkownik) -> None:
        self.__uzytkownicy.append(uzytkownik)

    def zapisz_czujnik(self, czujnik: Czujnik) -> None:
        self.__czujniki.append(czujnik)

    def zapisz_kamere(self, kamera: Kamera) -> None:
        self.__kamery.append(kamera)

    def usun_uzytkownika(self, uzytkownik: Uzytkownik) -> None:
        self.__uzytkownicy.remove(uzytkownik)

    def usun_czujnik(self, czujnik: Czujnik) -> None:
        self.__czujniki.remove(czujnik)

    def usun_kamere(self, kamera: Kamera) -> None:
        self.__kamery.remove(kamera)


# Klasa Fasada - centralny punkt modelu
class Fasada:
    def __init__(self):
        self.__alarm = Alarm(False, "")
        self.__uzytkownik = None
        self.__dao = Dao()

    # Metody zarządzające Alarmem
    def get_stan_alarmu(self) -> bool:
        return self.__alarm.get_stan_alarmu()

    def set_stan_alarmu(self, stan: bool) -> None:
        self.__alarm.set_stan_alarmu(stan)

    def get_tryb(self) -> str:
        return self.__alarm.get_tryb()

    def set_tryb(self, tryb: str) -> None:
        self.__alarm.set_tryb(tryb)

    # Metody zarządzania Uzytkownikami
    def zapisz_uzytkownika(self, uzytkownik: Uzytkownik) -> None:
        self.__dao.zapisz_uzytkownika(uzytkownik)

    def usun_uzytkownika(self, uzytkownik: Uzytkownik) -> None:
        self.__dao.usun_uzytkownika(uzytkownik)

    def get_uzytkownik(self, login: str) -> Optional[Uzytkownik]:
        for uzytkownik in self.__dao.get_uzytkownicy():
            if uzytkownik.get_login() == login:
                return uzytkownik
        return None

    # Metody zarządzania Czujnikami
    def zapisz_czujnik(self, czujnik: Czujnik) -> None:
        self.__dao.zapisz_czujnik(czujnik)

    def usun_czujnik(self, czujnik: Czujnik) -> None:
        self.__dao.usun_czujnik(czujnik)

    # Metody zarządzania Kamerami
    def zapisz_kamere(self, kamera: Kamera) -> None:
        self.__dao.zapisz_kamere(kamera)

    def usun_kamere(self, kamera: Kamera) -> None:
        self.__dao.usun_kamere(kamera)

