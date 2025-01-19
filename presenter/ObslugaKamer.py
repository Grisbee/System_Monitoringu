class ObslugaKamer:
    def usun_kamere(self, kamera: 'Kamera') -> None:
        print(f"Usuwanie kamery {kamera}")
        if autoryzacja_rfid(uzytkownik):
            Dao.delete_kamera(kamera)
            print(f"Usunięto kamerę {kamera}")
        else:
            print("Brak autoryzacji")
    def podglad_obrazu(self, tryb: str, kamery: Optional[List[bool]], pomieszczenie : Optional[str]) -> None:
        print(f"Podgląd obrazu w trybie {tryb}")
        if tryb == "pomieszczenie":
            lista_kamer = Dao.get_kamery()
            lista_czujnikow = Dao.get_czujniki()

            for index in range(len(lista_kamer)):
                if lista_kamer[index].get_pomieszczenie() != pomieszczenie:
                    lista_kamer.remove(lista_kamer[index])

            for index in range(len(lista_czujnikow)):
                if lista_czujnikow[index].get_pomieszczenie() != pomieszczenie:
                    lista_czujnikow.remove(lista_czujnikow[index])

        elif tryb == "kamery":
            lista_kamer = Dao.get_kamery()
            for index in range(len(kamery)):
                if kamery[index] == False:
                    lista_kamer.remove(lista_kamer[index])
    def autoryzacja_rfid(self, uzytkownik: 'User') -> bool:
        if uzytkownik.get_rfid() == True:
            return True
        else:
            return False

