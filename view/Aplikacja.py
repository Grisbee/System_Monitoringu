class Aplikacja:
    """
    Klasa główna aplikacji, inicjująca widok.
    """

    def __init__(self, widok: "Widok"):
        self.widok = widok

    def main(self) -> None:
        """
        Uruchamia aplikację i wyświetla domyślny panel logowania.
        """
        self.widok.wyswietl_panel_logowania()


if __name__ == "__main__":
    from view import WidokOchroniarza  # Ensure proper import
    widok = WidokOchroniarza()
    aplikacja = Aplikacja(widok)
    aplikacja.main()
