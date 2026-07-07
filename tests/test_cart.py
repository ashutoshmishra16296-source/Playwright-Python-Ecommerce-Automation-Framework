from pages.login_page import LoginPage
from pages.cart_page import CartPage


def test_add_product_to_cart(page):

    login = LoginPage(page)

    login.open()

    login.login("standard_user", "secret_sauce")

    cart = CartPage(page)

    cart.add_backpack()

    cart.open_cart()

    assert cart.cart_has_product()