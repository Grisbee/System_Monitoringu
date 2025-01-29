Feature: Kamera update functionality
  As a system user
  I want to update camera information
  So that I can modify camera details in the system

  Scenario: Update camera with ID and name
    Given Mam nową instancję kamery
    When Dodaję do listy kamerę o ID 6 i nazwie "salon"
    Then Najnowsza kamera na liście powinna mieć ID 6 i nazwe "salon"
