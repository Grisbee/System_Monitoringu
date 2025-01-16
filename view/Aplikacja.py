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
    widok = WidokOchroniarza()
    aplikacja = Aplikacja(widok)
    aplikacja.main()
