from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_without_first_name(logged_in_page):

    cart = CartPage(logged_in_page)

    cart.add_backpack()

    cart.open_cart()

    checkout = CheckoutPage(logged_in_page)

    checkout.start_checkout()

    checkout.enter_information(
        "",
        "Mishra",
        "751001"
    )

    checkout.continue_checkout()

    assert "First Name is required" in checkout.get_error_message()


def test_checkout_without_last_name(logged_in_page):

    cart = CartPage(logged_in_page)

    cart.add_backpack()

    cart.open_cart()

    checkout = CheckoutPage(logged_in_page)

    checkout.start_checkout()

    checkout.enter_information(
        "Ashutosh",
        "",
        "751001"
    )

    checkout.continue_checkout()

    assert "Last Name is required" in checkout.get_error_message()


def test_checkout_without_postal_code(logged_in_page):

    cart = CartPage(logged_in_page)

    cart.add_backpack()

    cart.open_cart()

    checkout = CheckoutPage(logged_in_page)

    checkout.start_checkout()

    checkout.enter_information(
        "Ashutosh",
        "Mishra",
        ""
    )

    checkout.continue_checkout()

    assert "Postal Code is required" in checkout.get_error_message()