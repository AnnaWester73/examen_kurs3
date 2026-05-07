class BasePage:

    URL = "https://tap-ht25-testverktyg.github.io/exam/"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)