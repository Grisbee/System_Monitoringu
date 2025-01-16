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
