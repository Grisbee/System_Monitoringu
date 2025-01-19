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

    def usun_kamere(self, kamera: 'Kamera') -> None:
        self.kamery.usun_kamere(kamera)

    def podglad_danych(self, czujniki: List[int]) -> None:
        self.czujniki.podglad_danych(czujniki)

    def podglad_obrazu(self, tryb: str, kamery: Optional[List[bool]], pomieszczenie: Optional[List[string]]) -> None:
        self.kamery.podglad_obrazu(tryb, kamery, pomieszczenie)
