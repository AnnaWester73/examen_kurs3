Feature: Lägg till bok

  Scenario: Lägga till en bok
    Given att jag öppnar vyn Lägg till bok
    When jag fyller i titel "Nybörjarkurs i Python"
    And jag fyller i författare "Anna Wester"
    And jag klickar på Lägg till ny bok
    Then ska boken "Nybörjarkurs i Python" visas i katalogen

  Scenario: Hindra att lägga till bok utan titel
    Given att jag öppnar vyn Lägg till bok
    When jag lämnar titel tom
    And jag fyller i författare "Anna Wester"
    Then ska knappen Lägg till ny bok vara inaktiv

  Scenario: Hindra att lägga till bok utan författare
    Given att jag öppnar vyn Lägg till bok
    When jag fyller i titel "Nybörjarkurs i Python"
    And jag lämnar författare tom
    Then ska knappen Lägg till ny bok vara inaktiv

  Scenario: Formuläret återställs efter att bok lagts till
    Given att jag öppnar vyn Lägg till bok
    When jag fyller i titel "Nybörjarkurs i Python"
    And jag fyller i författare "Anna Wester"
    And jag klickar på Lägg till ny bok
    Then ska fälten vara tomma

  Scenario: Lägga till flera böcker
    Given att jag öppnar vyn Lägg till bok
    When jag fyller i titel "Nybörjarkurs i Python"
    And jag fyller i författare "Anna Wester"
    And jag klickar på Lägg till ny bok
    And jag fyller i titel "Annas mat"
    And jag fyller i författare "Anna Bergström"
    And jag klickar på Lägg till ny bok
    Then ska båda böckerna visas i katalogen

