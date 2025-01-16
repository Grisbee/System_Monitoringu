# Interfejs FabrykaUrządzeń
from abc import ABC, abstractmethod

class FabrykaUrzadzen(ABC):
    @abstractmethod
    def dodaj_urzadzenie(self):
        pass
