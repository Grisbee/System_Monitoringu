# Klasa Uzytkownik
class Uzytkownik:
    def __init__(self, login: str, haslo: str):
        self.__login = login
        self.__haslo = haslo
        self._authorised = "abc"

    def get_login(self) -> str:
        return self.__login

    def get_haslo(self) -> str:
        return self.__haslo

    def get_RFID(self, uzytkownik: str) -> str:
        if uzytkownik == self._authorised:
            return True

    def set_login(self, login: str) -> None:
        self.__login = login

    def set_haslo(self, haslo: str) -> None:
        self.__haslo = haslo

    def set_RFID(self, rfid: str) -> None:
        self._authorised = "abc"

