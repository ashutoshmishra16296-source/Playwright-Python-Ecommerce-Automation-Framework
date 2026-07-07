from pages.base_page import BasePage


class SortPage(BasePage):

    sort_dropdown = ".product_sort_container"
    inventory_items = ".inventory_item_name"

    def sort_by(self, value):
        self.page.locator(self.sort_dropdown).select_option(value)

    def get_product_names(self):
        return self.page.locator(self.inventory_items).all_text_contents()