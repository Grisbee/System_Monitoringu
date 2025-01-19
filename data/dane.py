from model.Kamera import Kamera


lista_kamer = []

kamera1 = Kamera(1, "lobby")
kamera2 = Kamera(2, "lobby")
kamera3 = Kamera(3, "magazyn")
kamera4 = Kamera(4, "korytarz")
kamera5 = Kamera(5, "schody")

lista_kamer.append(kamera1)
lista_kamer.append(kamera2)
lista_kamer.append(kamera3)
lista_kamer.append(kamera4)
lista_kamer.append(kamera5)

for kamera in lista_kamer:
    print(kamera)

print(kamera1.get_pomieszczenie())

def get_lista_kamer():
    return lista_kamer