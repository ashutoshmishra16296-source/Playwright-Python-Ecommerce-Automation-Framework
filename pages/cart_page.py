from pages.base_page import BasePage


class CartPage(BasePage):

    # Add Product Buttons
    backpack = "#add-to-cart-sauce-labs-backpack"
    bike_light = "#add-to-cart-sauce-labs-bike-light"
    tshirt = "#add-to-cart-sauce-labs-bolt-t-shirt"

    # Remove Product Button
    remove_backpack_button = "#remove-sauce-labs-backpack"

    # Cart
    cart_icon = ".shopping_cart_link"
    cart_badge = ".shopping_cart_badge"
    cart_items = ".cart_item"

    # --------------------
    # Add Products
    # --------------------

    def add_backpack(self):
        self.click(self.backpack)

    def add_bike_light(self):
        self.click(self.bike_light)

    def add_tshirt(self):
        self.click(self.tshirt)

    # --------------------
    # Remove Product
    # --------------------

    def remove_backpack(self):
        self.click(self.remove_backpack_button)

    # --------------------
    # Cart Operations
    # --------------------

    def open_cart(self):
        self.click(self.cart_icon)

    def cart_has_product(self):
        return self.is_visible(self.cart_items)

    def cart_is_empty(self):
        return self.page.locator(self.cart_items).count() == 0

    def get_cart_count(self):
        return self.page.locator(self.cart_badge).text_content()

    def get_total_items(self):
        return self.page.locator(self.cart_items).count()