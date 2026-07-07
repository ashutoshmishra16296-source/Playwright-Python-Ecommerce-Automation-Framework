from pages.login_page import LoginPage
from pages.cart_page import CartPage


def test_remove_product(page):

    login = LoginPage(page)

    login.open()

    login.login("standard_user", "secret_sauce")

    cart = CartPage(page)

    cart.add_backpack()

    cart.remove_backpack()

    cart.open_cart()

    assert cart.cart_is_empty()