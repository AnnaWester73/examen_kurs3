Feature: Navigera mellan olika vyer

  Scenario: Visa startsidan
    Given att jag öppnar Läslistan
    Then ska startsidan visas med navigeringsalternativ

  Scenario: Navigera till Katalog
    Given att jag öppnar startsidan för Läslistan
    When jag klickar på Katalog
    Then ska katalogen med böcker visas

  Scenario: Navigera till Lägg till bok
    Given att jag öppnar startsidan för Läslistan
    When jag klickar på Lägg till bok
    Then ska formulär för att lägga till bok visas

  Scenario: Navigera till Mina böcker
    Given att jag öppnar startsidan för Läslistan
    When jag klickar på Mina böcker
    Then ska formulär för mina favoritböcker visas

  Scenario: Navigera till Statistik
    Given att jag öppnar startsidan för Läslistan
    When jag klickar på Statistik
    Then ska statistikvyn visas
