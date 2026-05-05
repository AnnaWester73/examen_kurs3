Feature: Statistik

  Scenario: Visa total antal böcker
    Given att jag navigerar till vyn Statistik
    Then ska det totala antalet böcker visas

  Scenario: Visa antal favoritmarkerade böcker
    Given att jag navigerar till vyn Katalog
    When jag markerar boken "Learn Python in 21 Years" som favorit
    And jag klickar på Statistik
    Then ska antalet favoritmarkerade böcker visas