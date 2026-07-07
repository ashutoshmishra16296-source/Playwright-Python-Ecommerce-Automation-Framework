from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout(logged_in_page):

    cart = CartPage(logged_in_page)

    cart.add_backpack()

    cart.open_cart()

    checkout = CheckoutPage(logged_in_page)

    checkout.start_checkout()

    checkout.enter_information(
        "Ashutosh",
        "Mishra",
        "751001"
    )

    checkout.continue_checkout()

    checkout.finish_order()

    assert checkout.order_successful()