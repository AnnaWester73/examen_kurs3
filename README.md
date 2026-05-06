# Examensarbeta för kurs 3 - Testautomatisering och testverktyg
### Inlämning: Anna Wester

## Projektet innehåll
Se länk:
```
https://docs.google.com/document/d/1YFubvcXCJx71fedHHOjv6RWh-vhmXFRmh602V8g1WGo/edit?tab=t.0
```
- Backend-logik för att hantera en lista med böcker
- Enhetstester (pytest)
- Integrationstester (pytest)
- Frontend-del
- BDD-tester med Behave och Playwright
- CI med GitHub Actions
- Teorifrågor (kommer senare)

## Teststrategi 
Projektet använder flera nivåer av tester:
### Tekniska tester
- Pytest för unit och integrationstester
- Testar backend-logik i klasserna BookStore och FavoriteBooks

### UI tester (BDD)
- User stories finns ./STORIES.md
- Acceptanskriterier och scenarios finns ./features/feature-filer
  - skrivna i Gherkin-format
- Step filer för att implementera tester med Behave och 
- Scenario Outline används för BDD Scenario i add-book
- Testar applikationen ur ett användarperspektiv

## Dokumentation
TODO

## Installation
```bash
pip install -r requirements.txt
playwright install
```
## Kör tester

### Kör alla tester
```bash
pytest
```
### Kör unit tester
```bash
pytest -m unit
```
### Kör integrations tester
```bash
pytest -m integration
```
## Kör behave tester
```bash
behave TODO
```

