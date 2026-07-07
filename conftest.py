import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        yield page

        browser.close()


@pytest.fixture(scope="function")
def logged_in_page(page):

    login = LoginPage(page)

    login.open()

    login.login("standard_user", "secret_sauce")

    return page