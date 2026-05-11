# Examensarbeta för kurs 3 - Testautomatisering och testverktyg
### Inlämning: Anna Wester

Webbsidan som testas: <https://tap-ht25-testverktyg.github.io/exam/>

## Projektet innehåll
Projektet innehåller tester på flera nivåer för att täcka både backend-logik
och webbsidans funktionalitet ur ett användarperspektiv.

### Backend (pytest)
Backend-koden i `src/` består av två klasser, `BookStore` och `FavoriteBooks`, som utvecklats med TDD.
- Backend-logik för att hantera en lista med böcker
- Enhetstester (pytest)
- Integrationstester (pytest)

### Frontend (Behave + Playwright)
- BDD-tester
- Testerna använder Page Object för att hålla logiken kring webbsidans element separat från stegfilerna
- Scenario Online för att validera när fält är tomt i lägg till bok och navigering

### CI i GitHub
- GitHub Actions kör alla tester automatiskt vid push till `main`. Behave körs headless i CI.

### Designval och avgränsningar

## Hantering av favoriter
`BookStore` har en intern `FavoriteBooks` och delegerar favorithantering dit, så favoritlistan har bara en sanningskälla.

## Mock-tester
Jag använder inte mock-tester. Klasserna är små och välavgränsade, och integrationstesterna täcker samspelet mellan dem på ett naturligt sätt.


#
## Installation
```bash
pip install -r requirements.txt
playwright install
```
## Kör tester

### Pytest (unit + integration)
Kör alla pytest-tester:
```bash
pytest
```

Kör bara unit-tester:
```bash
pytest -m unit
```

Kör bara integrationstester:
```bash
pytest -m integration
```
### Behave (BDD)

Kör alla feature-filer:
```bash
behave
```

Kör en specifik feature-fil:
```bash
behave features/add_book.feature
```

Kör headless (utan att webbläsarfönster öppnas):
```bash
behave -D headless=true
```
## Projektstruktur

```
examen_kurs3/
├── .github/workflows/tests.yml    CI-konfiguration
├── src/                           Backend-kod (BookStore, FavoriteBooks)
├── tests/
│   ├── unit/                      Unit-tester
│   └── integration/               Integrationstester
├── features/
│   ├── pages/                     Page Object-klasser
│   ├── steps/                     Stegfiler
│   ├── environment.py             Behave-konfiguration
│   └── *.feature                  Feature-filer
├── ANSWERS.md                     Svar på teorifrågor
├── STORIES.md                     User stories
├── README.md                      Denna fil
├── pytest.ini                     Pytest-konfiguration
├── behave.ini                     Behave-konfiguration
└── requirements.txt               Beroenden
```
