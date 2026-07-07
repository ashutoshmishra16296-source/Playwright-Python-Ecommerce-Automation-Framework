from pages.login_page import LoginPage
from pages.cart_page import CartPage


def test_multiple_products(page):

    login = LoginPage(page)

    login.open()

    login.login("standard_user", "secret_sauce")

    cart = CartPage(page)

    cart.add_backpack()
    cart.add_bike_light()
    cart.add_tshirt()

    assert cart.get_cart_count() == "3"

    cart.open_cart()

    assert cart.get_total_items() == 3