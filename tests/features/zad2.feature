# features/kamera.feature
Feature: Testowanie funkcji klasy Kamera

  Scenario Outline: Pobieranie nazwy pomieszczenia dla różnych kamer
    Given istnieje kamera o ID <id> w pomieszczeniu "<pomieszczenie>"
    When pobieram nazwę pomieszczenia z kamery
    Then nazwa pomieszczenia powinna wynosić "<pomieszczenie>"

    Examples:
      | id | pomieszczenie |
      | 1  | schody        |
      | 2  | korytarz      |
      | 3  | salon        |

  Scenario: Update camera with ID and name
    Given Mam nową instancję kamery
    When Dodaję do listy kamerę o ID 6 i nazwie "salon"
    Then Najnowsza kamera na liście powinna mieć ID 6 i nazwę "salon"
