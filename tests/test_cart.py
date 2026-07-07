from pages.cart_page import CartPage


def test_add_product_to_cart(logged_in_page):

    cart = CartPage(logged_in_page)

    cart.add_backpack()

    cart.open_cart()

    assert cart.cart_has_product()