class ObslugaLogowania:
    def login(self, login: str, haslo: str) -> None:
        print(f"Logowanie użytkownika: {login}")

    def zmien_haslo(self, haslo: str, nowe_haslo: str) -> None:
        print("Zmiana hasła")

    def zarejestruj(self, login: str, haslo: str) -> 'Uzytkownik':
        print(f"Rejestracja użytkownika: {login}")

