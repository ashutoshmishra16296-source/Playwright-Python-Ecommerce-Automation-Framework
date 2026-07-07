import pytest

from pages.login_page import LoginPage
from utils.csv_reader import get_login_data


@pytest.mark.parametrize(
    "username,password,expected",
    get_login_data()
)
def test_login(page, username, password, expected):

    login = LoginPage(page)

    login.open()
    login.login(username, password)

    if expected == "pass":
        assert login.login_successful()
    else:
        assert login.login_failed()