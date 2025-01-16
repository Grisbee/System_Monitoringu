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
    def update_uzytkownik(self, uzytkownik: Uzytkownik) -> None:
        self.__dao.update_uzytkownik(uzytkownik)

    def delete_uzytkownik(self, uzytkownik: Uzytkownik) -> None:
        self.__dao.delete_uzytkownik(uzytkownik)

    def get_uzytkownik(self, login: str) -> Optional[Uzytkownik]:
        for uzytkownik in self.__dao.get_uzytkownicy():
            if uzytkownik.get_login() == login:
                return uzytkownik
        return None

    # Metody zarządzania Czujnikami
    def update_czujnik(self, czujnik: Czujnik) -> None:
        self.__dao.update_czujnik(czujnik)

    def delete_czujnik(self, czujnik: Czujnik) -> None:
        self.__dao.delete_czujnik(czujnik)

    # Metody zarządzania Kamerami
    def update_kamera(self, kamera: Kamera) -> None:
        self.__dao.update_kamera(kamera)

    def delete_kamera(self, kamera: Kamera) -> None:
        self.__dao.delete_kamera(kamera)
