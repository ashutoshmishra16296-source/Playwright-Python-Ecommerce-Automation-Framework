from pages.base_page import BasePage


class InventoryPage(BasePage):

    inventory_title = ".title"

    def is_inventory_displayed(self):
        return self.is_visible(self.inventory_title)
    