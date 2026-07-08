from pages.base_page import BasePage
from utils.logger import logger


class LoginPage(BasePage):

    # Locators
    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"
    error_message = '[data-test="error"]'

    # Open Login Page
    def open(self):
        logger.info("Opening SauceDemo Login Page")
        self.page.goto("https://www.saucedemo.com/")

    # Login Method
    def login(self, username, password):
        logger.info(f"Logging in with username: {username}")
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    # Verify Successful Login
    def login_successful(self):
        logger.info("Checking if login was successful")
        return "inventory" in self.get_url()

    # Verify Failed Login
    def login_failed(self):
        logger.info("Checking if login failed")
        return self.is_visible(self.error_message)

    # Get Error Message
    def get_error_message(self):
        logger.info("Fetching login error message")
        return self.page.locator(self.error_message).text_content()