Feature: Favoritböcker

  Scenario: Markera en bok som favorit
    Given att jag navigerar till vyn "Katalog"
    When jag markerar boken "Learn Python in 21 Years" som favorit
    Then ska boken "Learn Python in 21 Years" vara markerad som favorit

  Scenario: Visa favoritböcker
    Given att jag navigerar till vyn "Katalog"
    When jag markerar boken "Learn Python in 21 Years" som favorit
    And jag klickar på "Mina böcker"
    Then ska boken "Learn Python in 21 Years" visas i "Mina böcker"

  Scenario: Ta bort en bok från favoriter
    Given att jag navigerar till vyn "Katalog"
    When jag markerar boken "Learn Python in 21 Years" som favorit
    And jag avmarkerar boken "Learn Python in 21 Years" som favorit
    And jag klickar på "Mina böcker"
    Then ska boken "Learn Python in 21 Years" inte visas i "Mina böcker"

  Scenario: Flera böcker kan vara favoriter samtidigt
    Given att jag navigerar till vyn "Katalog"
    When jag markerar boken "Learn Python in 21 Years" som favorit
    And jag markerar boken "Agile Is a Feeling" som favorit
    And jag klickar på "Mina böcker"
    Then ska boken "Learn Python in 21 Years" visas i "Mina böcker"
    And ska boken "Agile Is a Feeling" visas i "Mina böcker"

  Scenario: "Mina böcker" är tom när inga böcker är markerade som favoriter
    Given att jag navigerar till vyn "Mina böcker"
    Then ska inga favoritböcker visas