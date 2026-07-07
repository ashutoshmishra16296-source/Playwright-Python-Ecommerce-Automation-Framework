from pages.inventory_page import InventoryPage


def test_inventory(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    assert inventory.is_inventory_displayed()