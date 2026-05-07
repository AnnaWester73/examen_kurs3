from features.pages.base_page import BasePage


class AppPage(BasePage):
    URL = "https://tap-ht25-testverktyg.github.io/exam/"

    VIEWS = {
        "Katalog":{
            "button":"catalog",
            "view":".catalog",
        },
        "Lägg till bok":{
            "button":"add-book",
            "view":".form",
        },
        "Mina böcker":{
            "button":"favorites",
            "view":".favorites",
        },
        "Statistik":{
            "button":"statistics",
            "view":".stats",
        },
    }

    def open(self):
        self.page.goto(self.URL)

    # Kontrollerar att alla navigeringsknappar finns på sidan.
    def navigation_is_visible(self):
        return all(self.page.get_by_test_id(view["button"]).is_visible()for view in self.VIEWS.values())

    # Klickar på rätt navigeringsknapp utifrån vynamn.
    def click_navigation(self, view_name):
        self.page.get_by_test_id(self.VIEWS[view_name]["button"]).click()

    # Kontrollerar att rätt vy visas efter navigation.
    def view_is_visible(self, view_name):
        return self.page.locator(self.VIEWS[view_name]["view"]).is_visible()

    # Fyller i titel i formuläret.
    def fill_title(self, title):
        self.page.get_by_test_id("add-input-title").fill(title)

    # Fyller i författare i formuläret.
    def fill_author(self, author):
        self.page.get_by_test_id("add-input-author").fill(author)

    # Klickar på knappen för att lägga till ny bok.
    def click_add_new_book(self):
        self.page.get_by_test_id("add-submit").click()

    # Kontrollerar att böcker visas i katalogen.
    def book_is_visible_in_catalog(self, title):
        return self.page.get_by_test_id(f"star-{title}").is_visible()

    # Kontrollerar att formulärfälten är tomma.
    def form_fields_are_empty(self):
        return (self.page.get_by_test_id("add-input-title").input_value() == ""
                and self.page.get_by_test_id("add-input-author").input_value() == "")

    # Kontrollerar att knappen Lägg till ny bok är inaktiv.
    def add_submit_button_is_disabled(self):
        return self.page.get_by_test_id("add-submit").is_disabled()
