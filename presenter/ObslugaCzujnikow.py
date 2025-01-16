class ObslugaCzujnikow:
    def kalibracja_czujnika(self, czujnik: int, parametry: List[int]) -> None:
        print(f"Kalibracja czujnika {czujnik} z parametrami {parametry}")

    def usun_czujniki(self, czujnik: int) -> None:
        print(f"Usuwanie czujnika {czujnik}")

    def podglad_danych(self, czujniki: List[int]) -> None:
        print(f"Podgląd danych z czujników: {czujniki}")

