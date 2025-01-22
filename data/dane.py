import model.Alarm
from model.Kamera import Kamera
from model.Czujnik import Czujnik
from model.Alarm import Alarm
from model.Uzytkownik import Uzytkownik

lista_kamer = []
lista_czujnikow = []
lista_uzytkownikow = []


kamera1 = Kamera(1, "lobby")
kamera2 = Kamera(2, "lobby")
kamera3 = Kamera(3, "magazyn")
kamera4 = Kamera(4, "korytarz")
kamera5 = Kamera(5, "korytarz")

lista_kamer.append(kamera1)
lista_kamer.append(kamera2)
lista_kamer.append(kamera3)
lista_kamer.append(kamera4)
lista_kamer.append(kamera5)

czujnik1 = Czujnik(kod=1, pomieszczenie="korytarz", typ="wykrywacz_nacisku")
czujnik2 = Czujnik(kod=2, pomieszczenie="zsyp_na_kartofle", typ="wykrywacz_temperatury")
czujnik3 = Czujnik(kod=3, pomieszczenie="zsyp_na_kartofle", typ="wykrywacz_dymu")

lista_czujnikow.append(czujnik1)
lista_czujnikow.append(czujnik2)
lista_czujnikow.append(czujnik3)

for kamera in lista_kamer:
    print(kamera)
for czujnik in lista_czujnikow:
    print(czujnik)

print(kamera1.get_pomieszczenie())

alarm = Alarm(stan=False, tryb="czuwanie")

uzytkownik = Uzytkownik("barnaba", "maslo")
lista_uzytkownikow.insert(0, uzytkownik)

def get_lista_kamer():
    return lista_kamer

def get_lista_czujnikow():
    return lista_czujnikow
def set_lista_kamer(lista):
    print("stara lista ")
    lista_kamer = lista

def set_lista_czujnikow(lista):
    lista_czujnikow = lista


# kamera5.set_pomieszczenie_kamery(pomieszczenie=False)

# kamera5.set_kod_kamery("abc")
def get_lista_uzytkownikow():
    return lista_uzytkownikow