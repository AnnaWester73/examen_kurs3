Feature: Lägg till bok

  Scenario: Lägga till en bok
    Given att jag öppnar vyn Lägg till bok
    When jag fyller i titel "Nybörjarkurs i Python"
    And jag fyller i författare "Anna Wester"
    And jag klickar på Lägg till ny bok
    And jag klickar på "Katalog"
    Then ska boken "Nybörjarkurs i Python" visas i katalogen

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
    And jag klickar på "Katalog"
    Then ska boken "Nybörjarkurs i Python" visas i katalogen
    And ska boken "Annas mat" visas i katalogen

  Scenario Outline: Hindra att lägga till bok med saknade fält
    Given att jag öppnar vyn Lägg till bok
    When jag fyller i titel "<title>"
    And jag fyller i författare "<author>"
    Then ska knappen Lägg till ny bok vara inaktiv
    Examples:
      | title    | author          |
      | <null>   | Astrid Lindgren |
      | Madicken | <null>          |


