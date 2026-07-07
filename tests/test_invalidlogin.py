from playwright.sync_api import Page
from pages.login_page import LoginPage


def test_invalid_login(page: Page):

    login = LoginPage(page)

    login.open()

    login.login("abc", "123")

    assert login.login_failed()