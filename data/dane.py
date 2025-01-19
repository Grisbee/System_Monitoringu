import model.Alarm
from model.Kamera import Kamera
from model.Czujnik import Czujnik
from model.Alarm import Alarm

lista_kamer = []
lista_czujnikow = []


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

czujnik1 = Czujnik(kod=1, pomieszczenie="korytarz", typ="wykrywacz_twojej_starej")

lista_czujnikow.append(czujnik1)

for kamera in lista_kamer:
    print(kamera)
for czujnik in lista_czujnikow:
    print(czujnik)

print(kamera1.get_pomieszczenie())

alarm = Alarm(stan=False, tryb="czuwanie")

def get_lista_kamer():
    return lista_kamer

def get_lista_czujnikow():
    return lista_czujnikow
def set_lista_kamer(lista):
    print("stara lista ")
    lista_kamer = lista

def set_lista_czujnikow(lista):
    lista_czujnikow = lista


kamera5.set_pomieszczenie_kamery(pomieszczenie=False)

p = kamera5.get_pomieszczenie()
print(p)

kamera5.set_kod_kamery("abc")
