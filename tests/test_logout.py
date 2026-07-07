from pages.menu_page import MenuPage


def test_logout(logged_in_page):

    menu = MenuPage(logged_in_page)

    menu.open_menu()

    menu.logout()

    assert menu.is_login_page()