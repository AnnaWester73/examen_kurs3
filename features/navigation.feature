Feature: Navigera mellan olika vyer

  Scenario: Visa navigeringsmenyn
    Given att jag öppnar Läslistan
    Then ska navigeringsmenyn visas

  Scenario: Katalog är aktiv från start
    Given att jag öppnar Läslistan
    Then ska vyn "Katalog" visas

  Scenario: Navigera till Lägg till bok
    Given att jag öppnar Läslistan
    When jag klickar på "Lägg till bok"
    Then ska vyn "Lägg till bok" visas

  Scenario: Navigera till Mina böcker
    Given att jag öppnar Läslistan
    When jag klickar på "Mina böcker"
    Then ska vyn "Mina böcker" visas

  Scenario: Navigera till Statistik
    Given att jag öppnar Läslistan
    When jag klickar på "Statistik"
    Then ska vyn "Statistik" visas
