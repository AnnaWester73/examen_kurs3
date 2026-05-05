Feature: Favoritböcker

  Scenario: Markera en bok som favorit
    Given att jag navigerar till vyn Katalog
    When jag markerar boken "Nybörjarkurs i Python" som favorit
    Then ska boken "Nybörjarkurs i Python" vara markerad som favorit

  Scenario: Visa favoritböcker
    Given att jag navigerar till vyn Katalog
    When jag markerar boken "Nybörjarkurs i Python" som favorit
    And jag klickar på Mina böcker
    Then ska boken "Nybörjarkurs i Python" visas i Mina böcker

  Scenario: Ta bort en bok från favoriter
    Given att jag navigerar till vyn Katalog
    When jag markerar boken "Nybörjarkurs i Python" som favorit
    And jag avmarkerar boken "Nybörjarkurs i Python" som favorit
    And jag klickar på Mina böcker
    Then ska boken "Nybörjarkurs i Python" inte visas i Mina böcker

  Scenario: Mina böcker är tom när inga böcker är markerade som favoriter
    Given att jag navigerar till vyn Mina böcker
    Then ska inga favoritböcker visas