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
