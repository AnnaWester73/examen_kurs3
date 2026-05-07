Feature: Navigera mellan olika vyer

  Scenario: Visa navigeringsmenyn
    Given att jag öppnar Läslistan
    Then ska navigeringsmenyn visas

  Scenario: Katalog är aktiv från start
    Given att jag öppnar Läslistan
    Then ska vyn "Katalog" visas

  Scenario Outline: Navigera mellan vyer
    Given att jag öppnar Läslistan
    When jag klickar på "<view>"
    Then ska vyn "<view>" visas
    Examples:
      | view          |
      | Lägg till bok |
      | Mina böcker   |
      | Statistik     |

  Scenario: Återgå till Katalog efter att ha bytt vy
    Given att jag öppnar Läslistan
    When jag klickar på "Lägg till bok"
    And jag klickar på "Katalog"
    Then ska vyn "Katalog" visas
