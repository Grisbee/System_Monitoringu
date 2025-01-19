from model.Kamera import Kamera
from model.Czujnik import Czujnik


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

def get_lista_kamer():
    return lista_kamer

def get_lista_czujnikow():
    return lista_czujnikow