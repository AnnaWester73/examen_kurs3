# Svar på teorifrågor

## 1. Skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest

- Enhetstester testar enskilda funktioner eller klasser isolerat. De är snabba och hittar buggar tidigt.
- Integrationstester verifierar att olika delar fungerar tillsammans. Till exempel om man har en användare i systemet och en kassa-funktion, så testar integrationstestet att användaren faktiskt kan användas i kassan – något som enhetstesterna inte fångar eftersom de testar varje del isolerat.
- Prestandatester mäter hur snabbt systemet svarar och hur mycket last det klarar. Även om enhets- och integrationstester går igenom, så uppfyller systemet ingen funktion om det tar flera minuter att lägga upp en användare i kassan.
- Regressionstester är viktiga för underhåll. Om jag lägger till en ny funktion (t.ex. mobilnummer på användarkortet för att skicka SMS från kassan), måste det gamla flödet fortfarande fungera så att man kan söka upp kunden i kassan. Regressionstester körs efter ändringar så att gammal kod fortfarande fungerar ihop med ny kod.


## 2. Beskriv hur det går till när man arbetar med TDD
TDD står för Test-Driven Development och följer det som kallas Red-Green-Refactor:

1. Red — skriv ett test som beskriver önskat beteende. Testet failar eftersom funktionen inte finns än.
2. Green — skriv minsta möjliga kod för att få testet att passera.
3. Refactor — städa upp koden utan att bryta testet.

Sedan upprepar man flödet för nästa funktion. När enhetstesterna är på plats kompletterar man med integrationstester som verifierar att flera funktioner fungerar tillsammans, enligt samma metodik.
I detta projekt har jag använt TDD för backend-koden i `BookStore` och `FavoriteBooks`.


## 3. Beskriv hur BDD skiljer sig från TDD

- TDD utgår från ett utvecklarperspektiv. Testerna skrivs i kod (t.ex. pytest) och fokuserar på att verifiera att funktioner gör rätt sak internt.
- BDD utgår från ett användarperspektiv. 
- Testerna skrivs i Gherkin-syntax (Given/When/Then) som beskriver flöden i klartext. 
- Tanken är att även icke-tekniska personer ska kunna läsa testerna.
- BDD utgår ofta från "User stories", vilket gör att testerna följer affärsbehov i applikationen.
- BDD och TDD kompletterar varandra. I detta projekt har jag använt TDD för backend och BDD för webbsidans funktioner.


## 4. Vilka tester skulle du vilja använda i en webbsida som Läslistan?

För Läslistan skulle jag använda många snabba enhetstester, färre integrationstester, och flera end-to-end-tester för webbsidan.

I min anpassade test-pyramid skulle fokus vara på många enhetstester i botten som inte kostar så mycket, 
färre integrationstester i mitten då det inte finns så mycket logik som behöver integreras, 
och flera i toppen för att säkerställa användarupplevelsen. Det är en medveten avvikelse från klassisk test-pyramid där E2E-tester ska vara få
– men för en användarfokuserad webbsida som Läslistan tycker jag att det är motiverat.

