Feature: Zarządzanie systemem kamer

  Scenario: Dodaj nową kamerę o id 6 i pomieszczeniu salon
    Given Mam nową instancję kamery
    When Dodaję do listy kamerę o ID 6 i nazwie "salon"
    Then Najnowsza kamera na liście powinna mieć ID 6 i nazwe "salon"

    Scenario: Usuń kamerę z listy o id 6 i pomieszczeniu korytarz
    Given Mam listę kamer i instancje kamery do usuniecia
    When Usuwam kamerę o ID 6
    Then Kamera o ID 6 nie powinna znajdować się na liście