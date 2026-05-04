# Examensarbeta för kurs 3 - Testautomatisering och testverktyg
### Inlämning: Anna Wester

## Projektet innehåll
Se länk:
```
https://docs.google.com/document/d/1YFubvcXCJx71fedHHOjv6RWh-vhmXFRmh602V8g1WGo/edit?tab=t.0
```
- Backend-logik för att hantera en lista med böcker
- Enhetstester (pytest)
- Integrationstester (kommer senare)
- Frontend-del (kommer senare)
- BDD-tester med Behave (kommer senare)
- CI med GitHub Actions
- Teori frågor (kommer senare)

## Teststrategi 
Projektet använder flera nivåer av tester:
### Tekniska tester
- Pytest för unit och integrationstester
- Testar backen-logik i klasserna BookStore och FavoriteBooks

### UI tester (BDD)
- User stories finns ./STORIES.md
- Acceptanskriterier och scenarios finns ./features/feature-filer
  - skrivna i Gherkin-format
- Step filer för att implementera tester med Behave och Playwright
- Testar applikationen ur ett användarperspektiv

### Sammanfattning
- Unit tester → testar enskilda metoder
- Integrationstester → testar samspel mellan klasser
- UI-tester → testar hela flöden i användargränssnittet

## Dokumentation
TODO

## Installation
```bash
pip install -r requirements.txt
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

