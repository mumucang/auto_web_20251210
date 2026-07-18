import pytest

from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage


@pytest.fixture(scope="function")
def login():
    login_page = LoginPage()
    login_page.open_page(login_page.login_url)
    login_page.login("sdfsdf", "123456")
    yield login_page.driver


@pytest.fixture(scope="function",autouse=True)
def my_account(login):
    my_accout_page = MyAccountPage(login)
    yield my_accout_page