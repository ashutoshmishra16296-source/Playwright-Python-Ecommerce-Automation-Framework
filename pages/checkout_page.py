from pages.base_page import BasePage


class CheckoutPage(BasePage):

    checkout_button = "#checkout"
    first_name = "#first-name"
    last_name = "#last-name"
    postal_code = "#postal-code"
    continue_button = "#continue"
    finish_button = "#finish"
    complete_header = ".complete-header"

    def start_checkout(self):
        self.click(self.checkout_button)

    def enter_information(self, first, last, zip_code):
        self.fill(self.first_name, first)
        self.fill(self.last_name, last)
        self.fill(self.postal_code, zip_code)

    def continue_checkout(self):
        self.click(self.continue_button)

    def finish_order(self):
        self.click(self.finish_button)

    def order_successful(self):
        return self.page.locator(self.complete_header).text_content() == "Thank you for your order!"