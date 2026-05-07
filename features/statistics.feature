Feature: Statistik

  Scenario: Visa total antal böcker
    Given att jag navigerar till vyn "Statistik"
    Then ska det totala antalet böcker visas

  Scenario: Visa antal favoritmarkerade böcker
    Given att jag navigerar till vyn "Katalog"
    When jag markerar boken "Learn Python in 21 Years" som favorit
    And jag klickar på "Statistik"
    Then ska antalet favoritmarkerade böcker visas

  Scenario: Statistik vid start
    Given att jag navigerar till vyn "Statistik"
    Then ska totalt antal böcker vara "13"
    And ska antal favoriter vara "0"

  Scenario: Totalt antal uppdateras när en bok läggs till
    Given att jag öppnar vyn Lägg till bok
    When jag fyller i titel "Madicken"
    And jag fyller i författare "Astrid Lindgren"
    And jag klickar på Lägg till ny bok
    And jag klickar på "Statistik"
    Then ska totalt antal böcker vara "14"

  Scenario: Antal favoriter ökar när en bok markeras
    Given att jag navigerar till vyn "Katalog"
    When jag markerar boken "Learn Python in 21 Years" som favorit
    And jag klickar på "Statistik"
    Then ska antal favoriter vara "1"

  Scenario: Antal favoriter återgår när bok avmarkeras
    Given att jag navigerar till vyn "Katalog"
    When jag markerar boken "Learn Python in 21 Years" som favorit
    And jag avmarkerar boken "Learn Python in 21 Years" som favorit
    And jag klickar på "Statistik"
    Then ska antal favoriter vara "0"