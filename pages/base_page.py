from utils.config_reader import get_config


class BasePage:

    def __init__(self, page):
        self.page = page
        self.config = get_config()

    def open(self):
        self.page.goto(self.config["base_url"])

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def get_url(self):
        return self.page.url

    def get_text(self, locator):
        return self.page.locator(locator).text_content()