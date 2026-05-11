import re
from features.pages.base_page import BasePage


class AppPage(BasePage):

    VIEWS = {
        "Katalog": {
            "button": "catalog",
            "view": ".catalog",
            "item_testid_prefix": "star",
        },
        "Lägg till bok": {
            "button": "add-book",
            "view": ".form",
        },
        "Mina böcker": {
            "button": "favorites",
            "view": ".favorites",
            "item_testid_prefix": "fav",
        },
        "Statistik": {
            "button": "statistics",
            "view": ".stats",
        },
    }

    # --- Navigation ---

    # Kontrollerar att alla navigeringsknappar finns på sidan.
    def navigation_is_visible(self):
        return all(self.page.get_by_test_id(view["button"]).is_visible() for view in self.VIEWS.values())

    # Klickar på rätt navigeringsknapp utifrån vynamn.
    def click_navigation(self, view_name):
        self.page.get_by_test_id(self.VIEWS[view_name]["button"]).click()

    # Kontrollerar att rätt vy visas efter navigation.
    def view_is_visible(self, view_name):
        return self.page.get_by_test_id(self.VIEWS[view_name]["button"]).is_disabled()

    # Navigerar till angiven vy, om vi inte redan är där.
    # Skyddar mot att klicka på en redan aktiv (disabled) nav-knapp.
    def go_to(self, view_name):
        if not self.view_is_visible(view_name):
            self.click_navigation(view_name)
    def go_to(self, view_name):
        if not self.view_is_visible(view_name):
            self.click_navigation(view_name)

    # --- Lägg till bok ---

    # Fyller i titel i formuläret.
    def fill_title(self, title):
        self.page.get_by_test_id("add-input-title").fill(title)

    # Fyller i författare i formuläret.
    def fill_author(self, author):
        self.page.get_by_test_id("add-input-author").fill(author)

    # Klickar på knappen för att lägga till ny bok.
    def click_add_new_book(self):
        self.page.get_by_test_id("add-submit").click()

    # Kontrollerar att formulärfälten är tomma.
    def form_fields_are_empty(self):
        title = self.page.get_by_test_id("add-input-title").input_value()
        author = self.page.get_by_test_id("add-input-author").input_value()
        return title == "" and author == ""

    # Kontrollerar att knappen Lägg till ny bok är inaktiv.
    def add_submit_button_is_disabled(self):
        return self.page.get_by_test_id("add-submit").is_disabled()


    # --- Bok-items i Katalog och Mina böcker ---

    # Hjälpmetod: returnerar locator för en boks item i angiven vy.
    def _book_item(self, view_name, title):
        prefix = self.VIEWS[view_name]["item_testid_prefix"]
        return self.page.get_by_test_id(f"{prefix}-{title}")

    # Kontrollerar att en bok visas i angiven vy (Katalog eller Mina böcker).
    def book_in_view_is_visible(self, view_name, title):
        return self._book_item(view_name, title).is_visible()

    # Räknar förekomster av en bok i angiven vy.
    def book_in_view_count(self, view_name, title):
        return self._book_item(view_name, title).count()

    # --- Favoritmarkering Katalog ---

    # Returnerar locator för Hjärta på en bok.
    def _star(self, title):
        return self.page.get_by_test_id(f"star-{title}")

    # Klickar på hjärta för att markera/avmarkera bok som favorit.
    def toggle_favorite(self, title):
        self._star(title).click()

    # Kontrollerar att en bok är favoritmarkerad
    def is_marked_as_favorite(self, title):
        class_name = self._star(title).get_attribute("class") or ""
        return "selected" in class_name


    # --- Favoritlistan Mina böcker ---

    # Kontrollerar att favoritlistan är tom.
    # Listan har test-id "book-list" och innehåller <li>-element per favorit.
    def favorites_list_is_empty(self):
        return self.page.get_by_test_id("book-list").locator("li").count() == 0


    # --- Statistik ---

    # Hjälpmetod: plockar ut första heltalet ur en text.
    def _extract_number(self, text):
        match = re.search(r"\d+", text)
        return int(match.group()) if match else None

    # Returnerar totalt antal böcker som heltal.
    def stats_total_books(self):
        text = self.page.get_by_test_id("book-count").inner_text()
        return self._extract_number(text)

    # Returnerar antal favoritmarkerade böcker som heltal.
    def stats_favorite_books(self):
        text = self.page.get_by_test_id("stars-count").inner_text()
        return self._extract_number(text)

    # Kontrollerar att totalt antal böcker visas i statistikvyn.
    def stats_total_is_visible(self):
        return self.page.get_by_test_id("book-count").is_visible()

    # Kontrollerar att antal favoritmarkerade böcker visas i statistikvyn.
    def stats_favorites_is_visible(self):
        return self.page.get_by_test_id("stars-count").is_visible()