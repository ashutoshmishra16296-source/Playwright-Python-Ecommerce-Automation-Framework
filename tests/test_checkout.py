from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout(page):

    login = LoginPage(page)

    login.open()

    login.login("standard_user", "secret_sauce")

    cart = CartPage(page)

    cart.add_backpack()

    cart.open_cart()

    checkout = CheckoutPage(page)

    checkout.start_checkout()

    checkout.enter_information(
        "Ashutosh",
        "Mishra",
        "751001"
    )

    checkout.continue_checkout()

    checkout.finish_order()

    assert checkout.order_successful()