class Widok:
    """
    Klasa bazowa dla widoków. Odpowiada za wyświetlanie panelu logowania.
    """

    def wyswietl_panel_logowania(self) -> None:
        print("Wyświetlanie panelu logowania")


class WidokOchroniarza(Widok):
    """
    Klasa reprezentująca widok dla ochroniarza.
    """

    def wyswietl_formularz_kalibracja_czujnikow(self) -> None:
        print("Wyświetlanie formularza kalibracji czujników")

    def wyswietl_formularz_dodawania_czujnikow(self) -> None:
        print("Wyświetlanie formularza dodawania czujników")

    def wyswietl_formularz_zmiany_hasla(self) -> None:
        print("Wyświetlanie formularza zmiany hasła")

    def wyswietl_podglad_z_kamer(self) -> None:
        print("Wyświetlanie podglądu z kamer")

    def wyswietl_dane_z_czujnikow(self) -> None:
        print("Wyświetlanie danych z czujników")

    def wyswietl_panel_podgladu(self) -> None:
        print("Wyświetlanie panelu podglądu")

    def autoryzacja_popup(self) -> None:
        print("Wyświetlanie popupu autoryzacji")


class WidokAdministratora(Widok):
    """
    Klasa reprezentująca widok dla administratora.
    """

    def wyswietl_panel_sterowania_alarmem(self) -> None:
        print("Wyświetlanie panelu sterowania alarmem")

    def wyswietl_kamery_czujniki(self) -> None:
        print("Wyświetlanie kamer i czujników")


class Aplikacja:
    """
    Klasa główna aplikacji, inicjująca widok.
    """

    def __init__(self, widok: Widok):
        self.widok = widok

    def main(self) -> None:
        """
        Uruchamia aplikację i wyświetla domyślny panel logowania.
        """
        self.widok.wyswietl_panel_logowania()


if __name__ == "__main__":
    # Przykład użycia z WidokOchroniarza
    widok = WidokOchroniarza()
    aplikacja = Aplikacja(widok)
    aplikacja.main()

    # Przykład użycia z WidokAdministratora
    widok_admin = WidokAdministratora()
    aplikacja_admin = Aplikacja(widok_admin)
    aplikacja_admin.main()
