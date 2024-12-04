from abc import ABC, abstractmethod

class iPresenter(ABC):
    @abstractmethod
    def zmien_haslo(self, haslo: str, nowe_haslo: str):
        pass

    @abstractmethod
    def login(self, login: str, haslo: str):
        pass

    @abstractmethod
    def dodaj_czujnik(self, typ: str, kod: int):
        pass

    @abstractmethod
    def kalibracja_czujnika(self, kod: int, parametry: list[int]):
        pass

    @abstractmethod
    def usun_czujnik(self, kod: int):
        pass

    @abstractmethod
    def wlacz_alarm(self):
        pass

    @abstractmethod
    def wylacz_alarm(self):
        pass

    @abstractmethod
    def aktywuj_czuwanie(self):
        pass

    @abstractmethod
    def dezaktywuj_czuwanie(self):
        pass

    @abstractmethod
    def autoryzacja_rfid(self, klucz: str):
        pass


class Widok:
    def wyswietl_panel_logowania(self):
        pass


class WidokOchroniarza(Widok):
    def wyswietl_formularz_kalibracja_czujnikow(self):
        pass

    def wyswietl_formularz_dodawania_czujnikow(self):
        pass

    def wyswietl_formularz_zmiany_hasla(self):
        pass

    def wyswietl_podglad_z_kamer(self):
        pass

    def wyswietl_dane_z_czujnikow(self):
        pass

    def wyswietl_panel_podgladu(self):
        pass

    def autoryzacja_popup(self):
        pass


class WidokAdministratora(Widok):
    def wyswietl_panel_sterowania_alarmem(self):
        pass

    def wyswietl_kamery_czujniki(self):
        pass


class Aplikacja:
    def main(self):
        pass
