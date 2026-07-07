from pages.base_page import BasePage


class MenuPage(BasePage):

    menu_button = "#react-burger-menu-btn"
    logout_button = "#logout_sidebar_link"

    def open_menu(self):
        self.click(self.menu_button)

    def logout(self):
        self.click(self.logout_button)

    def is_login_page(self):
        return "saucedemo.com" in self.get_url()