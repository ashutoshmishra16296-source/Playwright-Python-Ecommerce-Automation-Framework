from pages.base_page import BasePage
from utils.logger import get_logger


class LoginPage(BasePage):

    logger = get_logger()

    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"
    error_message = '[data-test="error"]'

    def login(self, username, password):

        self.logger.info("Entering Username")
        self.fill(self.username_input, username)

        self.logger.info("Entering Password")
        self.fill(self.password_input, password)

        self.logger.info("Clicking Login Button")
        self.click(self.login_button)

    def login_successful(self):
        return "inventory" in self.get_url()

    def login_failed(self):
        return self.is_visible(self.error_message)