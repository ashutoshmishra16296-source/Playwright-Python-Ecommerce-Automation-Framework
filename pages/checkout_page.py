from pages.base_page import BasePage


class CheckoutPage(BasePage):

    checkout_button = "#checkout"
    first_name_input = "#first-name"
    last_name_input = "#last-name"
    postal_code_input = "#postal-code"
    continue_button = "#continue"
    finish_button = "#finish"
    complete_header = ".complete-header"
    error_message = '[data-test="error"]'

    def start_checkout(self):
        self.click(self.checkout_button)

    def enter_information(self, first_name, last_name, postal_code):
        self.fill(self.first_name_input, first_name)
        self.fill(self.last_name_input, last_name)
        self.fill(self.postal_code_input, postal_code)

    def continue_checkout(self):
        self.click(self.continue_button)

    def finish_order(self):
        self.click(self.finish_button)

    def order_successful(self):
        return self.is_visible(self.complete_header)

    def get_error_message(self):
        return self.page.locator(self.error_message).text_content()