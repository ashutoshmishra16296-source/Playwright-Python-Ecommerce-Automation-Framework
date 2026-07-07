from pages.base_page import BasePage


class CartPage(BasePage):

    add_backpack_button = "#add-to-cart-sauce-labs-backpack"
    remove_backpack_button = "#remove-sauce-labs-backpack"
    cart_icon = ".shopping_cart_link"
    cart_item = ".cart_item"

    def add_backpack(self):
        self.click(self.add_backpack_button)

    def remove_backpack(self):
        self.click(self.remove_backpack_button)

    def open_cart(self):
        self.click(self.cart_icon)

    def cart_has_product(self):
        return self.is_visible(self.cart_item)

    def cart_is_empty(self):
        return self.page.locator(self.cart_item).count() == 0